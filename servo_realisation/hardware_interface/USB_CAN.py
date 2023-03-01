import canalystii
import threading
import typing
import time
import copy
from servo_realisation.hardware_interface.hardware_interface import HardwareInterface
from servo_realisation.protocol_interface.CanOpen301 import ReceievedMessage


class QueueMessage:
    def __init__(self, message: canalystii.Message, last_send_time: float) -> None:
        self.message = message
        self.attempts = 0
        self.last_send_time = last_send_time


class MessagesBuffer:
    def __init__(self, lock: threading.Lock) -> None:
        self.messages_buffer: typing.Dict[int, typing.Dict[int, typing.Dict[bool, QueueMessage]]] = {}
        self.lock = lock

    def get(self):
        with self.lock:
            return copy.deepcopy(self.messages_buffer)

    def set(self, command_id, servo_id, is_read: bool, msg: QueueMessage):
        with self.lock:
            if not command_id in self.messages_buffer:
                self.messages_buffer[command_id] = {}

            if not servo_id in self.messages_buffer[command_id]:
                self.messages_buffer[command_id][servo_id] = {}

            self.messages_buffer[command_id][servo_id][is_read] = msg

    def update(self, command_id, servo_id, is_read: bool, new_msg: QueueMessage):
        with self.lock:
            if command_id in self.messages_buffer:
                if servo_id in self.messages_buffer[command_id]:
                    if is_read in self.messages_buffer[command_id][servo_id]:
                        self.messages_buffer[command_id][servo_id][is_read] = new_msg

    def delete(self, command_id, servo_id, is_read: bool):
        with self.lock:
            if command_id in self.messages_buffer:
                if servo_id in self.messages_buffer[command_id]:
                    if is_read in self.messages_buffer[command_id][servo_id]:
                        msg = self.messages_buffer[command_id][servo_id][is_read]
                        self.messages_buffer[command_id][servo_id].pop(is_read, None)
                        
                        if command_id == 'interpolation' or command_id[1] == 0x81 or command_id[1] == 0x83:
                            print('removed from buffer:', 'servo_id', servo_id,  'command_id', command_id, )
    
    

    def check_is_empty(self):
        with self.lock:
            is_empty = True
            
            if self.messages_buffer:
                for command_id in self.messages_buffer:
                    if self.messages_buffer[command_id]:
                        for servo_id in self.messages_buffer[command_id]:
                            if self.messages_buffer[command_id][servo_id]:
                                # print('wtf', self.messages_buffer[command_id][servo_id][is_read].message.can_id)
                                is_empty = False
            
            return is_empty

            
class USB_CAN(HardwareInterface):
    def __init__(
        self,
        bus_id: int,
        bitrate: int,
        on_recieve: typing.Callable[[canalystii.protocol.Message], ReceievedMessage],
    ) -> None:
        self.bus_id = bus_id
        self.on_recieve = on_recieve
        try:
            self.device = canalystii.CanalystDevice(
                bitrate=bitrate, device_index=bus_id
            )
        except:
            print("error - opening usbcan device")

        self.sent_messages_buffer_lock = threading.Lock()

        self.sent_messages_buffer = MessagesBuffer(
            self.sent_messages_buffer_lock
        )  # command_id: {servoid: message}

        self.read_thread = threading.Thread(target=self.__read_thread, daemon=True)
        if not self.read_thread.is_alive():
            try:
                self.read_thread.start()
            except:
                print("start read thread - error")

        self.send_thread = threading.Thread(target=self.__send_thread, daemon=True)
        if not self.send_thread.is_alive():
            try:
                self.send_thread.start()
            except:
                print("start send thread - error")

        # self.debug_thread = threading.Thread(target=self.__debug_thr)
        # if not self.debug_thread.is_alive():
        #     try:
        #         self.debug_thread.start()
        #     except:
        #         print("start debug thread - error")

    def __read_thread(self):
        while self.read_thread.is_alive():
            # print('read thread alive', time.time())
            try:
                recv = self.device.receive(self.bus_id)
                if recv:
                    for message in recv:

                        # print("recieved --> ", message)
                        parsed = self.on_recieve(message)

                        
                        self.__queue_recieved_msg_handler(parsed)

            except:
                print("read thread - error")
                self.read_thread.join()
                return False

    def __send_thread(self):
        while self.send_thread.is_alive():
            # print('send thread alive', time.time())
            sent_messages_buffer_copy = self.sent_messages_buffer.get()

            if not sent_messages_buffer_copy:
                continue

            for command_id in sent_messages_buffer_copy:
                for servo_id in sent_messages_buffer_copy[command_id]:
                    for is_read in sent_messages_buffer_copy[command_id][servo_id]:
                        if (
                            time.time()
                            - sent_messages_buffer_copy[command_id][servo_id][is_read].last_send_time
                            > 1
                        ):
                            msg = sent_messages_buffer_copy[command_id][servo_id][is_read]
                            msg.attempts += 1
                            msg.last_send_time = time.time()
                            self.__send_again(message=msg.message)
                            # print("send again", msg.attempts, msg.last_send_time, time.time(), is_read)
                            self.sent_messages_buffer.update(
                                command_id=command_id, servo_id=servo_id, new_msg=msg, is_read=is_read
                            )
                            # print("sent again --> ", self.sent_messages_buffer[command_id][servo_id].message)

    def __debug_thr(self):
        while True:
            time.sleep(0.01)
            print('---------------')

            buffa = self.sent_messages_buffer.get()
            for code in buffa:
                for com_id in buffa[code]:
                    for is_read in buffa[code][com_id]:
                        print("comm_id", code, "servo_id", com_id, 'is_read', is_read, "|", buffa[code][com_id][is_read].message)
            
            pass

    def __queue_send_msg(self, msg: canalystii.Message, command_id: int, servo_id: int, is_read: bool):
        msg = QueueMessage(message=msg, last_send_time=time.time())
        self.sent_messages_buffer.set(command_id=command_id, servo_id=servo_id, msg=msg, is_read=is_read)

    def __queue_recieved_msg_handler(self, msg: ReceievedMessage):
        self.sent_messages_buffer.delete(
            command_id=msg.command_data, servo_id=msg.servo_id, is_read=msg.is_read
        )
        
    def get_buffer(self):
        return self.sent_messages_buffer.get()

    def open_connection(self):
        try:
            # self.device.start(channel=self.bus_id)

            if not self.read_thread.is_alive():
                self.read_thread.start()

            return True
        except:
            print("open connection - error")
            return False

    def connection_is_opened(self):
        return self.device.get_can_status()

    def send(self, message: canalystii.Message, command_id: int, servo_id: int, is_read: bool):
        # try:
            # print('added to buffer:', 'servo_id', servo_id,  'command_id', command_id, )
            self.__queue_send_msg(msg=message, command_id=command_id, servo_id=servo_id, is_read=is_read)
            return self.device.send(channel=self.bus_id, messages=message)
            # pass
        # except:
            print("send - error")
            return False

    def send_without_buffer(self, message: canalystii.Message):
        return self.device.send(channel=self.bus_id, messages=message)

    def __send_again(self, message: canalystii.Message):
        self.device.send(channel=self.bus_id, messages=message)

    def receive(self):
        try:
            return self.device.receive(channel=self.bus_id)
        except:
            print("receive - error")
            return False

    def check_is_device_buffer_empty(self):
        return self.sent_messages_buffer.check_is_empty()

    def close_connection(self):
        try:
            self.device.stop(channel=self.bus_id)
            if self.read_thread.is_alive():
                self.read_thread.join()

            return True
        except:
            print("close connection - error")
            return False
