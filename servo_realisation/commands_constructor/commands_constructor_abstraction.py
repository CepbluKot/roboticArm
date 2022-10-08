import servo_realisation.commands_constructor.commands_constructor_interface
import canalystii


class CommandConstructorAbstraction(
    servo_realisation.commands_constructor.commands_constructor_interface.CommandConstructorInterface
):
    def __init__(
        self,
        interface: servo_realisation.commands_constructor.commands_constructor_interface.CommandConstructorInterface,
    ) -> None:
        self.interface = interface

    def create_command(
        self,
        command_from_documentation: str,
        is_read: bool = False,
        is_write: bool = False,
        address: int = 601,
        write_value: int = None,
    ) -> canalystii.Message:
        return self.interface.create_command(
            command_from_documentation=command_from_documentation,
            is_read=is_read,
            is_write=is_write,
            address=address,
            write_value=write_value,
        )
