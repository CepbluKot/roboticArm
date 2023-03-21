import typing
import textwrap
import canalystii
import threading

from servo_realization.protocol_interface.protocol_interface import ProtocolInterface
from servo_realization.hardware_interface.hardware_interface import HardwareInterface

# to-do : make interface


class ReceivedMessage:
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
    __pos_command_full = 60640020
    __save_command_full = 26140010
    __error_check_command_full = '260E0010'
    __interpolation = 'interpolation'
    __voltage_check_command_full = 60790010
    __temperature_check_command_full = 26120010
    __current_check_command_full = 60780010
    __PWM_check_command_full = 26130010
    __speed_loop_integration_time_command_full = '60F90210'
    __enable_modbus_command_full = 26000010
    __driver_output_permission_command_full = 26010010
    __weak_magnet_angle_command_full = 26040010
    __speed_loop_scale_coefficient_command_full = '60F90110'
    __position_loop_scale_coefficient_command_full = '60FB0110'
    __speed_control_command_full = '60FB0210'
    __polarity_dir_command_full = 26090010
    __electronic_gear_molecules_command_full = '260A0010'
    __transfer_electronic_denominator_command_full = '260B0010'
    __incremental_position_command_full = '260C0020'
    __current_speed_check_command_full = '606C0010'
    __system_PWM_output_command_full = 26130010
    __new_servo_address_command_full = 26150010
    __stationary_max_power_command_full = 26180010
    __specials_command_full = 26190010
    __target_location_cache_command_full = '607A0020'
    __speed_mode_speed_command_full = '60FF0020'
    __can_connection_sync_speed_word_command_full = '261C0010'
    __max_current_command_full = '261D0010'
    __input_port_status_command_full = '60FD0010'
    __control_words_command_full = 60400010
    __status_word_command_full = 60410010
    __work_mode_command_full = 60600008
    __goto_home_mode_command_full = 60980008

    __RPDO4_object = 0x500
    __SDO_object = 0x600

    def __init__(
        self,
        hardware_interface: HardwareInterface,
        on_read_speed: typing.Callable[[ReceivedMessage], None],
        on_read_accel: typing.Callable[[ReceivedMessage], None],
        on_read_mode: typing.Callable[[ReceivedMessage], None],
        on_read_pos: typing.Callable[[ReceivedMessage], None],
        on_read_target_pos: typing.Callable[[ReceivedMessage], None],
        on_read_error_check: typing.Callable[[ReceivedMessage], None],
        on_voltage_check: typing.Callable[[ReceivedMessage], None],
        on_temperature_check: typing.Callable[[ReceivedMessage], None],
        on_current_check: typing.Callable[[ReceivedMessage], None],

        on_read_modbus_permission: typing.Callable[[ReceivedMessage], None],
        on_read_driver_output_permission: typing.Callable[[ReceivedMessage], None],
        on_read_weak_magnet_angle: typing.Callable[[ReceivedMessage], None],
        on_read_speed_loop_scale_coefficient: typing.Callable[[ReceivedMessage], None],
        on_read_speed_loop_integration_time: typing.Callable[[ReceivedMessage], None],
        on_read_position_loop_scale_coefficient: typing.Callable[[ReceivedMessage], None],
        on_read_speed_control: typing.Callable[[ReceivedMessage], None],
        on_read_polarity_dir: typing.Callable[[ReceivedMessage], None],
        on_read_electronic_gear_molecules: typing.Callable[[ReceivedMessage], None],
        on_read_transfer_electronic_denominator: typing.Callable[[ReceivedMessage], None],
        on_read_incremental_position: typing.Callable[[ReceivedMessage], None],
        on_read_system_PWM_output: typing.Callable[[ReceivedMessage], None],
        on_read_save: typing.Callable[[ReceivedMessage], None],
        on_read_address: typing.Callable[[ReceivedMessage], None],
        on_read_stationary_max_power: typing.Callable[[ReceivedMessage], None],
        on_read_target_location_cache: typing.Callable[[ReceivedMessage], None],
        on_read_can_connection_sync_speed_word: typing.Callable[[ReceivedMessage], None],
    ) -> None:

        self.__speed_command_short = self.__get_short_command(self.__speed_command_full)
        self.__accel_command_short = self.__get_short_command(self.__accel_command_full)
        self.__mode_command_short = self.__get_short_command(self.__mode_command_full)
        self.__save_command_short = self.__get_short_command(self.__save_command_full)
        self.__pos_command_short = self.__get_short_command(self.__pos_command_full)
        self.__error_check_command_short = int(self.__error_check_command_full[0:2], 16), int(self.__error_check_command_full[2:4], 16)
        self.__voltage_check_command_short = self.__get_short_command(self.__voltage_check_command_full)
        self.__temperature_check_command_short = self.__get_short_command(self.__temperature_check_command_full)
        self.__current_check_command_short = self.__get_short_command(self.__current_check_command_full)
        self.__PWM_check_command_short = self.__get_short_command(self.__PWM_check_command_full)
        self.__speed_loop_integration_time_command_short = int(self.__speed_loop_integration_time_command_full[0:2], 16), int(self.__speed_loop_integration_time_command_full[2:4], 16)
        self.__enable_modbus_command_short = self.__get_short_command(self.__enable_modbus_command_full)
        self.__driver_output_permission_command_short = self.__get_short_command(self.__driver_output_permission_command_full)
        self.__weak_magnet_angle_command_short = self.__get_short_command(self.__weak_magnet_angle_command_full)
        self.__speed_loop_scale_coefficient_command_short = int(self.__speed_loop_scale_coefficient_command_full[0:2], 16), int(self.__speed_loop_scale_coefficient_command_full[2:4], 16)
        self.__position_loop_scale_coefficient_command_short = int(self.__position_loop_scale_coefficient_command_full[0:2], 16), int(self.__position_loop_scale_coefficient_command_full[2:4], 16)
        self.__speed_control_command_short = int(self.__speed_control_command_full[0:2], 16), int(self.__speed_control_command_full[2:4], 16)
        self.__polarity_dir_command_short = self.__get_short_command(self.__polarity_dir_command_full)
        self.__electronic_gear_molecules_command_short = int(self.__electronic_gear_molecules_command_full[0:2], 16), int(self.__electronic_gear_molecules_command_full[2:4], 16)
        self.__transfer_electronic_denominator_command_short = int(self.__transfer_electronic_denominator_command_full[0:2], 16), int(self.__transfer_electronic_denominator_command_full[2:4], 16)
        self.__current_speed_command_short = int(self.__current_speed_check_command_full[0:2], 16), int(self.__current_speed_check_command_full[2:4], 16)
        self.__system_PWM_output_command_short = self.__get_short_command(self.__system_PWM_output_command_full)
        self.__new_servo_address_command_short = self.__get_short_command(self.__new_servo_address_command_full)
        self.__stationary_max_power_command_short = self.__get_short_command(self.__stationary_max_power_command_full)
        self.__specials_command_short = self.__get_short_command(self.__specials_command_full)
        self.__target_location_cache_command_short = int(self.__target_location_cache_command_full[0:2], 16), int(self.__target_location_cache_command_full[2:4], 16)
        self.__speed_mode_speed_command_short = int(self.__speed_mode_speed_command_full[0:2], 16), int(self.__speed_mode_speed_command_full[2:4], 16)
        self.__can_connection_sync_speed_word_command_short = int(self.__can_connection_sync_speed_word_command_full[0:2], 16), int(self.__can_connection_sync_speed_word_command_full[2:4], 16)
        self.__max_current_command_short = int(self.__max_current_command_full[0:2], 16), int(self.__max_current_command_full[2:4], 16)
        self.__input_port_status_command_short = int(self.__input_port_status_command_full[0:2], 16), int(self.__input_port_status_command_full[2:4], 16)
        self.__control_words_command_short = self.__get_short_command(self.__specials_command_full)
        self.__incremental_position_command_short = int(self.__incremental_position_command_full[0:2], 16), int(self.__incremental_position_command_full[2:4], 16)

        self.commands_parse_storage: typing.Dict[
            str, typing.Callable[[ReceivedMessage], None]
        ] = {
            self.__speed_command_short: on_read_speed,
            self.__accel_command_short: on_read_accel,
            self.__mode_command_short: on_read_mode,
            self.__pos_command_short: on_read_pos,
            self.__interpolation: on_read_target_pos,
            self.__error_check_command_short: on_read_error_check,
            self.__voltage_check_command_short: on_voltage_check,
            self.__temperature_check_command_short: on_temperature_check,
            self.__current_check_command_short: on_current_check,
            self.__enable_modbus_command_short: on_read_modbus_permission,
            self.__driver_output_permission_command_short: on_read_driver_output_permission,
            self.__weak_magnet_angle_command_short: on_read_weak_magnet_angle,
            self.__speed_loop_scale_coefficient_command_short: on_read_speed_loop_scale_coefficient,
            self.__speed_loop_integration_time_command_short: on_read_speed_loop_integration_time,
            self.__position_loop_scale_coefficient_command_short: on_read_position_loop_scale_coefficient,
            self.__speed_control_command_short: on_read_speed_control,
            self.__polarity_dir_command_short: on_read_polarity_dir,
            self.__electronic_gear_molecules_command_short: on_read_electronic_gear_molecules,
            self.__transfer_electronic_denominator_command_short: on_read_transfer_electronic_denominator,
            self.__incremental_position_command_short: on_read_incremental_position,
            self.__PWM_check_command_short: on_read_system_PWM_output,
            self.__save_command_short: on_read_save,
            self.__new_servo_address_command_short: on_read_address,
            self.__stationary_max_power_command_short: on_read_stationary_max_power,
            self.__target_location_cache_command_short: on_read_target_location_cache,
            self.__can_connection_sync_speed_word_command_short: on_read_can_connection_sync_speed_word
        }

        self.device = hardware_interface

    def __init_list_of_bytes(self, lenth):
        list_of_bytes = (0,) * lenth
        return list_of_bytes

    def __get_short_command(self, full_command: int):
        first_byte = full_command // 1000000
        second_byte = full_command // 10000 - first_byte * 100
        
        first_byte_hex_to_dec = first_byte // 10 * 16 + first_byte % 10
        second_byte_hex_to_dec = second_byte // 10 * 16 + second_byte % 10
        return first_byte_hex_to_dec, second_byte_hex_to_dec

    def parse_receive(self, msg: canalystii.Message) -> ReceivedMessage:
        id = hex(msg.can_id)
        servo_id = int(id[-1])
        ts = msg.timestamp
        data = msg.data

        recieved_command = ReceivedMessage(id=id, ts=ts, data=data)
        recieved_command.servo_id = servo_id

        num_of_bytes_to_read = hex(bytes(data)[0])

        if id[2:4] == "48":
            recieved_command.decoded_data = int.from_bytes(
                bytes(data)[:-4], byteorder="little"
            )
            recieved_command.command_data = self.__interpolation
            is_read = False
            recieved_command.is_read = is_read

            if recieved_command.command_data in self.commands_parse_storage:
                self.commands_parse_storage[recieved_command.command_data](recieved_command)

        elif num_of_bytes_to_read == "0x60":
            recieved_command.decoded_data = "success"
            is_read = False
            recieved_command.is_read = is_read
            recieved_command.command_data = data[2], data[1]

        elif num_of_bytes_to_read == "0x80":
            recieved_command.decoded_data = "fail"
            is_read = False
            recieved_command.is_read = is_read
            recieved_command.command_data = data[2], data[1]

        else:
            recieved_command.decoded_data = int.from_bytes(
                bytes(data)[4:], byteorder="little"
            )
            is_read = True
            recieved_command.is_read = is_read
            recieved_command.command_data = data[2], data[1]
        
            if recieved_command.command_data in self.commands_parse_storage:
                self.commands_parse_storage[recieved_command.command_data](recieved_command)

        return recieved_command

    def on_message(self, msg: canalystii.Message):
        return self.parse_receive(msg)

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

    def get_buffer(self):
        return self.device.get_device_buffer()


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

        # print("sped value = ", value)

        list_of_bytes = self.__init_list_of_bytes(4 + num_of_bytes_for_command)
        list_of_bytes = (bytes_code, command_byte_second, command_byte_first, 0) + value

        output_command = canalystii.Message(
            remote=False,
            extended=False,
            data_len=len(list_of_bytes),
            data=list_of_bytes,
            can_id=address + servo_id,
        )
        command_id = command_byte_first, command_byte_second

        # print("send speed --> ", output_command, list_of_bytes)

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

        # print("send mode --> ", output_command)

        command_id = command_byte_first, command_byte_second
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

        # print("send accel --> ", output_command)

        command_id = command_byte_first, command_byte_second
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

        value = 1

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

        command_id = command_byte_first, command_byte_second
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

        # print("send target_pos --> ", output_command)

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
        # print('command_byte_second',command_byte_second, 'command_byte_second_hex',command_byte_second_hex, 'command_byte_first',command_byte_first, 'command_byte_first_hex',command_byte_first_hex)
        final_command = (bytes_code, command_byte_second, command_byte_first, 0)

        output_command = canalystii.Message(
            remote=False,
            extended=False,
            data_len=len(final_command),
            data=final_command,
            can_id=address + servo_id,
        )

        command_id = command_byte_first, command_byte_second
        self.device.send(
            message=output_command, command_id=command_id, servo_id=servo_id, is_read=is_read
        )

    def read_acceleration(self, servo_id: int) -> canalystii.Message:
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

        command_id = command_byte_first, command_byte_second
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

        command_id = command_byte_first, command_byte_second
        self.device.send(
            message=output_command, command_id=command_id, servo_id=servo_id, is_read=is_read
        )

    def read_error_checker(self, servo_id: int) -> canalystii.Message:
        command_code_from_documentation = self.__error_check_command_full
        address = self.__SDO_object
        is_read = True

        num_of_bytes_for_command = (
            int(command_code_from_documentation[-2:], 16)
        ) // 8

        command_byte_first_hex = command_code_from_documentation[0:2]
        command_byte_second_hex = command_code_from_documentation[2:4]
        
        command_byte_first = int(command_byte_first_hex, 16)
        command_byte_second = int(command_byte_second_hex, 16)

        bytes_code = self.__get_bytes_code(
            num_of_bytes=num_of_bytes_for_command, is_read=is_read
        )

        final_command = (bytes_code, command_byte_second, command_byte_first, 0)

        output_command = canalystii.Message(
            remote=False,
            extended=False,
            data_len=len(final_command),
            data=final_command,
            can_id=address + servo_id,
        )

        command_id = command_byte_first, command_byte_second
        
        # print('command_id',command_id, final_command)
        
        self.device.send(
            message=output_command, command_id=command_id, servo_id=servo_id, is_read=is_read
        )

    def read_voltage(self, servo_id: int) -> canalystii.Message:
            command_code_from_documentation = self.__voltage_check_command_full
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

            command_id = command_byte_first, command_byte_second
            self.device.send(
                message=output_command, command_id=command_id, servo_id=servo_id, is_read=is_read
            )
        
    def read_temperature(self, servo_id: int) -> canalystii.Message:
        command_code_from_documentation = self.__temperature_check_command_full
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

        command_id = command_byte_first, command_byte_second
        self.device.send(
            message=output_command, command_id=command_id, servo_id=servo_id, is_read=is_read
        )

    def read_current(self, servo_id: int) -> canalystii.Message:
        command_code_from_documentation = self.__current_check_command_full
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

        command_id = command_byte_first, command_byte_second
        self.device.send(
            message=output_command, command_id=command_id, servo_id=servo_id, is_read=is_read
        )

    def read_save(self, servo_id: int) -> canalystii.Message:
        command_code_from_documentation = self.__save_command_full
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

        command_id = command_byte_first, command_byte_second
        self.device.send(
            message=output_command, command_id=command_id, servo_id=servo_id, is_read=is_read
        )

    def read_position(self, servo_id: int) -> canalystii.Message:
        command_code_from_documentation = self.__pos_command_full
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

        command_id = command_byte_first, command_byte_second
        self.device.send(
            message=output_command, command_id=command_id, servo_id=servo_id, is_read=is_read
        )

    def read_speed_loop_integration_time(self, servo_id: int) -> canalystii.Message:
        command_code_from_documentation = self.__speed_loop_integration_time_command_full

        address = self.__SDO_object
        is_read = True

        num_of_bytes_for_command = (
            int(command_code_from_documentation[-2:], 16)
        ) // 8

        command_byte_first_hex = command_code_from_documentation[0:2]
        command_byte_second_hex = command_code_from_documentation[2:4]
        
        command_byte_first = int(command_byte_first_hex, 16)
        command_byte_second = int(command_byte_second_hex, 16)

        bytes_code = self.__get_bytes_code(
            num_of_bytes=num_of_bytes_for_command, is_read=is_read
        )

        final_command = (bytes_code, command_byte_second, command_byte_first, 0)

        output_command = canalystii.Message(
            remote=False,
            extended=False,
            data_len=len(final_command),
            data=final_command,
            can_id=address + servo_id,
        )

        command_id = command_byte_first, command_byte_second
        
        # print('command_id',command_id, final_command)
        
        self.device.send(
            message=output_command, command_id=command_id, servo_id=servo_id, is_read=is_read
        )
    
    def send_speed_loop_integration_time(self, servo_id: int, value: int) -> canalystii.Message:
        command_code_from_documentation = self.__speed_loop_integration_time_command_full

        address = self.__SDO_object
        is_read = False

        num_of_bytes_for_command = (
            int(command_code_from_documentation[-2:], 16)
        ) // 8

        command_byte_first_hex = command_code_from_documentation[0:2]
        command_byte_second_hex = command_code_from_documentation[2:4]
        
        command_byte_first = int(command_byte_first_hex, 16)
        command_byte_second = int(command_byte_second_hex, 16)

        value = value

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

        command_id = command_byte_first, command_byte_second
        self.device.send(
            message=output_command, command_id=command_id, servo_id=servo_id, is_read=is_read
        )


############ new
    def send_modbus_status(self, servo_id: int, value: bool) -> canalystii.Message:
        command_code_from_documentation = self.__enable_modbus_command_full
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

        value = value

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

        command_id = command_byte_first, command_byte_second
        self.device.send(
            message=output_command, command_id=command_id, servo_id=servo_id, is_read=is_read
        )

    def read_modbus_status(self, servo_id: int) -> canalystii.Message:
        command_code_from_documentation = self.__enable_modbus_command_full
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

        command_id = command_byte_first, command_byte_second
        self.device.send(
            message=output_command, command_id=command_id, servo_id=servo_id, is_read=is_read
        )

    def send_driver_output_permission(self, servo_id: int, value: bool) -> canalystii.Message:
        command_code_from_documentation = self.__driver_output_permission_command_full
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

        value = value

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

        command_id = command_byte_first, command_byte_second
        self.device.send(
            message=output_command, command_id=command_id, servo_id=servo_id, is_read=is_read
        )

    def read_driver_output_permission(self, servo_id: int) -> canalystii.Message:
        command_code_from_documentation = self.__driver_output_permission_command_full
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

        command_id = command_byte_first, command_byte_second
        self.device.send(
            message=output_command, command_id=command_id, servo_id=servo_id, is_read=is_read
        )

    def send_weak_magnet_angle(self, servo_id: int, value: int) -> canalystii.Message:
        command_code_from_documentation = self.__weak_magnet_angle_command_full
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

        value = value

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

        command_id = command_byte_first, command_byte_second
        self.device.send(
            message=output_command, command_id=command_id, servo_id=servo_id, is_read=is_read
        )

    def read_weak_magnet_angle(self, servo_id: int) -> canalystii.Message:
        command_code_from_documentation = self.__weak_magnet_angle_command_full
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

        command_id = command_byte_first, command_byte_second
        self.device.send(
            message=output_command, command_id=command_id, servo_id=servo_id, is_read=is_read
        )

    def send_speed_loop_scale_coefficient(self, servo_id: int, value: int) -> canalystii.Message:
        command_code_from_documentation = self.__speed_loop_scale_coefficient_command_full
        address = self.__SDO_object
        is_read = False

        num_of_bytes_for_command = (
            int(command_code_from_documentation[-2:], 16)
        ) // 8

        command_byte_first_hex = command_code_from_documentation[0:2]
        command_byte_second_hex = command_code_from_documentation[2:4]
        
        command_byte_first = int(command_byte_first_hex, 16)
        command_byte_second = int(command_byte_second_hex, 16)

        value = value

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

        command_id = command_byte_first, command_byte_second
        self.device.send(
            message=output_command, command_id=command_id, servo_id=servo_id, is_read=is_read
        )

    def read_speed_loop_scale_coefficient(self, servo_id: int) -> canalystii.Message:

        command_code_from_documentation = self.__speed_loop_scale_coefficient_command_full
        address = self.__SDO_object
        is_read = True

        num_of_bytes_for_command = (
            int(command_code_from_documentation[-2:], 16)
        ) // 8

        command_byte_first_hex = command_code_from_documentation[0:2]
        command_byte_second_hex = command_code_from_documentation[2:4]
        
        command_byte_first = int(command_byte_first_hex, 16)
        command_byte_second = int(command_byte_second_hex, 16)

        bytes_code = self.__get_bytes_code(
            num_of_bytes=num_of_bytes_for_command, is_read=is_read
        )

        final_command = (bytes_code, command_byte_second, command_byte_first, 0)

        output_command = canalystii.Message(
            remote=False,
            extended=False,
            data_len=len(final_command),
            data=final_command,
            can_id=address + servo_id,
        )

        command_id = command_byte_first, command_byte_second
        
        # print('command_id',command_id, final_command)
        
        self.device.send(
            message=output_command, command_id=command_id, servo_id=servo_id, is_read=is_read
        )

    def send_position_loop_scale_coefficient(self, servo_id: int, value: int) -> canalystii.Message: # !!!
        command_code_from_documentation = self.__position_loop_scale_coefficient_command_full
        address = self.__SDO_object
        is_read = False

        num_of_bytes_for_command = (
            int(command_code_from_documentation[-2:], 16)
        ) // 8

        command_byte_first_hex = command_code_from_documentation[0:2]
        command_byte_second_hex = command_code_from_documentation[2:4]
        
        command_byte_first = int(command_byte_first_hex, 16)
        command_byte_second = int(command_byte_second_hex, 16)

        value = value

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

        command_id = command_byte_first, command_byte_second
        self.device.send(
            message=output_command, command_id=command_id, servo_id=servo_id, is_read=is_read
        )

    def read_position_loop_scale_coefficient(self, servo_id: int) -> canalystii.Message: # !!!

        command_code_from_documentation = self.__position_loop_scale_coefficient_command_full
        address = self.__SDO_object
        is_read = True

        num_of_bytes_for_command = (
            int(command_code_from_documentation[-2:], 16)
        ) // 8

        command_byte_first_hex = command_code_from_documentation[0:2]
        command_byte_second_hex = command_code_from_documentation[2:4]
        
        command_byte_first = int(command_byte_first_hex, 16)
        command_byte_second = int(command_byte_second_hex, 16)

        bytes_code = self.__get_bytes_code(
            num_of_bytes=num_of_bytes_for_command, is_read=is_read
        )

        final_command = (bytes_code, command_byte_second, command_byte_first, 0)

        output_command = canalystii.Message(
            remote=False,
            extended=False,
            data_len=len(final_command),
            data=final_command,
            can_id=address + servo_id,
        )

        command_id = command_byte_first, command_byte_second
        
        # print('command_id',command_id, final_command)
        
        self.device.send(
            message=output_command, command_id=command_id, servo_id=servo_id, is_read=is_read
        )

    def send_speed_control(self, servo_id: int, value: int) -> canalystii.Message: # !!!
        command_code_from_documentation = self.__speed_control_command_full
        address = self.__SDO_object
        is_read = False

        num_of_bytes_for_command = (
            int(command_code_from_documentation[-2:], 16)
        ) // 8

        command_byte_first_hex = command_code_from_documentation[0:2]
        command_byte_second_hex = command_code_from_documentation[2:4]
        
        command_byte_first = int(command_byte_first_hex, 16)
        command_byte_second = int(command_byte_second_hex, 16)

        value = value

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

        command_id = command_byte_first, command_byte_second
        self.device.send(
            message=output_command, command_id=command_id, servo_id=servo_id, is_read=is_read
        )

    def read_speed_control(self, servo_id: int) -> canalystii.Message: # !!!
        command_code_from_documentation = self.__speed_control_command_full
        address = self.__SDO_object
        is_read = True

        num_of_bytes_for_command = (
            int(command_code_from_documentation[-2:], 16)
        ) // 8

        command_byte_first_hex = command_code_from_documentation[0:2]
        command_byte_second_hex = command_code_from_documentation[2:4]
        
        command_byte_first = int(command_byte_first_hex, 16)
        command_byte_second = int(command_byte_second_hex, 16)

        bytes_code = self.__get_bytes_code(
            num_of_bytes=num_of_bytes_for_command, is_read=is_read
        )

        final_command = (bytes_code, command_byte_second, command_byte_first, 0)

        output_command = canalystii.Message(
            remote=False,
            extended=False,
            data_len=len(final_command),
            data=final_command,
            can_id=address + servo_id,
        )

        command_id = command_byte_first, command_byte_second
        
        # print('command_id',command_id, final_command)
        
        self.device.send(
            message=output_command, command_id=command_id, servo_id=servo_id, is_read=is_read
        )

    def send_polarity_dir(self, servo_id: int, value: bool) -> canalystii.Message:
        command_code_from_documentation = self.__polarity_dir_command_full
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

        # print("sped value = ", value)

        list_of_bytes = self.__init_list_of_bytes(4 + num_of_bytes_for_command)
        list_of_bytes = (bytes_code, command_byte_second, command_byte_first, 0) + value

        output_command = canalystii.Message(
            remote=False,
            extended=False,
            data_len=len(list_of_bytes),
            data=list_of_bytes,
            can_id=address + servo_id,
        )
        command_id = command_byte_first, command_byte_second

        # print("send speed --> ", output_command, list_of_bytes)

        self.device.send(
            message=output_command, command_id=command_id, servo_id=servo_id, is_read=is_read
        )

    def read_polarity_dir(self, servo_id: int) -> canalystii.Message:

        command_code_from_documentation = self.__polarity_dir_command_full
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
        # print('command_byte_second',command_byte_second, 'command_byte_second_hex',command_byte_second_hex, 'command_byte_first',command_byte_first, 'command_byte_first_hex',command_byte_first_hex)
        final_command = (bytes_code, command_byte_second, command_byte_first, 0)

        output_command = canalystii.Message(
            remote=False,
            extended=False,
            data_len=len(final_command),
            data=final_command,
            can_id=address + servo_id,
        )

        command_id = command_byte_first, command_byte_second
        self.device.send(
            message=output_command, command_id=command_id, servo_id=servo_id, is_read=is_read
        )

    def send_electronic_gear_molecules(self, servo_id: int, value: int) -> canalystii.Message:
        command_code_from_documentation = self.__electronic_gear_molecules_command_full
        address = self.__SDO_object
        is_read = False

        num_of_bytes_for_command = (
            int(command_code_from_documentation[-2:], 16)
        ) // 8

        command_byte_first_hex = command_code_from_documentation[0:2]
        command_byte_second_hex = command_code_from_documentation[2:4]
        
        command_byte_first = int(command_byte_first_hex, 16)
        command_byte_second = int(command_byte_second_hex, 16)

        value = value

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

        command_id = command_byte_first, command_byte_second
        self.device.send(
            message=output_command, command_id=command_id, servo_id=servo_id, is_read=is_read
        )

    def read_electronic_gear_molecules(self, servo_id: int) -> canalystii.Message:
        command_code_from_documentation = self.__electronic_gear_molecules_command_full
        address = self.__SDO_object
        is_read = True

        num_of_bytes_for_command = (
            int(command_code_from_documentation[-2:], 16)
        ) // 8

        command_byte_first_hex = command_code_from_documentation[0:2]
        command_byte_second_hex = command_code_from_documentation[2:4]
        
        command_byte_first = int(command_byte_first_hex, 16)
        command_byte_second = int(command_byte_second_hex, 16)

        bytes_code = self.__get_bytes_code(
            num_of_bytes=num_of_bytes_for_command, is_read=is_read
        )

        final_command = (bytes_code, command_byte_second, command_byte_first, 0)

        output_command = canalystii.Message(
            remote=False,
            extended=False,
            data_len=len(final_command),
            data=final_command,
            can_id=address + servo_id,
        )

        command_id = command_byte_first, command_byte_second
        
        # print('command_id',command_id, final_command)
        
        self.device.send(
            message=output_command, command_id=command_id, servo_id=servo_id, is_read=is_read
        )

    def send_electrical_transmission_denominator(self, servo_id: int, value: int) -> canalystii.Message:
        command_code_from_documentation = self.__transfer_electronic_denominator_command_full
        address = self.__SDO_object
        is_read = False

        num_of_bytes_for_command = (
            int(command_code_from_documentation[-2:], 16)
        ) // 8

        command_byte_first_hex = command_code_from_documentation[0:2]
        command_byte_second_hex = command_code_from_documentation[2:4]
        
        command_byte_first = int(command_byte_first_hex, 16)
        command_byte_second = int(command_byte_second_hex, 16)

        value = value

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

        command_id = command_byte_first, command_byte_second
        self.device.send(
            message=output_command, command_id=command_id, servo_id=servo_id, is_read=is_read
        )

    def read_electrical_transmission_denominator(self, servo_id: int) -> canalystii.Message:
        command_code_from_documentation = self.__transfer_electronic_denominator_command_full
        address = self.__SDO_object
        is_read = True

        num_of_bytes_for_command = (
            int(command_code_from_documentation[-2:], 16)
        ) // 8

        command_byte_first_hex = command_code_from_documentation[0:2]
        command_byte_second_hex = command_code_from_documentation[2:4]
        
        command_byte_first = int(command_byte_first_hex, 16)
        command_byte_second = int(command_byte_second_hex, 16)

        bytes_code = self.__get_bytes_code(
            num_of_bytes=num_of_bytes_for_command, is_read=is_read
        )

        final_command = (bytes_code, command_byte_second, command_byte_first, 0)

        output_command = canalystii.Message(
            remote=False,
            extended=False,
            data_len=len(final_command),
            data=final_command,
            can_id=address + servo_id,
        )

        command_id = command_byte_first, command_byte_second
        
        # print('command_id',command_id, final_command)
        
        self.device.send(
            message=output_command, command_id=command_id, servo_id=servo_id, is_read=is_read
        )

    def send_incremental_position(self, servo_id: int, value: int) -> canalystii.Message:
        command_code_from_documentation = self.__incremental_position_command_full
        address = self.__SDO_object
        is_read = False

        num_of_bytes_for_command = (
            int(command_code_from_documentation[-2:], 16)
        ) // 8

        command_byte_first_hex = command_code_from_documentation[0:2]
        command_byte_second_hex = command_code_from_documentation[2:4]
        
        command_byte_first = int(command_byte_first_hex, 16)
        command_byte_second = int(command_byte_second_hex, 16)

        value = value

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

        command_id = command_byte_first, command_byte_second
        self.device.send(
            message=output_command, command_id=command_id, servo_id=servo_id, is_read=is_read
        )

    def read_incremental_position(self, servo_id: int) -> canalystii.Message:
        command_code_from_documentation = self.__incremental_position_command_full
        address = self.__SDO_object
        is_read = True

        num_of_bytes_for_command = (
            int(command_code_from_documentation[-2:], 16)
        ) // 8

        command_byte_first_hex = command_code_from_documentation[0:2]
        command_byte_second_hex = command_code_from_documentation[2:4]
        
        command_byte_first = int(command_byte_first_hex, 16)
        command_byte_second = int(command_byte_second_hex, 16)

        bytes_code = self.__get_bytes_code(
            num_of_bytes=num_of_bytes_for_command, is_read=is_read
        )

        final_command = (bytes_code, command_byte_second, command_byte_first, 0)

        output_command = canalystii.Message(
            remote=False,
            extended=False,
            data_len=len(final_command),
            data=final_command,
            can_id=address + servo_id,
        )

        command_id = command_byte_first, command_byte_second
        
        # print('command_id',command_id, final_command)
        
        self.device.send(
            message=output_command, command_id=command_id, servo_id=servo_id, is_read=is_read
        )

    def read_current_speed(self, servo_id: int) -> canalystii.Message:
        command_code_from_documentation = self.__current_speed_check_command_full
        address = self.__SDO_object
        is_read = True

        num_of_bytes_for_command = (
            int(command_code_from_documentation[-2:], 16)
        ) // 8

        command_byte_first_hex = command_code_from_documentation[0:2]
        command_byte_second_hex = command_code_from_documentation[2:4]
        
        command_byte_first = int(command_byte_first_hex, 16)
        command_byte_second = int(command_byte_second_hex, 16)

        bytes_code = self.__get_bytes_code(
            num_of_bytes=num_of_bytes_for_command, is_read=is_read
        )

        final_command = (bytes_code, command_byte_second, command_byte_first, 0)

        output_command = canalystii.Message(
            remote=False,
            extended=False,
            data_len=len(final_command),
            data=final_command,
            can_id=address + servo_id,
        )

        command_id = command_byte_first, command_byte_second
        
        # print('command_id',command_id, final_command)
        
        self.device.send(
            message=output_command, command_id=command_id, servo_id=servo_id, is_read=is_read
        )

    def read_system_pwm_output(self, servo_id: int) -> canalystii.Message:

        command_code_from_documentation = self.__system_PWM_output_command_full

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
        # print('command_byte_second',command_byte_second, 'command_byte_second_hex',command_byte_second_hex, 'command_byte_first',command_byte_first, 'command_byte_first_hex',command_byte_first_hex)
        final_command = (bytes_code, command_byte_second, command_byte_first, 0)

        output_command = canalystii.Message(
            remote=False,
            extended=False,
            data_len=len(final_command),
            data=final_command,
            can_id=address + servo_id,
        )

        command_id = command_byte_first, command_byte_second
        self.device.send(
            message=output_command, command_id=command_id, servo_id=servo_id, is_read=is_read
        )

    def send_servo_address(self, servo_id: int, value: int) -> canalystii.Message:
        command_code_from_documentation = self.__new_servo_address_command_full

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

        # print("sped value = ", value)

        list_of_bytes = self.__init_list_of_bytes(4 + num_of_bytes_for_command)
        list_of_bytes = (bytes_code, command_byte_second, command_byte_first, 0) + value

        output_command = canalystii.Message(
            remote=False,
            extended=False,
            data_len=len(list_of_bytes),
            data=list_of_bytes,
            can_id=address + servo_id,
        )
        command_id = command_byte_first, command_byte_second

        # print("send speed --> ", output_command, list_of_bytes)

        self.device.send(
            message=output_command, command_id=command_id, servo_id=servo_id, is_read=is_read
        )

    def read_servo_address(self, servo_id: int) -> canalystii.Message:

        command_code_from_documentation = self.__new_servo_address_command_full
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

        command_id = command_byte_first, command_byte_second
        self.device.send(
            message=output_command, command_id=command_id, servo_id=servo_id, is_read=is_read
        )

    def send_stationary_max_power(self, servo_id: int, value: int) -> canalystii.Message:
        command_code_from_documentation = self.__stationary_max_power_command_full

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

        # print("sped value = ", value)

        list_of_bytes = self.__init_list_of_bytes(4 + num_of_bytes_for_command)
        list_of_bytes = (bytes_code, command_byte_second, command_byte_first, 0) + value

        output_command = canalystii.Message(
            remote=False,
            extended=False,
            data_len=len(list_of_bytes),
            data=list_of_bytes,
            can_id=address + servo_id,
        )
        command_id = command_byte_first, command_byte_second

        # print("send speed --> ", output_command, list_of_bytes)

        self.device.send(
            message=output_command, command_id=command_id, servo_id=servo_id, is_read=is_read
        )

    def read_stationary_max_power(self, servo_id: int) -> canalystii.Message:

        command_code_from_documentation = self.__stationary_max_power_command_full
        
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

        command_id = command_byte_first, command_byte_second
        self.device.send(
            message=output_command, command_id=command_id, servo_id=servo_id, is_read=is_read
        )

    def send_specials(self, servo_id: int, value: int) -> canalystii.Message:
        command_code_from_documentation = self.__specials_command_full
        
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

        # print("sped value = ", value)

        list_of_bytes = self.__init_list_of_bytes(4 + num_of_bytes_for_command)
        list_of_bytes = (bytes_code, command_byte_second, command_byte_first, 0) + value

        output_command = canalystii.Message(
            remote=False,
            extended=False,
            data_len=len(list_of_bytes),
            data=list_of_bytes,
            can_id=address + servo_id,
        )
        command_id = command_byte_first, command_byte_second

        # print("send speed --> ", output_command, list_of_bytes)

        self.device.send(
            message=output_command, command_id=command_id, servo_id=servo_id, is_read=is_read
        )

    def read_specials(self, servo_id: int) -> canalystii.Message:

        command_code_from_documentation = self.__specials_command_full
        command_code_from_documentation = self.__stationary_max_power_command_full
        
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

        command_id = command_byte_first, command_byte_second
        self.device.send(
            message=output_command, command_id=command_id, servo_id=servo_id, is_read=is_read
        )

    def send_target_position_cache(self, servo_id: int, value: int) -> canalystii.Message:
        command_code_from_documentation = self.__target_location_cache_command_full
        address = self.__SDO_object
        is_read = False

        num_of_bytes_for_command = (
            int(command_code_from_documentation[-2:], 16)
        ) // 8

        command_byte_first_hex = command_code_from_documentation[0:2]
        command_byte_second_hex = command_code_from_documentation[2:4]
        
        command_byte_first = int(command_byte_first_hex, 16)
        command_byte_second = int(command_byte_second_hex, 16)

        value = value

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

        command_id = command_byte_first, command_byte_second
        self.device.send(
            message=output_command, command_id=command_id, servo_id=servo_id, is_read=is_read
        )

    def read_target_position_cache(self, servo_id: int) -> canalystii.Message:
        command_code_from_documentation = self.__target_location_cache_command_full
        address = self.__SDO_object
        is_read = True

        num_of_bytes_for_command = (
            int(command_code_from_documentation[-2:], 16)
        ) // 8

        command_byte_first_hex = command_code_from_documentation[0:2]
        command_byte_second_hex = command_code_from_documentation[2:4]
        
        command_byte_first = int(command_byte_first_hex, 16)
        command_byte_second = int(command_byte_second_hex, 16)

        bytes_code = self.__get_bytes_code(
            num_of_bytes=num_of_bytes_for_command, is_read=is_read
        )

        final_command = (bytes_code, command_byte_second, command_byte_first, 0)

        output_command = canalystii.Message(
            remote=False,
            extended=False,
            data_len=len(final_command),
            data=final_command,
            can_id=address + servo_id,
        )

        command_id = command_byte_first, command_byte_second
        
        # print('command_id',command_id, final_command)
        
        self.device.send(
            message=output_command, command_id=command_id, servo_id=servo_id, is_read=is_read
        )

    def send_speed_mode_speed(self, servo_id: int, value: int) -> canalystii.Message:
        command_code_from_documentation = self.__speed_mode_speed_command_full
        address = self.__SDO_object
        is_read = False

        num_of_bytes_for_command = (
            int(command_code_from_documentation[-2:], 16)
        ) // 8

        command_byte_first_hex = command_code_from_documentation[0:2]
        command_byte_second_hex = command_code_from_documentation[2:4]
        
        command_byte_first = int(command_byte_first_hex, 16)
        command_byte_second = int(command_byte_second_hex, 16)

        value = value

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

        command_id = command_byte_first, command_byte_second
        self.device.send(
            message=output_command, command_id=command_id, servo_id=servo_id, is_read=is_read
        )

    def read_speed_mode_speed(self, servo_id: int) -> canalystii.Message:
        command_code_from_documentation = self.__speed_mode_speed_command_full
        address = self.__SDO_object
        is_read = True

        num_of_bytes_for_command = (
            int(command_code_from_documentation[-2:], 16)
        ) // 8

        command_byte_first_hex = command_code_from_documentation[0:2]
        command_byte_second_hex = command_code_from_documentation[2:4]
        
        command_byte_first = int(command_byte_first_hex, 16)
        command_byte_second = int(command_byte_second_hex, 16)

        bytes_code = self.__get_bytes_code(
            num_of_bytes=num_of_bytes_for_command, is_read=is_read
        )

        final_command = (bytes_code, command_byte_second, command_byte_first, 0)

        output_command = canalystii.Message(
            remote=False,
            extended=False,
            data_len=len(final_command),
            data=final_command,
            can_id=address + servo_id,
        )

        command_id = command_byte_first, command_byte_second
        
        # print('command_id',command_id, final_command)
        
        self.device.send(
            message=output_command, command_id=command_id, servo_id=servo_id, is_read=is_read
        )

    def send_can_connection_sync_speed_word(self, servo_id: int, value: int) -> canalystii.Message:
        command_code_from_documentation = self.__can_connection_sync_speed_word_command_full
        address = self.__SDO_object
        is_read = False

        num_of_bytes_for_command = (
            int(command_code_from_documentation[-2:], 16)
        ) // 8

        command_byte_first_hex = command_code_from_documentation[0:2]
        command_byte_second_hex = command_code_from_documentation[2:4]
        
        command_byte_first = int(command_byte_first_hex, 16)
        command_byte_second = int(command_byte_second_hex, 16)

        value = value

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

        command_id = command_byte_first, command_byte_second
        self.device.send(
            message=output_command, command_id=command_id, servo_id=servo_id, is_read=is_read
        )

    def read_can_connection_sync_speed_word(self, servo_id: int) -> canalystii.Message:
        command_code_from_documentation = self.__can_connection_sync_speed_word_command_full
        address = self.__SDO_object
        is_read = True

        num_of_bytes_for_command = (
            int(command_code_from_documentation[-2:], 16)
        ) // 8

        command_byte_first_hex = command_code_from_documentation[0:2]
        command_byte_second_hex = command_code_from_documentation[2:4]
        
        command_byte_first = int(command_byte_first_hex, 16)
        command_byte_second = int(command_byte_second_hex, 16)

        bytes_code = self.__get_bytes_code(
            num_of_bytes=num_of_bytes_for_command, is_read=is_read
        )

        final_command = (bytes_code, command_byte_second, command_byte_first, 0)

        output_command = canalystii.Message(
            remote=False,
            extended=False,
            data_len=len(final_command),
            data=final_command,
            can_id=address + servo_id,
        )

        command_id = command_byte_first, command_byte_second
        
        # print('command_id',command_id, final_command)
        
        self.device.send(
            message=output_command, command_id=command_id, servo_id=servo_id, is_read=is_read
        )

    def send_max_current(self, servo_id: int, value: int) -> canalystii.Message:
        command_code_from_documentation = self.__max_current_command_full
        address = self.__SDO_object
        is_read = False

        num_of_bytes_for_command = (
            int(command_code_from_documentation[-2:], 16)
        ) // 8

        command_byte_first_hex = command_code_from_documentation[0:2]
        command_byte_second_hex = command_code_from_documentation[2:4]
        
        command_byte_first = int(command_byte_first_hex, 16)
        command_byte_second = int(command_byte_second_hex, 16)

        value = value

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

        command_id = command_byte_first, command_byte_second
        self.device.send(
            message=output_command, command_id=command_id, servo_id=servo_id, is_read=is_read
        )

    def read_max_current(self, servo_id: int) -> canalystii.Message:
        command_code_from_documentation = self.__max_current_command_full
        address = self.__SDO_object
        is_read = True

        num_of_bytes_for_command = (
            int(command_code_from_documentation[-2:], 16)
        ) // 8

        command_byte_first_hex = command_code_from_documentation[0:2]
        command_byte_second_hex = command_code_from_documentation[2:4]
        
        command_byte_first = int(command_byte_first_hex, 16)
        command_byte_second = int(command_byte_second_hex, 16)

        bytes_code = self.__get_bytes_code(
            num_of_bytes=num_of_bytes_for_command, is_read=is_read
        )

        final_command = (bytes_code, command_byte_second, command_byte_first, 0)

        output_command = canalystii.Message(
            remote=False,
            extended=False,
            data_len=len(final_command),
            data=final_command,
            can_id=address + servo_id,
        )

        command_id = command_byte_first, command_byte_second
        
        # print('command_id',command_id, final_command)
        
        self.device.send(
            message=output_command, command_id=command_id, servo_id=servo_id, is_read=is_read
        )

    def read_input_port_status(self, servo_id: int) -> canalystii.Message:
        command_code_from_documentation = self.__input_port_status_command_full
        address = self.__SDO_object
        is_read = True

        num_of_bytes_for_command = (
            int(command_code_from_documentation[-2:], 16)
        ) // 8

        command_byte_first_hex = command_code_from_documentation[0:2]
        command_byte_second_hex = command_code_from_documentation[2:4]
        
        command_byte_first = int(command_byte_first_hex, 16)
        command_byte_second = int(command_byte_second_hex, 16)

        bytes_code = self.__get_bytes_code(
            num_of_bytes=num_of_bytes_for_command, is_read=is_read
        )

        final_command = (bytes_code, command_byte_second, command_byte_first, 0)

        output_command = canalystii.Message(
            remote=False,
            extended=False,
            data_len=len(final_command),
            data=final_command,
            can_id=address + servo_id,
        )

        command_id = command_byte_first, command_byte_second
        
        # print('command_id',command_id, final_command)
        
        self.device.send(
            message=output_command, command_id=command_id, servo_id=servo_id, is_read=is_read
        )

    def send_control_words(self, servo_id: int, value: int) -> canalystii.Message:  
        command_code_from_documentation = self.__control_words_command_full
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

        # print("send mode --> ", output_command)

        command_id = command_byte_first, command_byte_second
        self.device.send(
            message=output_command, command_id=command_id, servo_id=servo_id, is_read=is_read
        )
    
    def read_control_words(self, servo_id: int) -> canalystii.Message:
        command_code_from_documentation = self.__control_words_command_full
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

        command_id = command_byte_first, command_byte_second
        self.device.send(
            message=output_command, command_id=command_id, servo_id=servo_id, is_read=is_read
        )

    def send_status_word(self, servo_id: int, value: int) -> canalystii.Message:  
        command_code_from_documentation = self.__status_word_command_full
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

        # print("send mode --> ", output_command)

        command_id = command_byte_first, command_byte_second
        self.device.send(
            message=output_command, command_id=command_id, servo_id=servo_id, is_read=is_read
        )
    
    def read_status_word(self, servo_id: int) -> canalystii.Message:
        command_code_from_documentation = self.__status_word_command_full
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

        command_id = command_byte_first, command_byte_second
        self.device.send(
            message=output_command, command_id=command_id, servo_id=servo_id, is_read=is_read
        )

    def send_work_mode(self, servo_id: int, value: int) -> canalystii.Message:  
        command_code_from_documentation = self.__work_mode_command_full
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

        # print("send mode --> ", output_command)

        command_id = command_byte_first, command_byte_second
        self.device.send(
            message=output_command, command_id=command_id, servo_id=servo_id, is_read=is_read
        )
    
    def read_work_mode(self, servo_id: int) -> canalystii.Message:
        command_code_from_documentation = self.__work_mode_command_full
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

        command_id = command_byte_first, command_byte_second
        self.device.send(
            message=output_command, command_id=command_id, servo_id=servo_id, is_read=is_read
        )

    def send_goto_home_mode(self, servo_id: int, value: int) -> canalystii.Message:  
        command_code_from_documentation = self.__goto_home_mode_command_full
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

        # print("send mode --> ", output_command)

        command_id = command_byte_first, command_byte_second
        self.device.send(
            message=output_command, command_id=command_id, servo_id=servo_id, is_read=is_read
        )
    
    def read_goto_home_mode(self, servo_id: int) -> canalystii.Message:
        command_code_from_documentation = self.__goto_home_mode_command_full
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

        command_id = command_byte_first, command_byte_second
        self.device.send(
            message=output_command, command_id=command_id, servo_id=servo_id, is_read=is_read
        )
