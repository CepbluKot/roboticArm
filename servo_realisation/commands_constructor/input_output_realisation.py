import servo_realisation.commands_constructor.commands_constructor
import servo_realisation.commands_constructor.commands_constructor_abstraction
import servo_realisation.control_objects.servo_interface
import can


def create_servo_command_constructor(
    servo_object: servo_realisation.control_objects.servo_interface.ServoInterface
):
    commands_constructor = servo_realisation.commands_constructor.commands_constructor.CommandConstructorThread(
        servo_object=servo_object
    )
    commands_constructor_abs = servo_realisation.commands_constructor.commands_constructor_abstraction.CommandConstructorAbstraction(
        commands_constructor
    )
    return commands_constructor_abs


def create_servo_command_constructor_can(
    servo_object: servo_realisation.control_objects.servo_interface.ServoInterfaceCan
):
    commands_constructor = servo_realisation.commands_constructor.commands_constructor.CommandConstructorCan(
        servo_object=servo_object
    )
    commands_constructor_abs = servo_realisation.commands_constructor.commands_constructor_abstraction.CommandConstructorAbstraction(
        commands_constructor
    )
    return commands_constructor_abs
