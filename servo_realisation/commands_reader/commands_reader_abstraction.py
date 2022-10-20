import servo_realisation.commands_reader.commands_reader_interface
import servo_realisation.commands_reader.commands_reader_data_structures

class CommandsReaderAbstraction(
    servo_realisation.commands_reader.commands_reader_interface.CommandsReaderInterface
):
    def __init__(
        self,
        interface: servo_realisation.commands_reader.commands_reader_interface.CommandsReaderInterface,
    ) -> None:
        self.interface = interface

    def read_recieve(self, recieve):
        return self.interface.read_recieve(recieve=recieve)
