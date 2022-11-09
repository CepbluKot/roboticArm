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
        self.messages_buffer = {}
        self.lock = lock

    def get(self):
        with self.lock:
            return copy.deepcopy(self.messages_buffer)

    def set(self, command_id, servo_id):
        with self.lock:
            return self.messages_buffer[command_id][servo_id]

    def delete(self, command_id, servo_id):
        with self.lock:
            if command_id in self.messages_buffer:
                self.messages_buffer[command_id].pop(servo_id)


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

        self.sent_messages_buffer: typing.Dict[
            int, typing.Dict[int, QueueMessage]
        ] = {}  # command_id: {servoid: message}

        self.sent_messages_buffer_lock = threading.Lock()

        self.read_thread = threading.Thread(target=self.__read_thread)
        if not self.read_thread.is_alive():
            try:
                self.read_thread.start()
            except:
                print("start read thread - error")

        self.send_thread = threading.Thread(target=self.__send_thread)
        if not self.send_thread.is_alive():
            try:
                self.send_thread.start()
            except:
                print("start send thread - error")

        self.debug_thread = threading.Thread(target=self.__debug_thr)
        if not self.debug_thread.is_alive():
            try:
                self.debug_thread.start()
            except:
                print("start debug thread - error")

    def __read_thread(self):
        while self.read_thread.is_alive():
            # try:
            self.device.clear_rx_buffer(self.bus_id)
            recv = self.device.receive(self.bus_id)

            if recv:
                for message in recv:

                    # print("recieved --> ", message)
                    parsed = self.on_recieve(message)
                    self.__queue_recieved_msg_handler(parsed)

        # except:
        # print("read thread - error")
        # self.read_thread.join()
        # return False

    def __send_thread(self):
        while self.send_thread.is_alive():
            if not self.sent_messages_buffer:
                pass

            sent_messages_buffer_copy = dict(self.sent_messages_buffer)
            for command_id in sent_messages_buffer_copy:
                for servo_id in sent_messages_buffer_copy[command_id]:
                    if time.time() - sent_messages_buffer_copy[command_id][servo_id].last_send_time > 1:
                        self.__send_again(
                            message=sent_messages_buffer_copy[command_id][
                                servo_id
                            ].message,
                            command_id=command_id,
                            servo_id=servo_id
                        )
                        # print("sent again --> ", self.sent_messages_buffer[command_id][servo_id].message)

    def __debug_thr(self):
        while True:
            time.sleep(0.2)
            # print('---------------')
            
            if self.sent_messages_buffer:
                print(self.sent_messages_buffer)
                

    def __queue_send_msg(self, msg: canalystii.Message, command_id: int, servo_id: int):
            if command_id not in self.sent_messages_buffer:
                self.sent_messages_buffer[command_id] = {}
            self.sent_messages_buffer[command_id][servo_id] = QueueMessage(message=msg, last_send_time=time.time())

    def __queue_recieved_msg_handler(self, msg: ReceievedMessage):
        if msg.command_data in self.sent_messages_buffer:
            if msg.servo_id in self.sent_messages_buffer[msg.command_data]:
                print('removing', self.sent_messages_buffer[msg.command_data][msg.servo_id].message)
                self.sent_messages_buffer[msg.command_data].pop(msg.servo_id, None)

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

    def send(self, message: canalystii.Message, command_id: int, servo_id: int):
        try:
            self.__queue_send_msg(msg=message, command_id=command_id, servo_id=servo_id)
            # return self.device.send(channel=self.bus_id, messages=message)
            pass
        except:
            print("send - error")
            return False

    def __send_again(self, message: canalystii.Message, command_id: int, servo_id: int):
        if command_id in self.sent_messages_buffer:
            if servo_id in self.sent_messages_buffer[command_id]:
                self.sent_messages_buffer[command_id][servo_id].attempts += 1
                self.sent_messages_buffer[command_id][servo_id].last_send_time = time.time()
                self.device.send(channel=self.bus_id, messages=message)

    def receive(self):
        try:
            return self.device.receive(channel=self.bus_id)
        except:
            print("receive - error")
            return False

    def close_connection(self):
        try:
            self.device.stop(channel=self.bus_id)
            if self.read_thread.is_alive():
                self.read_thread.join()

            return True
        except:
            print("close connection - error")
            return False
