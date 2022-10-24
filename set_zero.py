from time import sleep
import servo_realisation.control_objects.input_output_realisation
import servo_realisation.commands_abstraction.input_output_realisation
import canalystii


servo_3 = servo_realisation.control_objects.input_output_realisation.create_servo_object(
    servo_id=3
)

# ser_3 = servo_realisation.commands_abstraction.input_output_realisation.create_servo_commands_abstraction_can(servo_object=servo_3)


set_zero_1 = canalystii.Message(
    can_id=0x605,
    remote=False,
    extended=False,
    data_len=6,
    data=(0x2B, 0x0A, 0x26, 0x00, 0x66, 0xEA),
)

set_zero_2 = canalystii.Message(
    can_id=0x605,
    remote=False,
    extended=False,
    data_len=6,
    data=(0x2B, 0x0A, 0x26, 0x00, 0x70, 0xEA),
)

servo_3.send(channel=0, messages=set_zero_1)
sleep(0.5)
servo_3.send(channel=0, messages=set_zero_2)
print('end')