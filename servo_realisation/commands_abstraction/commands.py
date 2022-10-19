import canalystii

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
        self.current_mode = self.read_mode()

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
        command_id = '60810020'
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

    def set_speed(self, value: int):
        command_id = '60810020'
        # command_answer_id = commands_storage[command_id].answer_code + self.servo.servo_id
        command_send_address = commands_storage[command_id].send_address

        set_speed = self.servo_commander.create_command(
            command_from_documentation=command_id, address=command_send_address, write_value=value
        )

        # decoded_recieve = servo_realisation.commands_reader.commands_reader_data_structures.RecievedCommand(id=-1, ts="", data="")

        # while decoded_recieve.id != command_answer_id:
        print('SET_SPEED=', value, 'SERVO', self.servo.servo_id)
        self.servo.send(channel=0, messages=set_speed)
        # recv = self.servo.receive(channel=0)
        # decoded_recieve = self.command_reader.read_recieve(recv)

        # return decoded_recieve

    def read_pos(self):
        command_id = '60640020'
        command_answer_id = commands_storage[command_id].answer_code + self.servo.servo_id
        command_send_address = commands_storage[command_id].send_address

        read_pos = self.servo_commander.create_command(
            command_from_documentation=command_id, address=command_send_address
        )

        decoded_recieve = servo_realisation.commands_reader.commands_reader_data_structures.RecievedCommand(id=-1, ts="", data="")

        while decoded_recieve.id != command_answer_id:
            self.servo.send(channel=0, messages=read_pos)
            recv = self.servo.receive(channel=0)
            decoded_recieve = self.command_reader.read_recieve(recv)

        return decoded_recieve

    def set_pos(self, value: int):        
        # command_answer_id = 480 + self.servo.servo_id
        command_send_address = 0x500 + self.servo.servo_id

        write_value = self.servo_commander.only_convert_write_value_to_hex(write_value=value, num_of_bytes_for_command=4)
        set_pos = canalystii.Message(
                can_id=command_send_address,
                remote=False,
                extended=False,
                data_len=len(write_value),
                data=write_value,
            )

        # decoded_recieve = servo_realisation.commands_reader.commands_reader_data_structures.RecievedCommand(id=-1, ts="", data="")

        # while decoded_recieve.id != command_answer_id:
        print('SET_POS=', value, 'SERVO', self.servo.servo_id)
        self.servo.send(channel=0, messages=set_pos)
        # recv = self.servo.receive(channel=0)
        
        # decoded_recieve = self.command_reader.read_recieve(recv)

        # return decoded_recieve


    def read_mode(self):
        command_id = '60600008'
        command_answer_id = commands_storage[command_id].answer_code + self.servo.servo_id
        command_send_address = commands_storage[command_id].send_address

        read_mode = self.servo_commander.create_command(
            command_from_documentation=command_id, address=command_send_address
        )

        decoded_recieve = servo_realisation.commands_reader.commands_reader_data_structures.RecievedCommand(id=-1, ts="", data="")

        while decoded_recieve.id != command_answer_id:
            self.servo.send(channel=0, messages=read_mode)
            recv = self.servo.receive(channel=0)
            decoded_recieve = self.command_reader.read_recieve(recv)

        return decoded_recieve


    def set_mode(self, value: int):
        command_id = '60640020'
        # command_answer_id = commands_storage[command_id].answer_code + self.servo.servo_id
        command_send_address = commands_storage[command_id].send_address

        set_mode = self.servo_commander.create_command(
            command_from_documentation=command_id, address=command_send_address, write_value=value
        )

        # decoded_recieve = servo_realisation.commands_reader.commands_reader_data_structures.RecievedCommand(id=-1, ts="", data="")

        # while decoded_recieve.id != command_answer_id:
        self.servo.send(channel=0, messages=set_mode)
            # recv = self.servo.receive(channel=0)
            # decoded_recieve = self.command_reader.read_recieve(recv)

        self.current_mode = value

        # return decoded_recieve

    def set_zero_pos(self):
        address = 0x600 + self.servo.servo_id
        # print(600+self.servo.servo_id)
        command_answer_id = 580 + self.servo.servo_id
        set_zero_part_1 = canalystii.Message(
            can_id=address,
            remote=False,
            extended=False,
            data_len=6,
            data=(0x2B, 0x0A, 0x26, 0x00, 0x66, 0xEA),
                )

        set_zero_part_2 = canalystii.Message(
            can_id=address,
            remote=False,
            extended=False,
            data_len=6,
            data=(0x2B, 0x0A, 0x26, 0x00, 0x70, 0xEA),
            )

        # decoded_recieve = servo_realisation.commands_reader.commands_reader_data_structures.RecievedCommand(id=-1, ts="", data="")

        # while decoded_recieve.id != command_answer_id:
        self.servo.send(channel=0, messages=set_zero_part_1)
        self.servo.send(channel=0, messages=set_zero_part_2)

        #     recv = self.servo.receive(channel=0)
        #     print(recv)
        #     decoded_recieve = self.command_reader.read_recieve(recv)

        # return decoded_recieve

    def general_move_command(self):
        move_command = canalystii.Message(
            remote=False, extended=False, data_len=0, can_id=0x80
        )
        print('GENERAL MOVE FROM SERVO', self.servo.servo_id)
        self.servo.send(channel=0, messages=move_command)


    def save_settings(self):
        command_id = '26140010'
        command_answer_id = commands_storage[command_id].answer_code + self.servo.servo_id
        command_send_address = commands_storage[command_id].send_address

        save_settings = self.servo_commander.create_command(
            command_from_documentation=command_id, address=command_send_address, write_value=1
        )

        decoded_recieve = servo_realisation.commands_reader.commands_reader_data_structures.RecievedCommand(id=-1, ts="", data="")

        while decoded_recieve.id != command_answer_id:
            self.servo.send(channel=0, messages=save_settings)
            recv = self.servo.receive(channel=0)
            decoded_recieve = self.command_reader.read_recieve(recv)

        return decoded_recieve
