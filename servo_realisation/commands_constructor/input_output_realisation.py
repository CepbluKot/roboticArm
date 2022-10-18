import servo_realisation.commands_constructor.commands_constructor
import servo_realisation.commands_constructor.commands_constructor_abstraction
import servo_realisation.control_objects.servo_interface


def create_servo_command_constructor(
    servo_object: servo_realisation.control_objects.servo_interface.ServoInterface
):
    commands_constructor = servo_realisation.commands_constructor.commands_constructor.CommandConstructor(
        servo_object=servo_object
    )
    commands_constructor_abs = servo_realisation.commands_constructor.commands_constructor_abstraction.CommandConstructorAbstraction(
        commands_constructor
    )
    return commands_constructor_abs
