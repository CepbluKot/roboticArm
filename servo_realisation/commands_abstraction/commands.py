import servo_realisation.commands_constructor.input_output_realisation
import servo_realisation.control_objects.servo_interface
import servo_realisation.commands_abstraction.commads_storage
import servo_realisation.commands_reader.input_output_realisation
import servo_realisation.commands_reader.commands_reader_data_structures

# command:
# 1) send
# 2) save_command and servo id 
# 3) recieve and wait for answer id and commands id
# 4) output the data


commands_storage = servo_realisation.commands_abstraction.commads_storage.commands_storage


class ControlServo:
    def __init__(
        self, servo_object: servo_realisation.control_objects.servo_interface.ServoInterface
    ) -> None:
        self.servo = servo_object
        self.servo_commander = servo_realisation.commands_constructor.input_output_realisation.create_servo_command_constructor(
            servo_object=servo_object
        )

        self.command_reader = servo_realisation.commands_reader.input_output_realisation.create_servo_commands_reader()
        
        
        


        # current_mode = self.servo.send(channel=0, messages=check_mode)
        
        # self.current_mode = -1

    # def set_movements_speed(self, speed: int):
    #     set_speed = self.servo_commander.create_command(
    #         command_from_documentation="60810020",
    #         is_write=1,
    #         address=0x601,
    #         write_value=speed,
    #     )

    #     self.servo.send(channel=0, messages=set_speed)

    # def simple_move_to_position(self, position: int):
    #     if self.current_mode != 1:
    #         select_position_mode = self.servo_commander.create_command(
    #             command_from_documentation="60600008",
    #             is_write=1,
    #             address=0x601,
    #             write_value=1,
    #         )

    #         self.servo.send(channel=0, messages=select_position_mode)
    #         self.current_mode = 1

    #     abs_mode = self.servo_commander.create_command(
    #         command_from_documentation="60400010",
    #         is_write=True,
    #         write_value=47,
    #         address=601,
    #     )


    #     move_to_position = self.servo_commander.create_command(
    #         command_from_documentation="607A0020",
    #         is_write=1,
    #         address=0x601,
    #         write_value=position,
    #     )
    #     self.servo.send(channel=0, messages=abs_mode)

    #     self.servo.send(channel=0, messages=move_to_position)

    # def simple_interpolation(self, position: int):
    #     send_to_all = self.servo_commander.create_command(write_value=128)

    #     print(send_to_all)

    def read_speed(self):
        command_id = '60600008'
        command_answer_id = commands_storage[command_id].answer_code + self.servo.servo_id
        command_send_address = commands_storage[command_id].send_address

        read_speed = self.servo_commander.create_command(
            command_from_documentation=command_id, address=command_send_address
        )

        decoded_recieve = servo_realisation.commands_reader.commands_reader_data_structures.RecievedCommand(id=-1, ts="", data="")

        while decoded_recieve.id != command_answer_id:
            self.servo.send(channel=0, messages=read_speed)
            recv = self.servo.receive(channel=0)
            decoded_recieve = self.command_reader.read_recieve(recv)

        return decoded_recieve


    # def read_mode(self, ):
    #     check_mode = self.servo_commander.create_command(
    #         command_from_documentation="60600008", address=0x600
    #     )

    #     self.servo.send(channel=0, messages=check_mode)
        
    #     while not current_mode:

    #         current_mode = 0
    #         current_mode = self.servo.receive




