import abc
import servo_realisation.commands_reader.commands_reader_data_structures


class CommandsReaderInterface(abc.ABC):
    @abc.abstractmethod
    def read_recieve(self, recieve: str) -> servo_realisation.commands_reader.commands_reader_data_structures.RecievedCommand:
        raise NotImplemented
