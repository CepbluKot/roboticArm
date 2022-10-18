import servo_realisation.commands_constructor.commands_constructor_interface
import canalystii
import servo_realisation.control_objects.servo_interface


class CommandConstructorAbstraction(
    servo_realisation.commands_constructor.commands_constructor_interface.CommandConstructorInterface
):
    def __init__(
        self,
        interface: servo_realisation.commands_constructor.commands_constructor_interface.CommandConstructorInterface,
    ) -> None:
        self.interface = interface

    def general_move_command(self):
        return self.interface.general_move_command()

    def create_command(
        self, address: int, command_from_documentation: str, write_value: int = None
    ) -> canalystii.Message:
        return self.interface.create_command(
            command_from_documentation=command_from_documentation,
            write_value=write_value,
            address=address,
        )
