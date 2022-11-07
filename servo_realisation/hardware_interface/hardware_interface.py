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
    def send(self, message: canalystii.Message, command_id: int, servo_id: int):
        raise NotImplemented

    @abc.abstractmethod
    def receive(self):
        raise NotImplemented

    @abc.abstractmethod
    def close_connection(self):
        raise NotImplemented
