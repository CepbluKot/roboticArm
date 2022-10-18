import abc


class ServoInterface(abc.ABC):
    @abc.abstractmethod
    def recieve(self, channel: int):
        raise NotImplemented

    @abc.abstractmethod
    def send(self, channel: int, messages):
        raise NotImplemented
