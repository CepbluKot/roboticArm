import canalystii
import abc


class CommandConstructorInterface:
    @abc.abstractmethod
    def create_command(
        self,
        command_from_documentation: str,
        is_read: bool = False,
        is_write: bool = False,
        address: int = 601,
        write_value: int = None,
    ) -> canalystii.Message:
        raise NotImplemented
