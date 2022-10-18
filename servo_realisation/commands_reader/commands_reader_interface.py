import abc


class CommandsReaderInterface(abc.ABC):
    @abc.abstractmethod
    def read_recieve(self, recieve: str):
        raise NotImplemented
