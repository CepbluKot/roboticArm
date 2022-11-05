import canalystii
import threading
import typing
from servo_realisation.hardware_interface.hardware_interface import HardwareInterface


class USB_CAN(HardwareInterface):
    def __init__(self, bus_id: int, process_message_func: typing.Callable(canalystii.Message)) -> None:
        self.bus_id = bus_id
        self.device = canalystii.CanalystDevice(bitrate=1000000, device_index=bus_id)
        self.send_to_storage_func = process_message_func

        self.read_thread = threading.Thread(target=self.__thread)
    
        if not self.read_thread.is_alive():
            try:
                self.read_thread.start()
            except:
                print('start thread - error')


    def __thread(self):
        while self.read_thread.is_alive():
            try:
                recv = self.device.receive()
                while not recv:
                    recv = self.device.receive()
                
                for message in recv:
                    self.send_to_storage_func(message)
                    
            except:
                print('read thread - error')
                self.read_thread.join()
                return False

    def open_connection(self):
        try:
            self.device.start(channel=self.bus_id)

            if not self.read_thread.is_alive():
                self.read_thread.start()
            
            return True
        except:
            print('open connection - error')
            return False

    def connection_is_opened(self):
        return self.device.get_can_status() 

    def send(self, message: canalystii.Message):
            try:
                return self.device.send(channel=self.bus_id, messages=message)
            except:
                print('send - error')
                return False

    def receive(self):
        try:
            return self.device.receive(channel=self.bus_id)
        except:
            print('receive - error')
            return False

    def close_connection(self):
        try:
            self.device.stop(channel=self.bus_id)
            if self.read_thread.is_alive():
                self.read_thread.join()

            return True
        except:
            print('close connection - error')
            return False
