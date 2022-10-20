import abc
import canalystii
import can


class ServoInterface(abc.ABC):
    servo_id = int
    device = canalystii.CanalystDevice

    @abc.abstractmethod
    def receive(self, channel: int):
        raise NotImplementedError

    @abc.abstractmethod
    def send(self, channel: int, message):
        raise NotImplementedError


class ServoInterfaceCan(abc.ABC):
    servo_id = int
    device = can.interface.Bus

    @abc.abstractmethod
    def receive(self):
        raise NotImplementedError

    @abc.abstractmethod
    def send(self, message):
        raise NotImplementedError
