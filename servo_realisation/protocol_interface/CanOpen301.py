import typing
import textwrap
import canalystii
import threading
from servo_realisation.protocol_interface.protocol_interface import ProtocolInterface
from servo_realisation.hardware_interface.hardware_interface import HardwareInterface
from servo_realisation.hardware_interface.USB_CAN import USB_CAN
# to-do : make interface


class ReceievedCommand:
    def __init__(self, id: int, ts: str, data: str) -> None:
        self.id = id
        self.ts = ts
        self.data = data
        self.servo_id = int()
        self.decoded_data = int()
        self.command_data = str()

# modify_speed(servo_id, value)


class CanOpen301(ProtocolInterface):
    __speed_command_full = 0x60810020
    __accel_command_full = 0x60830020
    __mode_command_full = 0x60600008
    __save_command_full = 0x26140010
    __pos_command_full = 0x60640020
    __save_command_full = 0x26140010

    __RPDO4_object = 0x500
    __SDO_object = 0x600


    __speed_command_short = __speed_command_full[:4]
    __accel_command_short = __accel_command_full[:4]
    __mode_command_short = __mode_command_full[:4]
    __save_command_short = __save_command_full[:4]
    __pos_command_short = __pos_command_full[:4]


    def __init__(self, hardware_interface: HardwareInterface, modify_speed: typing.Callable[[ReceievedCommand], None], modify_accel: typing.Callable[[ReceievedCommand], None], modify_mode: typing.Callable[[ReceievedCommand], None], modify_pos: typing.Callable[[ReceievedCommand], None], modify_target_pos: typing.Callable[[ReceievedCommand], None]) -> None:
        self.commands_parse_storage: typing.Dict[str, typing.Callable[[ReceievedCommand], None]] = {
            self.__speed_command_short: modify_speed,
            self.__accel_command_short: modify_accel,
            self.__mode_command_short: modify_mode,
            self.__pos_command_short: modify_pos,
            self.__RPDO4_object: modify_target_pos,
        }

        self.device = hardware_interface

        self.modify_speed = modify_speed
        self.modify_accel = modify_accel
        self.modify_mode = modify_mode
        self.modify_pos = modify_pos
        self.modify_target_pos = modify_target_pos


    def __parse_recieve(self, raw_data: str,) -> ReceievedCommand:
        recieve = str(raw_data)

        id = int(recieve[recieve.index('ID=') + len('ID=') + 2: recieve.index(' TS=')])
        servo_id = id % 10
        ts = int(recieve[recieve.index('TS=') + len('TS=') + 2: recieve.index(' Data=')], 16)
        data = recieve[recieve.index("Data=") + len("Data=") :]

        recieved_command = ReceievedCommand(id=id, ts=ts, data=data)
        data = textwrap.wrap(recieved_command.data, 2)

        recieved_command.command_data = data[2] + data[1]
        recieved_command.servo_id = servo_id

        num_of_bytes_to_read = data[0]

        if int(id / 10) == 48:
            data = data[:3]
            decoded_data = ''
            decoded_data += data[2]
            decoded_data += data[1]
            decoded_data += data[0]
            recieved_command.decoded_data = int(decoded_data, 16)

        elif num_of_bytes_to_read == "4f":
            data = data[3:]
            decoded_data = ""
            decoded_data += data[1]
            recieved_command.decoded_data = int(decoded_data, 16)

        elif num_of_bytes_to_read == "4b":
            data = data[3:]
            decoded_data = ""
            decoded_data += data[2]
            decoded_data += data[1]
            recieved_command.decoded_data = int(decoded_data, 16)

        elif num_of_bytes_to_read == "43":
            data = data[3:]
            decoded_data = ""
            decoded_data += data[4]
            decoded_data += data[3]
            decoded_data += data[2]
            decoded_data += data[1]
            recieved_command.decoded_data = int(decoded_data, 16)

        elif num_of_bytes_to_read == "60":
            recieved_command.decoded_data = 'success'

        elif num_of_bytes_to_read == "80":
            recieved_command.decoded_data = 'fail'

        else:
            data = data[3:]
        
        return recieved_command

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
                print('error - bytes_code_func - reached max num of bytes to send')

    def __determinte_lenth(num_of_bytes_to_read: str): # new
        if num_of_bytes_to_read == 0x4f:
            return 1
        
        elif num_of_bytes_to_read == 0x4b:
            return 2

        elif num_of_bytes_to_read == 0x43:
            return 4

    def __convert_value_to_hex(self, value: int, num_of_bytes: int):
        result = []
        write_value = hex(write_value)[2:]

        num_of_iterations = 0

        while write_value:
            result.append("0x" + write_value[-2:])
            write_value = write_value[:-2]
            num_of_iterations += 1

        while num_of_bytes != num_of_iterations:
            result.append("0x00")
            num_of_iterations += 1

        convert_to_hex = ()
        
        for element in result:
            convert_to_hex += (int(element, 0),)

    def __convert_message_from_bytes_to_dec(self, input: canalystii.protocol.c_ubyte*8):
        len_of_Data_to_read = self.__determinte_lenth(input[0])
        
        to_read = bytearray(input[-len_of_Data_to_read:])
        output = bytes()
        for a in to_read:
            output += a.to_bytes(1, byteorder='big')
    
        return int.from_bytes(output, byteorder='little')

    # def __parse_send(self, command_code_from_documentation: str, address: str, servo_id: str, write_value=None) -> canalystii.Message:
    #     result = []
    #     num_of_bytes_for_command = int(int(command_code_from_documentation[-2:], 16) / 8)

    #     command_byte_first = command_code_from_documentation[:2]
    #     command_byte_second = command_code_from_documentation[2:4]


    #     if write_value and not command_code_from_documentation:
    #         write_value = round(write_value)

    #         write_value = hex(write_value)[2:]

    #         num_of_iterations = 0

    #         while write_value:
    #             result.append("0x" + write_value[-2:])
    #             write_value = write_value[:-2]
    #             num_of_iterations += 1

    #         while num_of_bytes_for_command != num_of_iterations:
    #             result.append("0x00")
    #             num_of_iterations += 1

    #         convert_to_hex = ()
            
    #         for element in result:
    #             convert_to_hex += (int(element, 0),)


    #         output_command = canalystii.Message(
    #             remote=False,
    #             extended=False,
    #             data_len=len(convert_to_hex),
    #             data=convert_to_hex,
    #             can_id=address + servo_id,
    #         )
            

    #     elif write_value:
    #         write_value = round(write_value)
            
    #         result.append(self.__get_bytes_code(num_of_bytes=num_of_bytes_for_command))
    #         result.append("0x" + command_byte_second)
    #         result.append("0x" + command_byte_first)
    #         result.append("0x00")

    #         write_value = hex(write_value)[2:]

    #         num_of_iterations = 0

    #         while write_value:
    #             result.append("0x" + write_value[-2:])
    #             write_value = write_value[:-2]
    #             num_of_iterations += 1

    #         while num_of_bytes_for_command != num_of_iterations:
    #             result.append("0x00")
    #             num_of_iterations += 1

    #         convert_to_hex = ()
            
    #         for element in result:
    #             convert_to_hex += (int(element, 0),)


    #         output_command = canalystii.Message(
    #             remote=False,
    #             extended=False,
    #             data_len=len(convert_to_hex),
    #             data=convert_to_hex,
    #             can_id=address + servo_id,
    #         )
            

    #     else:
    #         result.append(
    #             self.__get_bytes_code(num_of_bytes=num_of_bytes_for_command, is_read=True)
    #         )
    #         result.append("0x" + command_byte_second)
    #         result.append("0x" + command_byte_first)
    #         result.append("0x00")

    #         convert_to_hex = ()
    #         for element in result:
    #             convert_to_hex += (int(element, 0),)

    #         output_command = canalystii.Message(
    #             remote=False,
    #             extended=False,
    #             data_len=len(convert_to_hex),
    #             data=convert_to_hex,
    #             can_id=address + servo_id,
    #         )

    #     return output_command



    def __parse_send_new(self, command_code_from_documentation: str, address: str, servo_id: str, write_value:int=None) -> canalystii.Message:
        num_of_bytes_for_command = int(int(command_code_from_documentation[-2:], 16) / 8)

        command_byte_first = command_code_from_documentation[:2]
        command_byte_second = command_code_from_documentation[2:4]


        if write_value and not command_code_from_documentation:
            write_value = round(write_value)

            write_value = int.to_bytes(write_value, length=num_of_bytes_for_command, byteorder='little')


            output_command = canalystii.Message(
                remote=False,
                extended=False,
                data_len=len(write_value),
                data=write_value,
                can_id=address + servo_id,
            )
            

        elif write_value:
            write_value = round(write_value)
            
            command_byte_first = int.to_bytes(command_byte_first, 1, 'little')
            command_byte_second = int.to_bytes(command_byte_second, 1, 'little')

            bytes_code = self.__get_bytes_code(num_of_bytes=num_of_bytes_for_command)

            write_value = int.to_bytes(write_value, length=num_of_bytes_for_command, byteorder='little')

            final_command = bytes_code + command_byte_first + command_byte_second + write_value

            output_command = canalystii.Message(
                remote=False,
                extended=False,
                data_len=len(final_command),
                data=final_command,
                can_id=address + servo_id,
            )
            
        else:
            bytes_code = self.__get_bytes_code(num_of_bytes=num_of_bytes_for_command)

            command_byte_first = int.to_bytes(command_byte_first, 1, 'little')
            command_byte_second = int.to_bytes(command_byte_second, 1, 'little')
            null_byte = int.to_bytes(0, length=1, byteorder='little')

            final_command = bytes_code + command_byte_first + command_byte_second + null_byte

            output_command = canalystii.Message(
                remote=False,
                extended=False,
                data_len=len(final_command),
                data=final_command,
                can_id=address + servo_id,
            )

        return output_command

    def __process_message(self, raw_data: str) -> None:
        parsed_data = self.__parse_recieve(raw_data=raw_data)

        if parsed_data.decoded_data != 'success' and parsed_data.decoded_data != 'fail':
            if int(parsed_data.id / 10) == 48:
                self.commands_parse_storage[self.__RPDO4_object](parsed_data)
                
            elif parsed_data.command_data in self.commands_parse_storage:
                self.commands_parse_storage[parsed_data.command_data](parsed_data)

    def send_speed(self, servo_id: int, value: int) -> canalystii.Message:
        # value -  в 16 формат с инверсией байт

        command_code_from_documentation = self.__speed_command_full
        num_of_bytes_for_command = int(int(command_code_from_documentation[-2:], 16) / 8)

        command_byte_first = command_code_from_documentation[:2]
        command_byte_second = command_code_from_documentation[2:4]

        write_value = round(value)
    
        command_byte_first = int.to_bytes(command_byte_first, 1, 'little')
        command_byte_second = int.to_bytes(command_byte_second, 1, 'little')

        num_of_bytes_code = self.__get_bytes_code(num_of_bytes=num_of_bytes_for_command)
        write_value = int.to_bytes(write_value, length=num_of_bytes_for_command, byteorder='little')

        final_command = num_of_bytes_code + command_byte_first + command_byte_second + write_value

        command = canalystii.Message(
            remote=False,
            extended=False,
            data_len=len(final_command),
            data=final_command,
            can_id=self.__SDO_object + servo_id,
        )

        self.device.send(message=command)

    def send_mode(self, servo_id: int, value: int) -> canalystii.Message:
        command_code_from_documentation = self.__mode_command_full
        num_of_bytes_for_command = int(int(command_code_from_documentation[-2:], 16) / 8)

        command_byte_first = command_code_from_documentation[:2]
        command_byte_second = command_code_from_documentation[2:4]

        write_value = round(value)
    
        command_byte_first = int.to_bytes(command_byte_first, 1, 'little')
        command_byte_second = int.to_bytes(command_byte_second, 1, 'little')

        num_of_bytes_code = self.__get_bytes_code(num_of_bytes=num_of_bytes_for_command)
        write_value = int.to_bytes(write_value, length=num_of_bytes_for_command, byteorder='little')

        final_command = num_of_bytes_code + command_byte_first + command_byte_second + write_value

        command = canalystii.Message(
            remote=False,
            extended=False,
            data_len=len(final_command),
            data=final_command,
            can_id=self.__SDO_object + servo_id,
        )

        self.device.send(message=command)
    
    def send_acceleration(self, servo_id: int, value: int) -> canalystii.Message:
        command_code_from_documentation = self.__accel_command_full
        num_of_bytes_for_command = int(int(command_code_from_documentation[-2:], 16) / 8)

        command_byte_first = command_code_from_documentation[:2]
        command_byte_second = command_code_from_documentation[2:4]

        write_value = round(value)
    
        command_byte_first = int.to_bytes(command_byte_first, 1, 'little')
        command_byte_second = int.to_bytes(command_byte_second, 1, 'little')

        num_of_bytes_code = self.__get_bytes_code(num_of_bytes=num_of_bytes_for_command)
        write_value = int.to_bytes(write_value, length=num_of_bytes_for_command, byteorder='little')

        final_command = num_of_bytes_code + command_byte_first + command_byte_second + write_value

        command = canalystii.Message(
            remote=False,
            extended=False,
            data_len=len(final_command),
            data=final_command,
            can_id=self.__SDO_object + servo_id,
        )

        self.device.send(message=command)
  
    def send_save(self, servo_id: int) -> canalystii.Message:
        command_code_from_documentation = self.__save_command_full
        num_of_bytes_for_command = int(int(command_code_from_documentation[-2:], 16) / 8)

        command_byte_first = command_code_from_documentation[:2]
        command_byte_second = command_code_from_documentation[2:4]

        write_value = 1
    
        command_byte_first = int.to_bytes(command_byte_first, 1, 'little')
        command_byte_second = int.to_bytes(command_byte_second, 1, 'little')

        num_of_bytes_code = self.__get_bytes_code(num_of_bytes=num_of_bytes_for_command)
        write_value = int.to_bytes(write_value, length=num_of_bytes_for_command, byteorder='little')

        final_command = num_of_bytes_code + command_byte_first + command_byte_second + write_value

        command = canalystii.Message(
            remote=False,
            extended=False,
            data_len=len(final_command),
            data=final_command,
            can_id=self.__SDO_object + servo_id,
        )

        self.device.send(message=command)

    def send_zero_pos_set(self, servo_id: int) -> typing.List[canalystii.Message]:
        set_zero_part_1 = canalystii.Message(
            can_id=0x600+servo_id,
            remote=False,
            extended=False,
            data_len=6,
            data=(0x2B, 0x0A, 0x26, 0x00, 0x66, 0xEA),
        )

        set_zero_part_2 = canalystii.Message(
            can_id=0x600+servo_id,
            remote=False,
            extended=False,
            data_len=6,
            data=(0x2B, 0x0A, 0x26, 0x00, 0x70, 0xEA),
        )
        command = [set_zero_part_1, set_zero_part_2]
        self.device.send(message=command)

    def send_target_pos(self, servo_id: int, value: int) -> canalystii.Message:
        num_of_bytes_for_command = 4

        write_value = round(write_value)
        write_value = int.to_bytes(write_value, length=num_of_bytes_for_command, byteorder='little')

        command = canalystii.Message(
            remote=False,
            extended=False,
            data_len=len(write_value),
            data=write_value,
            can_id=self.__RPDO4_object + servo_id,
        )
        
        self.device.send(message=command)

    def send_general_move_command(self) -> canalystii.Message:
        command = canalystii.Message(
            remote=False, extended=False, data_len=0, can_id=0x80
        )
        self.device.send(message=command)
        
    def read_speed(self, servo_id: int) -> canalystii.Message:
        command_code_from_documentation = self.__speed_command_full
        
        num_of_bytes_for_command = int(int(command_code_from_documentation[-2:], 16) / 8)
        command_byte_first = command_code_from_documentation[:2]
        command_byte_second = command_code_from_documentation[2:4]


        bytes_code = self.__get_bytes_code(num_of_bytes=num_of_bytes_for_command)

        command_byte_first = int.to_bytes(command_byte_first, 1, 'little')
        command_byte_second = int.to_bytes(command_byte_second, 1, 'little')
        null_byte = int.to_bytes(0, length=1, byteorder='little')

        final_command = bytes_code + command_byte_first + command_byte_second + null_byte

        command = canalystii.Message(
            remote=False,
            extended=False,
            data_len=len(final_command),
            data=final_command,
            can_id=self.__SDO_object + servo_id,
        )
        self.device.send(message=command)

    def read_accelearation(self, servo_id: int) -> canalystii.Message:
        command_code_from_documentation = self.__accel_command_full
        
        num_of_bytes_for_command = int(int(command_code_from_documentation[-2:], 16) / 8)
        command_byte_first = command_code_from_documentation[:2]
        command_byte_second = command_code_from_documentation[2:4]


        bytes_code = self.__get_bytes_code(num_of_bytes=num_of_bytes_for_command)

        command_byte_first = int.to_bytes(command_byte_first, 1, 'little')
        command_byte_second = int.to_bytes(command_byte_second, 1, 'little')
        null_byte = int.to_bytes(0, length=1, byteorder='little')

        final_command = bytes_code + command_byte_first + command_byte_second + null_byte

        command = canalystii.Message(
            remote=False,
            extended=False,
            data_len=len(final_command),
            data=final_command,
            can_id=self.__SDO_object + servo_id,
        )
        self.device.send(message=command)

    def read_mode(self, servo_id: int) -> canalystii.Message:
        command_code_from_documentation = self.__mode_command_full
        
        num_of_bytes_for_command = int(int(command_code_from_documentation[-2:], 16) / 8)
        command_byte_first = command_code_from_documentation[:2]
        command_byte_second = command_code_from_documentation[2:4]


        bytes_code = self.__get_bytes_code(num_of_bytes=num_of_bytes_for_command)

        command_byte_first = int.to_bytes(command_byte_first, 1, 'little')
        command_byte_second = int.to_bytes(command_byte_second, 1, 'little')
        null_byte = int.to_bytes(0, length=1, byteorder='little')

        final_command = bytes_code + command_byte_first + command_byte_second + null_byte

        command = canalystii.Message(
            remote=False,
            extended=False,
            data_len=len(final_command),
            data=final_command,
            can_id=self.__SDO_object + servo_id,
        )
        self.device.send(message=command)

    def read_error_checker(self, servo_id: int) -> canalystii.Message:
        pass
