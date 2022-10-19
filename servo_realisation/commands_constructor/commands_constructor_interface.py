import abc
import canalystii
import servo_realisation.control_objects.servo_interface


class CommandConstructorInterface:
    @abc.abstractmethod
    def general_move_command(self):
        raise NotImplementedError

    @abc.abstractmethod
    def create_command(
        self,
        address: int,
        command_from_documentation: str,
        write_value: int = None,
    ) -> canalystii.Message:
        raise NotImplementedError

    @abc.abstractmethod
    def only_convert_write_value_to_hex(self, write_value: int, num_of_bytes_for_command: int):
        raise NotImplementedError
