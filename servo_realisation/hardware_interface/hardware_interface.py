import abc
import canalystii


class HardwareInterface(abc.ABC):
    @abc.abstractmethod
    def open_connection(self):
        raise NotImplemented

    @abc.abstractmethod
    def connection_is_opened(self):
        raise NotImplemented

    @abc.abstractmethod
    def send(self, message: canalystii.Message, command_id: int, servo_id: int, is_read: bool):
        raise NotImplemented

    @abc.abstractmethod
    def send_without_buffer(self, message: canalystii.Message):
        raise NotImplemented
    
    @abc.abstractmethod
    def receive(self):
        raise NotImplemented

    @abc.abstractmethod
    def check_is_device_buffer_empty(self) -> bool:
        raise NotImplemented

    @abc.abstractmethod
    def close_connection(self):
        raise NotImplemented
