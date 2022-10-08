from servo_realisation.servo import Servo
import servo_realisation.commands_constructor.commands_constructor
import servo_realisation.commands_constructor.commands_constructor_abstraction

srv = Servo(device_id=0)
constructr = (
    servo_realisation.commands_constructor.commands_constructor.CommandConstructor(
        servo_object=srv
    )
)

constructr = (
    servo_realisation.commands_constructor.commands_constructor.CommandConstructor(
        servo_object=srv
    )
)
constructor_abs = servo_realisation.commands_constructor.commands_constructor_abstraction.CommandConstructorAbstraction(
    interface=constructr
)

print(
    constructor_abs.create_command(
        command_from_documentation="260A0010", is_write=1, write_value=60016
    )
)
