import time
import typing
import canalystii
import can

import servo_realisation.commands_constructor.input_output_realisation
import servo_realisation.control_objects.servo_interface
import servo_realisation.commands_abstraction.commads_storage
import servo_realisation.commands_reader.input_output_realisation
import servo_realisation.commands_reader.commands_reader_data_structures

import servo_realisation.commands_abstraction.commads_storage

# command:
# 1) send
# 2) save_command and servo id
# 3) recieve and wait for answer id and commands id
# 4) output the data


# commands_info_storage = servo_realisation.commands_abstraction.commads_storage.general_commands_info_storage
servo_info_storage = (
    servo_realisation.commands_abstraction.commads_storage.servo_info_storage
)

"""
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
        self.current_speed = self.read_speed()
        self.current_pos = self.read_pos()

        # проверка на наличие ключа в словаре
        # if self.servo.servo_id not in servo_info_storage:
        #     servo_info_storage[self.servo.servo_id] = servo_realisation.commands_abstraction.commads_storage.ServoData(speed=self.read_speed(), pos=self.read_pos(), mode=self.read_mode())
        # servo_info_storage[self.servo.servo_id] = servo_realisation.commands_abstraction.commads_storage.ServoData(
        #     speed_value=0, pos_value=0, mode_value=0, servo_object=servo_object)

    def read_speed(self):
        command_id = '60810020'
        command_answer_id = commands_info_storage[command_id].answer_code + self.servo.servo_id
        command_send_address = commands_info_storage[command_id].send_address

        read_speed = self.servo_commander.create_command(
            command_from_documentation=command_id, address=command_send_address
        )

        self.servo.send(channel=0, messages=read_speed)


        target_elem = 0

        while not target_elem:
            for elem in self.servo.receive(0):
                parsed_rec = self.command_reader.read_recieve(elem)
                if parsed_rec.id == command_answer_id:
                    target_elem = parsed_rec


        return target_elem


    def set_speed(self, value: int):
        # if value != servo_info_storage[self.servo.servo_id].speed:

            command_id = '60810020'
            # command_answer_id = commands_info_storage[command_id].answer_code + self.servo.servo_id
            command_send_address = commands_info_storage[command_id].send_address

            set_speed = self.servo_commander.create_command(
                command_from_documentation=command_id, address=command_send_address, write_value=value
            )

            # decoded_recieve = servo_realisation.commands_reader.commands_reader_data_structures.RecievedCommand(id=-1, ts="", data="")

            # while decoded_recieve.id != command_answer_id:
            # # print('SET_SPEED=', value, 'SERVO', self.servo.servo_id)
            self.servo.send(channel=0, messages=set_speed)
            # servo_info_storage[self.servo.servo_id].speed = set_speed
            # recv = self.servo.receive(channel=0)
            # decoded_recieve = self.command_reader.read_recieve(recv)
            # return decoded_recieve

    def read_pos(self):
        command_id = '60640020'
        command_answer_id = commands_info_storage[command_id].answer_code + self.servo.servo_id
        command_send_address = commands_info_storage[command_id].send_address

        read_pos = self.servo_commander.create_command(
            command_from_documentation=command_id, address=command_send_address
        )

        self.servo.send(channel=0, messages=read_pos)

        target_elem = 0
        while not target_elem:
            for elem in self.servo.receive(0):
                parsed_rec = self.command_reader.read_recieve(elem)
                if parsed_rec.id == command_answer_id:
                    target_elem = parsed_rec


        return target_elem

    def set_pos(self, value: int):
        if servo_info_storage[self.servo.servo_id].pos != value:

            # command_answer_id = 480 + self.servo.servo_id
            command_send_address = 0x500 + self.servo.servo_id

            write_value = self.servo_commander.only_convert_write_value_to_hex(
                write_value=value, num_of_bytes_for_command=4)
            set_pos = canalystii.Message(
                can_id=command_send_address,
                remote=False,
                extended=False,
                data_len=len(write_value),
                data=write_value,
            )

            # decoded_recieve = servo_realisation.commands_reader.commands_reader_data_structures.RecievedCommand(id=-1, ts="", data="")

            # while decoded_recieve.id != command_answer_id:
            # # print('SET_POS=', value, 'SERVO', self.servo.servo_id)
            self.servo.send(channel=0, messages=set_pos)
            # servo_info_storage[self.servo.servo_id].pos = value
            # recv = self.servo.receive(channel=0)

            # decoded_recieve = self.command_reader.read_recieve(recv)

            # return decoded_recieve

    def read_mode(self):
        command_id = '60600008'
        command_answer_id = commands_info_storage[command_id].answer_code + self.servo.servo_id
        command_send_address = commands_info_storage[command_id].send_address


        read_mode = self.servo_commander.create_command(
            command_from_documentation=command_id, address=command_send_address
        )

        self.servo.send(channel=0, messages=read_mode)

        target_elem = 0
        while not target_elem:
            for elem in self.servo.receive(0):
                parsed_rec = self.command_reader.read_recieve(elem)
                if parsed_rec.id == command_answer_id:
                    target_elem = parsed_rec


        return target_elem

    def set_mode(self, value: int):
        if servo_info_storage[self.servo.servo_id].mode != value:
            command_id = '60640020'
            # command_answer_id = commands_storage[command_id].answer_code + self.servo.servo_id
            command_send_address = commands_info_storage[command_id].send_address

            set_mode = self.servo_commander.create_command(
                command_from_documentation=command_id, address=command_send_address, write_value=value
            )

            # decoded_recieve = servo_realisation.commands_reader.commands_reader_data_structures.RecievedCommand(id=-1, ts="", data="")

            # while decoded_recieve.id != command_answer_id:
            self.servo.send(channel=0, messages=set_mode)
            # recv = self.servo.receive(channel=0)
            # decoded_recieve = self.command_reader.read_recieve(recv)
            servo_info_storage[self.servo.servo_id].mode = value

            # return decoded_recieve

    def set_zero_pos(self):
        address = 0x600 + self.servo.servo_id
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

        self.servo.send(channel=0, messages=[set_zero_part_1, set_zero_part_2])


    def general_move_command(self):
        move_command = canalystii.Message(
            remote=False, extended=False, data_len=0, can_id=0x80
        )
        # print('GENERAL MOVE FROM SERVO', self.servo.servo_id)
        self.servo.send(channel=0, messages=move_command)

    def save_settings(self):
        command_id = '26140010'
        command_answer_id = commands_info_storage[command_id].answer_code + \
            self.servo.servo_id
        command_send_address = commands_info_storage[command_id].send_address

        save_settings = self.servo_commander.create_command(
            command_from_documentation=command_id, address=command_send_address, write_value=1
        )

        decoded_recieve = servo_realisation.commands_reader.commands_reader_data_structures.RecievedCommand(
            id=-1, ts="", data="")

        while decoded_recieve.id != command_answer_id:
            self.servo.send(channel=0, messages=save_settings)
            recv = self.servo.receive(channel=0)
            decoded_recieve = self.command_reader.read_recieve(recv)

        return decoded_recieve

    def decode_everyth(self, recv: typing.List[canalystii.Message]):

        decoded_recieve = servo_realisation.commands_reader.commands_reader_data_structures.RecievedCommand(
            id=-1, ts="", data="")

        res: typing.List[servo_realisation.commands_reader.commands_reader_data_structures.RecievedCommand] = []

        for elem in recv:
            decoded_recieve = self.command_reader.read_recieve(elem)
            res.append(decoded_recieve)
        return res
"""


class ControlServoThread:
    def __init__(
        self,
        servo_object: servo_realisation.control_objects.servo_interface.ServoInterface,
        servo_info_storage: typing.Dict[
            int, servo_realisation.commands_abstraction.commads_storage.ServoData
        ],
    ) -> None:
        self.servo = servo_object
        self.servo_commander = servo_realisation.commands_constructor.input_output_realisation.create_servo_command_constructor(
            servo_object=servo_object
        )

        # self.command_reader = servo_realisation.commands_reader.input_output_realisation.create_servo_commands_reader()
        servo_info_storage[
            self.servo.servo_id
        ] = servo_realisation.commands_abstraction.commads_storage.ServoData(
            servo_id=servo_object.servo_id
        )

        self.current_servo_data = servo_info_storage[self.servo.servo_id]

    def read_speed(self):
        command_id = "60810020"

        command_data_in_servo_data = self.current_servo_data.commands_info_storage[
            command_id[:4]
        ]

        command_send_address = command_data_in_servo_data.send_address

        read_speed_command = self.servo_commander.create_command(
            command_from_documentation=command_id, address=command_send_address
        )

        self.current_servo_data.set_speed_flag(0)

        self.servo.send(channel=0, messages=read_speed_command)

        # print('wait sped red start')
        while not self.current_servo_data.read_speed_flag():
            self.servo.send(channel=0, messages=read_speed_command)

        # print('wait sped red end')

        return self.current_servo_data.read_speed()

    def set_speed(self, value: int):
        # if value != self.current_servo_data.read_speed():
        command_id = "60810020"
        command_data_in_servo_data = self.current_servo_data.commands_info_storage[
            command_id[:4]
        ]

        command_send_address = command_data_in_servo_data.send_address

        set_speed_command = self.servo_commander.create_command(
            command_from_documentation=command_id,
            address=command_send_address,
            write_value=value,
        )

        self.current_servo_data.set_speed_flag(0)
        self.servo.send(channel=0, messages=set_speed_command)
        self.read_speed()

        while (
            not command_data_in_servo_data.read_flag()
            and command_data_in_servo_data.read_value() != value
        ):
            self.current_servo_data.set_speed_flag(0)
            self.servo.send(channel=0, messages=set_speed_command)
            self.read_speed()

    def read_pos(self):
        command_id = "60640020"

        command_data_in_servo_data = self.current_servo_data.commands_info_storage[
            command_id[:4]
        ]

        command_send_address = command_data_in_servo_data.send_address

        read_pos_command = self.servo_commander.create_command(
            command_from_documentation=command_id, address=command_send_address
        )
        self.current_servo_data.set_current_pos_flag(0)
        self.servo.send(channel=0, messages=read_pos_command)

        # print('wait pos red start')
        while not self.current_servo_data.read_current_pos_flag():
            self.servo.send(channel=0, messages=read_pos_command)

        # print('wait pos red end')
        return self.current_servo_data.read_current_pos()

    def set_pos(self, value: int):
        command_send_address = 0x500 + self.servo.servo_id
        command_data_in_servo_data = self.current_servo_data.commands_info_storage[
            "interpolation"
        ]

        write_value = self.servo_commander.only_convert_write_value_to_hex(
            write_value=value, num_of_bytes_for_command=4
        )

        set_pos_command = canalystii.Message(
            can_id=command_send_address,
            remote=False,
            extended=False,
            data_len=len(write_value),
            data=write_value,
        )

        command_data_in_servo_data.set_flag(0)
        self.servo.send(channel=0, messages=set_pos_command)
        while (
            not command_data_in_servo_data.read_flag()
            and command_data_in_servo_data.read_value() != value
        ):
            command_data_in_servo_data.set_flag(0)
            self.servo.send(channel=0, messages=set_pos_command)

        # print('send pos done', self.servo.servo_id)

    def read_mode(self):
        command_id = "60600008"

        command_data_in_servo_data = self.current_servo_data.commands_info_storage[
            command_id[:4]
        ]

        command_send_address = command_data_in_servo_data.send_address

        read_mode_command = self.servo_commander.create_command(
            command_from_documentation=command_id, address=command_send_address
        )
        self.current_servo_data.set_mode_flag(0)
        self.servo.send(channel=0, messages=read_mode_command)

        # print('wait mod red start')
        while not self.current_servo_data.read_mode_flag():
            self.servo.send(channel=0, messages=read_mode_command)

        # print('wait mod red end')
        return self.current_servo_data.read_mode()

    def set_mode(self, value: int):
        # if self.current_servo_data.read_mode() != value:
        command_id = "60640020"
        # command_answer_id = commands_storage[command_id].answer_code + self.servo.servo_id
        command_send_address = self.current_servo_data.commands_info_storage[
            command_id[:4]
        ].send_address
        set_mode_command = self.servo_commander.create_command(
            command_from_documentation=command_id,
            address=command_send_address,
            write_value=value,
        )

        self.current_servo_data.set_mode_flag(0)
        self.servo.send(channel=0, messages=set_mode_command)
        self.read_mode()

        # print('mode set done')

    # # print('mode set - same val')

    def set_zero_pos(self):
        address = 0x600 + self.servo.servo_id
        # # print(600+self.servo.servo_id)
        # command_answer_id = 580 + self.servo.servo_id
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
        self.servo.send(channel=0, messages=[set_zero_part_1, set_zero_part_2])
        # self.read_pos()
        # self.servo.send(channel=0, messages=set_zero_part_2)

        #     recv = self.servo.receive(channel=0)
        #     # print(recv)
        #     decoded_recieve = self.command_reader.read_recieve(recv)

        # return decoded_recieve

    def general_move_command(self):
        move_command = canalystii.Message(
            remote=False, extended=False, data_len=0, can_id=0x80
        )
        # print('GENERAL MOVE FROM SERVO', self.servo.servo_id)
        self.servo.send(channel=0, messages=move_command)

    def save_settings(self):
        # command_id = '26140010'
        pass
        # command_answer_id = commands_info_storage[command_id].answer_code + \
        #     self.servo.servo_id
        # command_send_address = commands_info_storage[command_id].send_address

        # save_settings = self.servo_commander.create_command(
        #     command_from_documentation=command_id, address=command_send_address, write_value=1
        # )

        # decoded_recieve = servo_realisation.commands_reader.commands_reader_data_structures.RecievedCommand(
        #     id=-1, ts="", data="")

        # while decoded_recieve.id != command_answer_id:
        #     self.servo.send(channel=0, messages=save_settings)
        #     recv = self.servo.receive(channel=0)
        #     decoded_recieve = self.command_reader.read_recieve(recv)

        # return decoded_recieve

    def decode_everyth(self, recv: typing.List[canalystii.Message]):
        pass
        # decoded_recieve = servo_realisation.commands_reader.commands_reader_data_structures.RecievedCommand(
        #     id=-1, ts="", data="")

        # res: typing.List[servo_realisation.commands_reader.commands_reader_data_structures.RecievedCommand] = []

        # for elem in recv:
        #     decoded_recieve = self.command_reader.read_recieve(elem)
        #     res.append(decoded_recieve)
        # return res

    def send_general_move_command(self):
        final_command = canalystii.Message(
            remote=False, extended=False, data_len=0, can_id=0x80
        )
        self.servo.send(channel=0, message=final_command)

    def set_acceleration(self, value):
        command_id = "60830020"
        command_data_in_servo_data = self.current_servo_data.commands_info_storage[
            command_id[:4]
        ]

        command_send_address = command_data_in_servo_data.send_address

        set_speed_command = self.servo_commander.create_command(
            command_from_documentation=command_id,
            address=command_send_address,
            write_value=value,
        )

        self.current_servo_data.set_acceleration_flag(0)
        self.servo.send(channel=0, messages=set_speed_command)
        self.read_acceleration()
        while (
            not self.current_servo_data.read_acceleration_flag()
            and self.current_servo_data.read_acceleration() != value
        ):
            self.current_servo_data.set_acceleration_flag(0)
            self.servo.send(channel=0, messages=set_speed_command)
            self.read_acceleration()

    def read_acceleration(self):
        command_id = "60830020"
        command_data_in_servo_data = self.current_servo_data.commands_info_storage[
            command_id[:4]
        ]
        command_send_address = command_data_in_servo_data.send_address

        read_pos_command = self.servo_commander.create_command(
            command_from_documentation=command_id, address=command_send_address
        )
        self.current_servo_data.set_acceleration_flag(0)
        self.servo.send(channel=0, messages=read_pos_command)

        # print('wait accel  start')
        while not self.current_servo_data.read_acceleration_flag():
            self.servo.send(channel=0, messages=read_pos_command)

        # print('wait accel  end')
        return self.current_servo_data.read_acceleration()

    def print_servo_data(self):
        return self.current_servo_data.print_servo_data()


"""

class ControlServoCan:
    def __init__(
        self, servo_object: servo_realisation.control_objects.servo_interface.ServoInterfaceCan
    ) -> None:

        self.servo = servo_object
        self.servo_commander = servo_realisation.commands_constructor.input_output_realisation.create_servo_command_constructor_can(
            servo_object=servo_object
        )

        self.command_reader = servo_realisation.commands_reader.input_output_realisation.create_servo_commands_reader_can()

        # проверка на наличие ключа в словаре
        if self.servo.servo_id not in servo_info_storage:
            servo_info_storage[self.servo.servo_id] = servo_realisation.commands_abstraction.commads_storage.ServoData(
                speed_value=-1, pos_value=-1, mode_value=-1)

        self.current_mode = self.read_mode()
        self.current_speed = self.read_speed()
        self.current_pos = self.read_pos()

        servo_info_storage[self.servo.servo_id] = servo_realisation.commands_abstraction.commads_storage.ServoData(
            speed_value=self.current_speed, pos_value=self.current_pos, mode_value=self.current_mode)

    def read_speed(self):
        command_id = '60810020'
        command_answer_id = commands_info_storage[command_id].answer_code + \
            self.servo.servo_id
        command_send_address = commands_info_storage[command_id].send_address

        read_speed = self.servo_commander.create_command(
            command_from_documentation=command_id, address=command_send_address
        )

        decoded_recieve = servo_realisation.commands_reader.commands_reader_data_structures.RecievedCommand(
            id=-1, ts="", data="")

        while decoded_recieve.id != command_answer_id:
            self.servo.send(message=read_speed)
            recv = self.servo.receive()
            decoded_recieve = self.command_reader.read_recieve(recv)

        servo_info_storage[self.servo.servo_id].speed = decoded_recieve.decoded_data

        return decoded_recieve

    def set_speed(self, value: int):
        if value != servo_info_storage[self.servo.servo_id].speed:

            command_id = '60810020'
            command_answer_id = commands_info_storage[command_id].answer_code + \
                self.servo.servo_id
            command_send_address = commands_info_storage[command_id].send_address

            set_speed = self.servo_commander.create_command(
                command_from_documentation=command_id, address=command_send_address, write_value=value
            )

            decoded_recieve = servo_realisation.commands_reader.commands_reader_data_structures.RecievedCommand(
                id=-1, ts="", data="")

            while decoded_recieve.id != command_answer_id:
                # print('SET_SPEED=', value, 'SERVO', self.servo.servo_id)
                self.servo.send(message=set_speed)
                recv = self.servo.receive()
                decoded_recieve = self.command_reader.read_recieve(recv)

            servo_info_storage[self.servo.servo_id].speed = value

            return decoded_recieve

    def read_pos(self):
        command_id = '60640020'
        command_answer_id = commands_info_storage[command_id].answer_code + \
            self.servo.servo_id
        command_send_address = commands_info_storage[command_id].send_address

        read_pos = self.servo_commander.create_command(
            command_from_documentation=command_id, address=command_send_address
        )

        decoded_recieve = servo_realisation.commands_reader.commands_reader_data_structures.RecievedCommand(
            id=-1, ts="", data="")

        while decoded_recieve.id != command_answer_id:
            self.servo.send(message=read_pos)
            recv = self.servo.receive()
            decoded_recieve = self.command_reader.read_recieve(recv)

        servo_info_storage[self.servo.servo_id].pos = decoded_recieve.decoded_data

        return decoded_recieve

    def set_pos(self, value: int):
        if servo_info_storage[self.servo.servo_id].pos != value:

            command_answer_id = 0x480 + self.servo.servo_id
            command_send_address = 0x500 + self.servo.servo_id

            write_value = self.servo_commander.only_convert_write_value_to_hex(
                write_value=value, num_of_bytes_for_command=4)
            set_pos = can.Message(
                arbitration_id=command_send_address,
                is_extended_id=False,
                data=write_value,
            )

            decoded_recieve = servo_realisation.commands_reader.commands_reader_data_structures.RecievedCommand(
                id=-1, ts="", data="")

            while decoded_recieve.id != command_answer_id:
                # print('SET_POS=', value, 'SERVO', self.servo.servo_id)
                self.servo.send(message=set_pos)
                recv = self.servo.receive()
                decoded_recieve = self.command_reader.read_recieve(recv)

            servo_info_storage[self.servo.servo_id].pos = value

            return decoded_recieve

    def read_mode(self):
        command_id = '60600008'
        command_answer_id = commands_info_storage[command_id].answer_code + \
            self.servo.servo_id
        command_send_address = commands_info_storage[command_id].send_address

        read_mode = self.servo_commander.create_command(
            command_from_documentation=command_id, address=command_send_address
        )

        decoded_recieve = servo_realisation.commands_reader.commands_reader_data_structures.RecievedCommand(
            id=-1, ts="", data="")

        while decoded_recieve.id != command_answer_id:
            self.servo.send(message=read_mode)
            recv = self.servo.receive()
            decoded_recieve = self.command_reader.read_recieve(recv)

        servo_info_storage[self.servo.servo_id].mode = decoded_recieve.decoded_data

        return decoded_recieve

    def set_mode(self, value: int):
        if servo_info_storage[self.servo.servo_id].mode != value:
            command_id = '60640020'
            command_answer_id = commands_info_storage[command_id].answer_code + \
                self.servo.servo_id
            command_send_address = commands_info_storage[command_id].send_address

            set_mode = self.servo_commander.create_command(
                command_from_documentation=command_id, address=command_send_address, write_value=value
            )

            decoded_recieve = servo_realisation.commands_reader.commands_reader_data_structures.RecievedCommand(
                id=-1, ts="", data="")

            while decoded_recieve.id != command_answer_id:
                self.servo.send(message=set_mode)
                recv = self.servo.receive()
                decoded_recieve = self.command_reader.read_recieve(recv)

            servo_info_storage[self.servo.servo_id].mode = value

            # return decoded_recieve

    def set_zero_pos(self):
        address = 0x600 + self.servo.servo_id
        # # print(600+self.servo.servo_id)
        # command_answer_id = 580 + self.servo.servo_id
        set_zero_part_1 = can.Message(
            arbitration_id=address,
            is_extended_id=False,
            data=[0x2B, 0x0A, 0x26, 0x00, 0x66, 0xEA],
        )

        set_zero_part_2 = can.Message(
            arbitration_id=address,
            is_extended_id=False,
            data=[0x2B, 0x0A, 0x26, 0x00, 0x70, 0xEA],
        )
        # decoded_recieve = servo_realisation.commands_reader.commands_reader_data_structures.RecievedCommand(id=-1, ts="", data="")

        # while decoded_recieve.id != command_answer_id:
        self.servo.send(message=set_zero_part_1)
        time.sleep(0.1)
        self.servo.send(message=set_zero_part_2)

        # self.servo.send( messages=set_zero_part_2)

        #     recv = self.servo.receive()
        #     # print(recv)
        #     decoded_recieve = self.command_reader.read_recieve(recv)

        # return decoded_recieve

    def general_move_command(self):
        move_command = can.Message(
            is_extended_id=False, arbitration_id=0x80
        )
        # print('GENERAL MOVE FROM SERVO', self.servo.servo_id)
        self.servo.send(message=move_command)

    def save_settings(self):
        command_id = '26140010'
        command_answer_id = commands_info_storage[command_id].answer_code + \
            self.servo.servo_id
        command_send_address = commands_info_storage[command_id].send_address

        save_settings = self.servo_commander.create_command(
            command_from_documentation=command_id, address=command_send_address, write_value=1
        )

        decoded_recieve = servo_realisation.commands_reader.commands_reader_data_structures.RecievedCommand(
            id=-1, ts="", data="")

        while decoded_recieve.id != command_answer_id:
            self.servo.send(message=save_settings)
            recv = self.servo.receive()
            decoded_recieve = self.command_reader.read_recieve(recv)

        # return decoded_recieve


class ControlServoCan_test:
    def __init__(
        self, servo_object: servo_realisation.control_objects.servo_interface.ServoInterfaceCan
    ) -> None:

        self.servo = servo_object
        self.servo_commander = servo_realisation.commands_constructor.input_output_realisation.create_servo_command_constructor_can(
            servo_object=servo_object
        )

        self.command_reader = servo_realisation.commands_reader.input_output_realisation.create_servo_commands_reader_can()

        # проверка на наличие ключа в словаре
        if self.servo.servo_id not in servo_info_storage:
            servo_info_storage[self.servo.servo_id] = servo_realisation.commands_abstraction.commads_storage.ServoData(
                speed_value=-1, pos_value=-1, mode_value=-1)

        self.current_mode = self.read_mode()
        self.current_speed = self.read_speed()
        self.current_pos = self.read_pos()

        servo_info_storage[self.servo.servo_id] = servo_realisation.commands_abstraction.commads_storage.ServoData(
            speed_value=self.current_speed, pos_value=self.current_pos, mode_value=self.current_mode)

    def read_speed(self):
        command_id = '60810020'
        command_answer_id = commands_info_storage[command_id].answer_code + \
            self.servo.servo_id
        command_send_address = commands_info_storage[command_id].send_address

        read_speed = self.servo_commander.create_command(
            command_from_documentation=command_id, address=command_send_address
        )

        decoded_recieve = servo_realisation.commands_reader.commands_reader_data_structures.RecievedCommand(
            id=-1, ts="", data="")

        self.servo.send(message=read_speed)
        recv: can.Message = self.servo.receive()
        while recv.arbitration_id != command_answer_id:
            self.servo.send(message=read_speed)
            recv = self.servo.receive()
        decoded_recieve = self.command_reader.read_recieve(recv)

        servo_info_storage[self.servo.servo_id].speed = decoded_recieve.decoded_data

        return decoded_recieve

    def set_speed(self, value: int):
        if value != servo_info_storage[self.servo.servo_id].speed:

            command_id = '60810020'
            command_answer_id = commands_info_storage[command_id].answer_code + \
                self.servo.servo_id
            command_send_address = commands_info_storage[command_id].send_address

            set_speed = self.servo_commander.create_command(
                command_from_documentation=command_id, address=command_send_address, write_value=value
            )

            decoded_recieve = servo_realisation.commands_reader.commands_reader_data_structures.RecievedCommand(
                id=-1, ts="", data="")

            self.servo.send(message=set_speed)
            recv: can.Message = self.servo.receive()
            while recv.arbitration_id != command_answer_id:
                # print('SET_SPEED=', value, 'SERVO', self.servo.servo_id)
                self.servo.send(message=set_speed)
                recv = self.servo.receive()
            decoded_recieve = self.command_reader.read_recieve(recv)

            servo_info_storage[self.servo.servo_id].speed = value

            return decoded_recieve

    def read_pos(self):
        command_id = '60640020'
        command_answer_id = commands_info_storage[command_id].answer_code + \
            self.servo.servo_id
        command_send_address = commands_info_storage[command_id].send_address

        read_pos = self.servo_commander.create_command(
            command_from_documentation=command_id, address=command_send_address
        )

        decoded_recieve = servo_realisation.commands_reader.commands_reader_data_structures.RecievedCommand(
            id=-1, ts="", data="")

        self.servo.send(message=read_pos)
        recv: can.Message = self.servo.receive()
        while recv.arbitration_id != command_answer_id:
            self.servo.send(message=read_pos)
            recv = self.servo.receive()
        decoded_recieve = self.command_reader.read_recieve(recv)

        servo_info_storage[self.servo.servo_id].pos = decoded_recieve.decoded_data

        return decoded_recieve

    def set_pos(self, value: int):
        if servo_info_storage[self.servo.servo_id].pos != value:

            command_answer_id = 0x480 + self.servo.servo_id
            command_send_address = 0x500 + self.servo.servo_id

            write_value = self.servo_commander.only_convert_write_value_to_hex(
                write_value=value, num_of_bytes_for_command=4)
            set_pos = can.Message(
                arbitration_id=command_send_address,
                is_extended_id=False,
                data=write_value,
            )

            decoded_recieve = servo_realisation.commands_reader.commands_reader_data_structures.RecievedCommand(
                id=-1, ts="", data="")

            self.servo.send(message=set_pos)
            recv: can.Message = self.servo.receive()

            while recv.arbitration_id != command_answer_id:
                # print('SET_POS=', value, 'SERVO', self.servo.servo_id)
                self.servo.send(message=set_pos)
                recv = self.servo.receive()
            decoded_recieve = self.command_reader.read_recieve(recv)

            servo_info_storage[self.servo.servo_id].pos = value

            return decoded_recieve

    def read_mode(self):
        command_id = '60600008'
        command_answer_id = commands_info_storage[command_id].answer_code + \
            self.servo.servo_id
        command_send_address = commands_info_storage[command_id].send_address

        read_mode = self.servo_commander.create_command(
            command_from_documentation=command_id, address=command_send_address
        )

        decoded_recieve = servo_realisation.commands_reader.commands_reader_data_structures.RecievedCommand(
            id=-1, ts="", data="")

        self.servo.send(message=read_mode)
        recv: can.Message = self.servo.receive()

        while recv.arbitration_id != command_answer_id:
            self.servo.send(message=read_mode)
            recv = self.servo.receive()
        decoded_recieve = self.command_reader.read_recieve(recv)

        servo_info_storage[self.servo.servo_id].mode = decoded_recieve.decoded_data

        return decoded_recieve

    def set_mode(self, value: int):
        if servo_info_storage[self.servo.servo_id].mode != value:
            command_id = '60640020'
            command_answer_id = commands_info_storage[command_id].answer_code + \
                self.servo.servo_id
            command_send_address = commands_info_storage[command_id].send_address

            set_mode = self.servo_commander.create_command(
                command_from_documentation=command_id, address=command_send_address, write_value=value
            )

            decoded_recieve = servo_realisation.commands_reader.commands_reader_data_structures.RecievedCommand(
                id=-1, ts="", data="")

            self.servo.send(message=set_mode)
            recv: can.Message = self.servo.receive()

            while recv.arbitration_id != command_answer_id:
                self.servo.send(message=set_mode)
                recv = self.servo.receive()
            decoded_recieve = self.command_reader.read_recieve(recv)

            servo_info_storage[self.servo.servo_id].mode = value

            # return decoded_recieve

    def set_zero_pos(self):
        address = 0x600 + self.servo.servo_id
        # # print(600+self.servo.servo_id)
        # command_answer_id = 580 + self.servo.servo_id
        set_zero_part_1 = can.Message(
            arbitration_id=address,
            is_extended_id=False,
            data=[0x2B, 0x0A, 0x26, 0x00, 0x66, 0xEA],
        )

        set_zero_part_2 = can.Message(
            arbitration_id=address,
            is_extended_id=False,
            data=[0x2B, 0x0A, 0x26, 0x00, 0x70, 0xEA],
        )
        # decoded_recieve = servo_realisation.commands_reader.commands_reader_data_structures.RecievedCommand(id=-1, ts="", data="")

        # while decoded_recieve.id != command_answer_id:
        self.servo.send(message=set_zero_part_1)
        time.sleep(0.1)
        self.servo.send(message=set_zero_part_2)

        # self.servo.send( messages=set_zero_part_2)

        #     recv = self.servo.receive()
        #     # print(recv)
        #     decoded_recieve = self.command_reader.read_recieve(recv)

        # return decoded_recieve

    def general_move_command(self):
        move_command = can.Message(
            is_extended_id=False, arbitration_id=0x80
        )
        # print('GENERAL MOVE FROM SERVO', self.servo.servo_id)
        self.servo.send(message=move_command)

    def save_settings(self):
        command_id = '26140010'
        command_answer_id = commands_info_storage[command_id].answer_code + \
            self.servo.servo_id
        command_send_address = commands_info_storage[command_id].send_address

        save_settings = self.servo_commander.create_command(
            command_from_documentation=command_id, address=command_send_address, write_value=1
        )

        decoded_recieve = servo_realisation.commands_reader.commands_reader_data_structures.RecievedCommand(
            id=-1, ts="", data="")

        self.servo.send(message=save_settings)
        recv: can.Message = self.servo.receive()
        while recv.arbitration_id != command_answer_id:
            self.servo.send(message=save_settings)
            recv = self.servo.receive()
        # decoded_recieve = self.command_reader.read_recieve(recv)

        # return decoded_recieve


class ControlServoCan_test_2:
    def __init__(
        self, servo_object: servo_realisation.control_objects.servo_interface.ServoInterfaceCan
    ) -> None:

        self.servo = servo_object
        self.servo_commander = servo_realisation.commands_constructor.input_output_realisation.create_servo_command_constructor_can(
            servo_object=servo_object
        )

        self.command_reader = servo_realisation.commands_reader.input_output_realisation.create_servo_commands_reader_can()

        # проверка на наличие ключа в словаре
        if self.servo.servo_id not in servo_info_storage:
            servo_info_storage[self.servo.servo_id] = servo_realisation.commands_abstraction.commads_storage.ServoData(
                speed_value=-1, pos_value=-1, mode_value=-1)

        self.current_mode = self.read_mode()
        self.current_speed = self.read_speed()
        self.current_pos = self.read_pos()

        servo_info_storage[self.servo.servo_id] = servo_realisation.commands_abstraction.commads_storage.ServoData(
            speed_value=self.current_speed, pos_value=self.current_pos, mode_value=self.current_mode)

    def read_speed(self):
        command_id = '60810020'
        command_answer_id = commands_info_storage[command_id].answer_code + \
            self.servo.servo_id
        command_send_address = commands_info_storage[command_id].send_address

        read_speed = self.servo_commander.create_command(
            command_from_documentation=command_id, address=command_send_address
        )

        decoded_recieve = servo_realisation.commands_reader.commands_reader_data_structures.RecievedCommand(
            id=-1, ts="", data="")

        self.servo.send(message=read_speed)
        recv: can.Message = self.servo.receive()
        # while recv.arbitration_id != command_answer_id:
        #     self.servo.send(message=read_speed)
        #     recv = self.servo.receive()

        # decoded_recieve = self.command_reader.read_recieve(recv)

        # servo_info_storage[self.servo.servo_id].speed = decoded_recieve.decoded_data

        # return decoded_recieve

    def set_speed(self, value: int):
        if value != servo_info_storage[self.servo.servo_id].speed:

            command_id = '60810020'
            # command_answer_id = commands_info_storage[command_id].answer_code + self.servo.servo_id
            command_send_address = commands_info_storage[command_id].send_address

            set_speed = self.servo_commander.create_command(
                command_from_documentation=command_id, address=command_send_address, write_value=value
            )

            # decoded_recieve = servo_realisation.commands_reader.commands_reader_data_structures.RecievedCommand(id=-1, ts="", data="")

            time.sleep(0.1)
            self.servo.send(message=set_speed)
            # recv: can.Message = self.servo.receive()
            # while recv.arbitration_id != command_answer_id:
            #     # print('SET_SPEED=', value, 'SERVO', self.servo.servo_id)
            #     self.servo.send(message=set_speed)
            #     recv = self.servo.receive()
            # decoded_recieve = self.command_reader.read_recieve(recv)

            servo_info_storage[self.servo.servo_id].speed = value

            # return decoded_recieve

    def read_pos(self):
        command_id = '60640020'
        command_answer_id = commands_info_storage[command_id].answer_code + \
            self.servo.servo_id
        command_send_address = commands_info_storage[command_id].send_address

        read_pos = self.servo_commander.create_command(
            command_from_documentation=command_id, address=command_send_address
        )

        decoded_recieve = servo_realisation.commands_reader.commands_reader_data_structures.RecievedCommand(
            id=-1, ts="", data="")

        self.servo.send(message=read_pos)
        recv: can.Message = self.servo.receive()
        while recv.arbitration_id != command_answer_id:
            self.servo.send(message=read_pos)
            recv = self.servo.receive()
        decoded_recieve = self.command_reader.read_recieve(recv)

        servo_info_storage[self.servo.servo_id].pos = decoded_recieve.decoded_data

        return decoded_recieve

    def set_pos(self, value: int):
        if servo_info_storage[self.servo.servo_id].pos != value:

            # command_answer_id = 0x480 + self.servo.servo_id
            command_send_address = 0x500 + self.servo.servo_id

            write_value = self.servo_commander.only_convert_write_value_to_hex(
                write_value=value, num_of_bytes_for_command=4)
            set_pos = can.Message(
                arbitration_id=command_send_address,
                is_extended_id=False,
                data=write_value,
            )

            # decoded_recieve = servo_realisation.commands_reader.commands_reader_data_structures.RecievedCommand(id=-1, ts="", data="")

            time.sleep(0.1)
            self.servo.send(message=set_pos)
            # recv: can.Message = self.servo.receive()

            # while recv.arbitration_id != command_answer_id:
            #     # print('SET_POS=', value, 'SERVO', self.servo.servo_id)
            #     self.servo.send( message=set_pos)
            #     recv = self.servo.receive()
            # decoded_recieve = self.command_reader.read_recieve(recv)

            servo_info_storage[self.servo.servo_id].pos = value

            # return decoded_recieve

    def read_mode(self):
        command_id = '60600008'
        command_answer_id = commands_info_storage[command_id].answer_code + \
            self.servo.servo_id
        command_send_address = commands_info_storage[command_id].send_address

        read_mode = self.servo_commander.create_command(
            command_from_documentation=command_id, address=command_send_address
        )

        decoded_recieve = servo_realisation.commands_reader.commands_reader_data_structures.RecievedCommand(
            id=-1, ts="", data="")

        self.servo.send(message=read_mode)
        recv: can.Message = self.servo.receive()

        while recv.arbitration_id != command_answer_id:
            self.servo.send(message=read_mode)
            recv = self.servo.receive()
        decoded_recieve = self.command_reader.read_recieve(recv)

        servo_info_storage[self.servo.servo_id].mode = decoded_recieve.decoded_data

        return decoded_recieve

    def set_mode(self, value: int):
        if servo_info_storage[self.servo.servo_id].mode != value:
            command_id = '60640020'
            # command_answer_id = commands_info_storage[command_id].answer_code + self.servo.servo_id
            command_send_address = commands_info_storage[command_id].send_address

            set_mode = self.servo_commander.create_command(
                command_from_documentation=command_id, address=command_send_address, write_value=value
            )

            # decoded_recieve = servo_realisation.commands_reader.commands_reader_data_structures.RecievedCommand(id=-1, ts="", data="")

            time.sleep(0.1)
            self.servo.send(message=set_mode)
            # recv: can.Message = self.servo.receive()

            # while recv.arbitration_id != command_answer_id:
            #     self.servo.send( message=set_mode)
            #     recv = self.servo.receive()
            # decoded_recieve = self.command_reader.read_recieve(recv)

            servo_info_storage[self.servo.servo_id].mode = value

            # return decoded_recieve

    def set_zero_pos(self):
        address = 0x600 + self.servo.servo_id
        # # print(600+self.servo.servo_id)
        # command_answer_id = 580 + self.servo.servo_id
        set_zero_part_1 = can.Message(
            arbitration_id=address,
            is_extended_id=False,
            data=[0x2B, 0x0A, 0x26, 0x00, 0x66, 0xEA],
        )

        set_zero_part_2 = can.Message(
            arbitration_id=address,
            is_extended_id=False,
            data=[0x2B, 0x0A, 0x26, 0x00, 0x70, 0xEA],
        )
        # decoded_recieve = servo_realisation.commands_reader.commands_reader_data_structures.RecievedCommand(id=-1, ts="", data="")

        # while decoded_recieve.id != command_answer_id:
        time.sleep(0.1)
        self.servo.send(message=set_zero_part_1)
        time.sleep(0.1)
        self.servo.send(message=set_zero_part_2)

        # self.servo.send( messages=set_zero_part_2)

        #     recv = self.servo.receive()
        #     # print(recv)
        #     decoded_recieve = self.command_reader.read_recieve(recv)

        # return decoded_recieve

    def general_move_command(self):
        move_command = can.Message(
            is_extended_id=False, arbitration_id=0x80
        )
        # print('GENERAL MOVE FROM SERVO', self.servo.servo_id)
        self.servo.send(message=move_command)

    def save_settings(self):
        command_id = '26140010'
        # command_answer_id = commands_info_storage[command_id].answer_code + self.servo.servo_id
        command_send_address = commands_info_storage[command_id].send_address

        save_settings = self.servo_commander.create_command(
            command_from_documentation=command_id, address=command_send_address, write_value=1
        )

        # decoded_recieve = servo_realisation.commands_reader.commands_reader_data_structures.RecievedCommand(id=-1, ts="", data="")
        time.sleep(0.1)
        self.servo.send(message=save_settings)
        # recv: can.Message = self.servo.receive()
        # while recv.arbitration_id != command_answer_id:
        #     self.servo.send( message=save_settings)
        #     recv = self.servo.receive()
        # decoded_recieve = self.command_reader.read_recieve(recv)

        # return decoded_recieve

    def read_cur_speed(self):
        command_id = '606C0010'
        command_answer_id = commands_info_storage[command_id].answer_code + \
            self.servo.servo_id
        command_send_address = commands_info_storage[command_id].send_address

        read_mode = self.servo_commander.create_command(
            command_from_documentation=command_id, address=command_send_address
        )

        decoded_recieve = servo_realisation.commands_reader.commands_reader_data_structures.RecievedCommand(
            id=-1, ts="", data="")

        self.servo.send(message=read_mode)
        recv: can.Message = self.servo.receive()

        while recv.arbitration_id != command_answer_id:
            self.servo.send(message=read_mode)
            recv = self.servo.receive()
        decoded_recieve = self.command_reader.read_recieve(recv)

        servo_info_storage[self.servo.servo_id].mode = decoded_recieve.decoded_data

        return decoded_recieve
"""
