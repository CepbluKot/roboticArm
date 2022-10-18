import servo_realisation.commands_constructor.input_output_realisation
import servo_realisation.commands_reader.input_output_realisation
import servo_realisation.control_objects.input_output_realisation


device_1 = servo_realisation.control_objects.input_output_realisation.create_servo_object(
    servo_id=1
)
device_2 = servo_realisation.control_objects.input_output_realisation.create_servo_object(
    servo_id=2
)


reader = (
    servo_realisation.commands_reader.input_output_realisation.create_servo_commands_reader()
)
constructor = servo_realisation.commands_constructor.input_output_realisation.create_servo_command_constructor(
    servo_object=device_2
)


set_speed = constructor.create_command(
    command_from_documentation="60810020", address=0x600, write_value=20
)
read_sped = constructor.create_command(
    command_from_documentation="60810020", address=0x600
)

device_1.send(channel=0, messages=read_sped)
read = device_1.receive(channel=0)

print("recd", read)
print(reader.read_recieve(recieve=read))
