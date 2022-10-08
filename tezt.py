# from servo_realisation.servo import Servo
import servo_realisation.commands_constructor.commands_constructor
import servo_realisation.commands_constructor.commands_constructor_abstraction

# srv = Servo(device_id=0)
constructr = servo_realisation.commands_constructor.commands_constructor.CommandConstructor(
    # servo_object=srv
)

constructr = servo_realisation.commands_constructor.commands_constructor.CommandConstructor(
    # servo_object=srv
)
constructor_abs = servo_realisation.commands_constructor.commands_constructor_abstraction.CommandConstructorAbstraction(
    interface=constructr
)

print(
    constructor_abs.create_command(
        command_from_documentation="60830020", is_write=True, write_value=99999
    )
)


print(
    constructor_abs.create_command(
        command_from_documentation="60810020", is_read=True, address=0x601
    )
)
