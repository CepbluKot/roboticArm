import servo_realisation.servo_interface
import servo_realisation.commands_constructor.commands_constructor
import servo_realisation.commands_constructor.commands_constructor_abstraction

class ServoCommander:
    def __init__(self, servo_object: servo_realisation.servo_interface.ServoInterface) -> None:
        commands_constructor = servo_realisation.commands_constructor.commands_constructor.CommandConstructor(servo_object=servo_object)
        self.commands_constructor_abs = servo_realisation.commands_constructor.commands_constructor_abstraction.CommandConstructorAbstraction(commands_constructor)

    def create_command(self, command_from_documentation=None, address=None, write_value=None, is_read=0, is_write=0):
        return self.commands_constructor_abs.create_command(command_from_documentation=command_from_documentation, is_read=is_read, is_write=is_write, address=address, write_value=write_value)
