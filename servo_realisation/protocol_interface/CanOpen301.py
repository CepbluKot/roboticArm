import typing
import textwrap
import canalystii
import threading
from servo_realisation.protocol_interface.protocol_interface import ProtocolInterface
from servo_realisation.hardware_interface.hardware_interface import HardwareInterface

# to-do : make interface


class ReceievedMessage:
    def __init__(self, id: str, ts: str, data: str) -> None:
        self.id = id
        self.ts = ts
        self.data = data
        self.servo_id = int()
        self.decoded_data = int()
        self.command_data = int()
        self.is_read = bool()

# modify_speed(servo_id, value)


class CanOpen301(ProtocolInterface):
    __speed_command_full = 60810020
    __accel_command_full = 60830020
    __mode_command_full = 60600008
    __save_command_full = 26140010
    __pos_command_full = 60640020
    __save_command_full = 26140010
    __interpolation = 'interpolation'

    __RPDO4_object = 0x500
    __SDO_object = 0x600

    __speed_command_short = __speed_command_full // 10000
    __accel_command_short = __accel_command_full // 10000
    __mode_command_short = __mode_command_full // 10000
    __save_command_short = __save_command_full // 10000
    __pos_command_short = __pos_command_full // 10000

    def __init__(
        self,
        hardware_interface: HardwareInterface,
        on_modify_speed: typing.Callable[[ReceievedMessage], None],
        on_modify_accel: typing.Callable[[ReceievedMessage], None],
        on_modify_mode: typing.Callable[[ReceievedMessage], None],
        on_modify_pos: typing.Callable[[ReceievedMessage], None],
        on_modify_target_pos: typing.Callable[[ReceievedMessage], None],
    ) -> None:
        self.commands_parse_storage: typing.Dict[
            str, typing.Callable[[ReceievedMessage], None]
        ] = {
            self.__speed_command_short: on_modify_speed,
            self.__accel_command_short: on_modify_accel,
            self.__mode_command_short: on_modify_mode,
            self.__pos_command_short: on_modify_pos,
            self.__RPDO4_object: on_modify_target_pos,
        }

        self.device = hardware_interface

        self.modify_speed = on_modify_speed
        self.modify_accel = on_modify_accel
        self.modify_mode = on_modify_mode
        self.modify_pos = on_modify_pos
        self.modify_target_pos = on_modify_target_pos

    def __init_list_of_bytes(self, lenth):
        list_of_bytes = (0,) * lenth
        return list_of_bytes

    def parse_recieve(self, msg: canalystii.Message) -> ReceievedMessage:
        id = hex(msg.can_id)
        servo_id = int(id[-1])
        ts = msg.timestamp
        data = msg.data

        recieved_command = ReceievedMessage(id=id, ts=ts, data=data)

        recieved_command.command_data = int(hex(data[2])[2:] + hex(data[1])[2:])
        recieved_command.servo_id = servo_id

        num_of_bytes_to_read = hex(bytes(data)[0])

        if id[2:4] == "48":
            recieved_command.decoded_data = int.from_bytes(
                bytes(data)[:-4], byteorder="little"
            )
            recieved_command.command_data = self.__interpolation
            is_read = False

        elif num_of_bytes_to_read == "0x60":
            recieved_command.decoded_data = "success"
            is_read = False

        elif num_of_bytes_to_read == "0x80":
            recieved_command.decoded_data = "fail"
            is_read = False

        else:
            recieved_command.decoded_data = int.from_bytes(
                bytes(data)[4:], byteorder="little"
            )
            is_read = True

        recieved_command.is_read = is_read

        return recieved_command

    def get_command_id(self, msg: canalystii.Message):
        return int(str(msg.data[2]) + str(msg.data[1]))

    def on_message(self, msg: canalystii.Message):
        return self.parse_recieve(msg)

    def __get_bytes_code(self, num_of_bytes: int = None, is_read: bool = False) -> str:
        if is_read:
            return 0x40

        else:
            if num_of_bytes == 1:
                return 0x2F

            elif num_of_bytes == 2:
                return 0x2B

            elif num_of_bytes == 4:
                return 0x23

            else:
                print("error - bytes_code_func - reached max num of bytes to send")

    def __convert_to_bytes(self, value: int, num_of_bytes: int = 4) -> typing.Tuple:
        value = int.to_bytes(value, length=num_of_bytes, byteorder="little")
        value = tuple(value)
        return value

    def check_is_buffer_empty(self):
        return self.device.check_is_device_buffer_empty()

    def send_speed(self, servo_id: int, value: int) -> canalystii.Message:
        # value -  в 16 формат с инверсией байт
        command_code_from_documentation = self.__speed_command_full
        address = self.__SDO_object
        is_read = False

        num_of_bytes_for_command = (
            ((command_code_from_documentation % 100) // 10 * 16)
            + ((command_code_from_documentation % 100) % 10 * 1)
        ) // 8
        command_byte_first_hex = command_code_from_documentation // 1000000
        command_byte_first = (
            command_byte_first_hex % 10 * 1 + command_byte_first_hex // 10 * 16
        )

        command_byte_second_hex = (
            command_code_from_documentation // 10000 * 10000
            - command_code_from_documentation // 1000000 * 1000000
        ) // 10000
        command_byte_second = (
            command_byte_second_hex % 10 * 1 + command_byte_second_hex // 10 * 16
        )

        value = round(value)

        bytes_code = self.__get_bytes_code(num_of_bytes=num_of_bytes_for_command)
        value = self.__convert_to_bytes(
            value=value, num_of_bytes=num_of_bytes_for_command
        )

        print("sped value = ", value)

        list_of_bytes = self.__init_list_of_bytes(4 + num_of_bytes_for_command)
        list_of_bytes = (bytes_code, command_byte_second, command_byte_first, 0) + value

        output_command = canalystii.Message(
            remote=False,
            extended=False,
            data_len=len(list_of_bytes),
            data=list_of_bytes,
            can_id=address + servo_id,
        )
        command_id = int(str(command_byte_first_hex) + str(command_byte_second_hex))

        print("send speed --> ", output_command, list_of_bytes)

        self.device.send(
            message=output_command, command_id=command_id, servo_id=servo_id, is_read=is_read
        )

    def send_mode(self, servo_id: int, value: int) -> canalystii.Message:
        command_code_from_documentation = self.__mode_command_full
        address = self.__SDO_object
        is_read = False

        num_of_bytes_for_command = (
            ((command_code_from_documentation % 100) // 10 * 16)
            + ((command_code_from_documentation % 100) % 10 * 1)
        ) // 8
        command_byte_first_hex = command_code_from_documentation // 1000000
        command_byte_first = (
            command_byte_first_hex % 10 * 1 + command_byte_first_hex // 10 * 16
        )

        command_byte_second_hex = (
            command_code_from_documentation // 10000 * 10000
            - command_code_from_documentation // 1000000 * 1000000
        ) // 10000
        command_byte_second = (
            command_byte_second_hex % 10 * 1 + command_byte_second_hex // 10 * 16
        )

        value = round(value)

        bytes_code = self.__get_bytes_code(num_of_bytes=num_of_bytes_for_command)
        value = self.__convert_to_bytes(
            value=value, num_of_bytes=num_of_bytes_for_command
        )

        list_of_bytes = self.__init_list_of_bytes(4 + num_of_bytes_for_command)
        list_of_bytes = (bytes_code, command_byte_second, command_byte_first, 0) + value

        output_command = canalystii.Message(
            remote=False,
            extended=False,
            data_len=len(list_of_bytes),
            data=list_of_bytes,
            can_id=address + servo_id,
        )

        print("send mode --> ", output_command)

        command_id = int(str(command_byte_first_hex) + str(command_byte_second_hex))
        self.device.send(
            message=output_command, command_id=command_id, servo_id=servo_id, is_read=is_read
        )

    def send_acceleration(self, servo_id: int, value: int) -> canalystii.Message:
        command_code_from_documentation = self.__accel_command_full
        address = self.__SDO_object
        is_read = False

        num_of_bytes_for_command = (
            ((command_code_from_documentation % 100) // 10 * 16)
            + ((command_code_from_documentation % 100) % 10 * 1)
        ) // 8
        command_byte_first_hex = command_code_from_documentation // 1000000
        command_byte_first = (
            command_byte_first_hex % 10 * 1 + command_byte_first_hex // 10 * 16
        )

        command_byte_second_hex = (
            command_code_from_documentation // 10000 * 10000
            - command_code_from_documentation // 1000000 * 1000000
        ) // 10000
        command_byte_second = (
            command_byte_second_hex % 10 * 1 + command_byte_second_hex // 10 * 16
        )

        value = round(value)

        bytes_code = self.__get_bytes_code(num_of_bytes=num_of_bytes_for_command)

        value = self.__convert_to_bytes(
            value=value, num_of_bytes=num_of_bytes_for_command
        )

        list_of_bytes = self.__init_list_of_bytes(4 + num_of_bytes_for_command)
        list_of_bytes = (bytes_code, command_byte_second, command_byte_first, 0) + value

        output_command = canalystii.Message(
            remote=False,
            extended=False,
            data_len=len(list_of_bytes),
            data=list_of_bytes,
            can_id=address + servo_id,
        )

        print("send accel --> ", output_command)

        command_id = int(str(command_byte_first_hex) + str(command_byte_second_hex))
        self.device.send(
            message=output_command, command_id=command_id, servo_id=servo_id, is_read=is_read
        )

    def send_save(self, servo_id: int) -> canalystii.Message:
        command_code_from_documentation = self.__save_command_full
        address = self.__SDO_object
        is_read = False

        num_of_bytes_for_command = (
            ((command_code_from_documentation % 100) // 10 * 16)
            + ((command_code_from_documentation % 100) % 10 * 1)
        ) // 8
        command_byte_first_hex = command_code_from_documentation // 1000000
        command_byte_first = (
            command_byte_first_hex % 10 * 1 + command_byte_first_hex // 10 * 16
        )

        command_byte_second_hex = (
            command_code_from_documentation // 10000 * 10000
            - command_code_from_documentation // 1000000 * 1000000
        ) // 10000
        command_byte_second = (
            command_byte_second_hex % 10 * 1 + command_byte_second_hex // 10 * 16
        )

        value = round(value)

        bytes_code = self.__get_bytes_code(num_of_bytes=num_of_bytes_for_command)
        value = self.__convert_to_bytes(
            value=value, num_of_bytes=num_of_bytes_for_command
        )

        list_of_bytes = self.__init_list_of_bytes(4 + num_of_bytes_for_command)
        list_of_bytes = (bytes_code, command_byte_second, command_byte_first, 0) + value

        output_command = canalystii.Message(
            remote=False,
            extended=False,
            data_len=len(list_of_bytes),
            data=list_of_bytes,
            can_id=address + servo_id,
        )

        command_id = int(str(command_byte_first_hex) + str(command_byte_second_hex))
        self.device.send(
            message=output_command, command_id=command_id, servo_id=servo_id, is_read=is_read
        )

    def send_zero_pos_set(self, servo_id: int) -> typing.List[canalystii.Message]:

        set_zero_part_1 = canalystii.Message(
            can_id=0x600 + servo_id,
            remote=False,
            extended=False,
            data_len=6,
            data=(0x2B, 0x0A, 0x26, 0x00, 0x66, 0xEA),
        )

        set_zero_part_2 = canalystii.Message(
            can_id=0x600 + servo_id,
            remote=False,
            extended=False,
            data_len=6,
            data=(0x2B, 0x0A, 0x26, 0x00, 0x70, 0xEA),
        )
        command = [set_zero_part_1, set_zero_part_2]
        self.device.send_without_buffer(message=command)

    def send_target_pos(self, servo_id: int, value: int) -> canalystii.Message:
        # check
        num_of_bytes_for_command = 4
        is_read = False

        value = round(value)

        value = self.__convert_to_bytes(
            value=value, num_of_bytes=num_of_bytes_for_command
        )

        output_command = canalystii.Message(
            remote=False,
            extended=False,
            data_len=4,
            data=value,
            can_id=self.__RPDO4_object + servo_id,
        )

        print("send target_pos --> ", output_command)

        self.device.send(
            message=output_command, command_id=self.__interpolation, servo_id=servo_id, is_read=is_read
        )

    def send_general_move_command(self) -> canalystii.Message:
        command = canalystii.Message(
            remote=False, extended=False, data_len=0, can_id=0x80
        )

        self.device.send_without_buffer(message=command)

    def read_speed(self, servo_id: int) -> canalystii.Message:
        command_code_from_documentation = self.__speed_command_full
        address = self.__SDO_object
        is_read = True

        num_of_bytes_for_command = (
            ((command_code_from_documentation % 100) // 10 * 16)
            + ((command_code_from_documentation % 100) % 10 * 1)
        ) // 8
        command_byte_first_hex = command_code_from_documentation // 1000000
        command_byte_first = (
            command_byte_first_hex % 10 * 1 + command_byte_first_hex // 10 * 16
        )

        command_byte_second_hex = (
            command_code_from_documentation // 10000 * 10000
            - command_code_from_documentation // 1000000 * 1000000
        ) // 10000
        command_byte_second = (
            command_byte_second_hex % 10 * 1 + command_byte_second_hex // 10 * 16
        )

        bytes_code = self.__get_bytes_code(
            num_of_bytes=num_of_bytes_for_command, is_read=1
        )

        final_command = (bytes_code, command_byte_second, command_byte_first, 0)

        output_command = canalystii.Message(
            remote=False,
            extended=False,
            data_len=len(final_command),
            data=final_command,
            can_id=address + servo_id,
        )

        command_id = int(str(command_byte_first_hex) + str(command_byte_second_hex))
        self.device.send(
            message=output_command, command_id=command_id, servo_id=servo_id, is_read=is_read
        )

    def read_accelearation(self, servo_id: int) -> canalystii.Message:
        command_code_from_documentation = self.__accel_command_full
        address = self.__SDO_object
        is_read = True

        num_of_bytes_for_command = (
            ((command_code_from_documentation % 100) // 10 * 16)
            + ((command_code_from_documentation % 100) % 10 * 1)
        ) // 8
        command_byte_first_hex = command_code_from_documentation // 1000000
        command_byte_first = (
            command_byte_first_hex % 10 * 1 + command_byte_first_hex // 10 * 16
        )

        command_byte_second_hex = (
            command_code_from_documentation // 10000 * 10000
            - command_code_from_documentation // 1000000 * 1000000
        ) // 10000
        command_byte_second = (
            command_byte_second_hex % 10 * 1 + command_byte_second_hex // 10 * 16
        )

        bytes_code = self.__get_bytes_code(
            num_of_bytes=num_of_bytes_for_command, is_read=1
        )

        final_command = (bytes_code, command_byte_second, command_byte_first, 0)

        output_command = canalystii.Message(
            remote=False,
            extended=False,
            data_len=len(final_command),
            data=final_command,
            can_id=address + servo_id,
        )

        command_id = int(str(command_byte_first_hex) + str(command_byte_second_hex))
        self.device.send(
            message=output_command, command_id=command_id, servo_id=servo_id, is_read=is_read
        )

    def read_mode(self, servo_id: int) -> canalystii.Message:
        command_code_from_documentation = self.__mode_command_full
        address = self.__SDO_object

        is_read = True

        num_of_bytes_for_command = (
            ((command_code_from_documentation % 100) // 10 * 16)
            + ((command_code_from_documentation % 100) % 10 * 1)
        ) // 8
        command_byte_first_hex = command_code_from_documentation // 1000000
        command_byte_first = (
            command_byte_first_hex % 10 * 1 + command_byte_first_hex // 10 * 16
        )

        command_byte_second_hex = (
            command_code_from_documentation // 10000 * 10000
            - command_code_from_documentation // 1000000 * 1000000
        ) // 10000
        command_byte_second = (
            command_byte_second_hex % 10 * 1 + command_byte_second_hex // 10 * 16
        )

        bytes_code = self.__get_bytes_code(
            num_of_bytes=num_of_bytes_for_command, is_read=1
        )

        final_command = (bytes_code, command_byte_second, command_byte_first, 0)

        output_command = canalystii.Message(
            remote=False,
            extended=False,
            data_len=len(final_command),
            data=final_command,
            can_id=address + servo_id,
        )

        command_id = int(str(command_byte_first_hex) + str(command_byte_second_hex))
        self.device.send(
            message=output_command, command_id=command_id, servo_id=servo_id, is_read=is_read
        )

    def read_error_checker(self, servo_id: int) -> canalystii.Message:
        pass
