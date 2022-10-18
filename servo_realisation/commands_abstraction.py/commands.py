import servo_realisation.commands_constructor.input_output_realisation
import time


class ControlServo:
    def __init__(
        self, servo_object: servo_realisation.servo_interface.ServoInterface
    ) -> None:
        self.servo = servo_object
        self.servo_commander = servo_realisation.commands_constructor.input_output_realisation.ServoCommander(
            servo_object=servo_object
        )

        check_mode = self.servo_commander.commands_constructor_abs.create_command(
            command_from_documentation="60600008", is_read=1, address=601
        )
        self.current_mode = -1

    def set_movements_speed(self, speed: int):
        set_speed = self.servo_commander.create_command(
            command_from_documentation="60810020",
            is_write=1,
            address=0x601,
            write_value=speed,
        )
        time.sleep(0.2)
        self.servo.send(channel=0, messages=set_speed)

    def simple_move_to_position(self, position: int):
        if self.current_mode != 1:
            select_position_mode = self.servo_commander.create_command(
                command_from_documentation="60600008",
                is_write=1,
                address=0x601,
                write_value=1,
            )
            time.sleep(0.2)
            self.servo.send(channel=0, messages=select_position_mode)
            self.current_mode = 1

        abs_mode = self.servo_commander.create_command(
            command_from_documentation="60400010",
            is_write=True,
            write_value=47,
            address=601,
        )

        time.sleep(0.2)
        move_to_position = self.servo_commander.create_command(
            command_from_documentation="607A0020",
            is_write=1,
            address=0x601,
            write_value=position,
        )
        self.servo.send(channel=0, messages=abs_mode)
        time.sleep(0.2)
        self.servo.send(channel=0, messages=move_to_position)

    def simple_interpolation(self, position: int):
        send_to_all = self.servo_commander.create_command(write_value=128)

        print(send_to_all)
