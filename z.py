import canalystii, ctypes, time

from servo_realisation.hardware_interface import USB_CAN
from servo_realisation.protocol_interface import CanOpen301


def __get_bytes_code_old(num_of_bytes: int = None, is_read: bool = False) -> str:
    if is_read:
        return "0x40"

    else:
        if num_of_bytes == 1:
            return "0x2F"

        elif num_of_bytes == 2:
            return "0x2B"

        elif num_of_bytes == 4:
            return "0x23"

        else:
            print("error - bytes_code_func - reached max num of bytes to send")


def __get_bytes_code_new(num_of_bytes: int = None, is_read: bool = False) -> str:
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


def __parse_send(
    address: str,
    servo_id: str,
    write_value=None,
    command_code_from_documentation: str = None,
) -> canalystii.Message:
    result = []

    if write_value and not command_code_from_documentation:
        write_value = round(write_value)

        write_value = hex(write_value)[2:]

        num_of_iterations = 0

        while write_value:
            result.append("0x" + write_value[-2:])
            write_value = write_value[:-2]
            num_of_iterations += 1

        while 4 != num_of_iterations:
            result.append("0x00")
            num_of_iterations += 1

        convert_to_hex = ()

        for element in result:
            convert_to_hex += (int(element, 0),)

        output_command = canalystii.Message(
            remote=False,
            extended=False,
            data_len=len(convert_to_hex),
            data=convert_to_hex,
            can_id=address + servo_id,
        )
        print("old parser ", convert_to_hex, output_command)

    elif write_value:
        num_of_bytes_for_command = int(
            int(command_code_from_documentation[-2:], 16) / 8
        )

        command_byte_first = command_code_from_documentation[:2]
        command_byte_second = command_code_from_documentation[2:4]

        write_value = round(write_value)

        result.append(__get_bytes_code_old(num_of_bytes=num_of_bytes_for_command))
        result.append("0x" + command_byte_second)
        result.append("0x" + command_byte_first)
        result.append("0x00")

        write_value = hex(write_value)[2:]

        num_of_iterations = 0

        while write_value:
            result.append("0x" + write_value[-2:])
            write_value = write_value[:-2]
            num_of_iterations += 1

        while num_of_bytes_for_command != num_of_iterations:
            result.append("0x00")
            num_of_iterations += 1

        convert_to_hex = ()

        for element in result:

            convert_to_hex += (int(element, 0),)

        output_command = canalystii.Message(
            remote=False,
            extended=False,
            data_len=len(convert_to_hex),
            data=convert_to_hex,
            can_id=address + servo_id,
        )
        print("old parser ", convert_to_hex, output_command)

    else:

        num_of_bytes_for_command = int(
            int(command_code_from_documentation[-2:], 16) / 8
        )

        command_byte_first = command_code_from_documentation[:2]
        command_byte_second = command_code_from_documentation[2:4]

        result.append(
            __get_bytes_code_old(num_of_bytes=num_of_bytes_for_command, is_read=True)
        )
        result.append("0x" + command_byte_second)
        result.append("0x" + command_byte_first)
        result.append("0x00")

        convert_to_hex = ()
        for element in result:
            convert_to_hex += (int(element, 0),)

        output_command = canalystii.Message(
            remote=False,
            extended=False,
            data_len=len(convert_to_hex),
            data=convert_to_hex,
            can_id=address + servo_id,
        )

        print("old parser ", convert_to_hex, output_command)


def __parse_send_new(
    address: int,
    servo_id: int,
    write_value: int = None,
    command_code_from_documentation: str = None,
) -> canalystii.Message:

    if write_value and not command_code_from_documentation:
        write_value = (round(write_value),)

        output_command = canalystii.Message(
            remote=False,
            extended=False,
            data_len=4,
            data=write_value,
            can_id=address + servo_id,
        )
        print("new parser ", write_value, output_command)

    elif write_value:
        num_of_bytes_for_command = (
            ((command_code_from_documentation % 100) // 10 * 16)
            + ((command_code_from_documentation % 100) % 10 * 1)
        ) // 8
        command_byte_first = command_code_from_documentation // 1000000
        command_byte_first = command_byte_first % 10 * 1 + command_byte_first // 10 * 16

        command_byte_second = (
            command_code_from_documentation // 10000 * 10000
            - command_code_from_documentation // 1000000 * 1000000
        ) // 10000
        command_byte_second = (
            command_byte_second % 10 * 1 + command_byte_second // 10 * 16
        )

        write_value = round(write_value)

        bytes_code = __get_bytes_code_new(num_of_bytes=num_of_bytes_for_command)

        list_of_bytes = (
            bytes_code,
            command_byte_second,
            command_byte_first,
            0,
            write_value,
        )

        output_command = canalystii.Message(
            remote=False,
            extended=False,
            data_len=len(list_of_bytes),
            data=list_of_bytes,
            can_id=address + servo_id,
        )
        print("new parser ", list_of_bytes, output_command)

    else:
        num_of_bytes_for_command = (
            ((command_code_from_documentation % 100) // 10 * 16)
            + ((command_code_from_documentation % 100) % 10 * 1)
        ) // 8
        command_byte_first = command_code_from_documentation // 1000000
        command_byte_first = command_byte_first % 10 * 1 + command_byte_first // 10 * 16

        command_byte_second = (
            command_code_from_documentation // 10000 * 10000
            - command_code_from_documentation // 1000000 * 1000000
        ) // 10000
        command_byte_second = (
            command_byte_second % 10 * 1 + command_byte_second // 10 * 16
        )

        bytes_code = __get_bytes_code_new(
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

        print("new parser ", final_command)


# __parse_send(address=0x500, servo_id=1, write_value=15)
# __parse_send_new(address=0x500, servo_id=1, write_value=15)


def on_msg(msg: canalystii.protocol.Message):
    return protoc.parse_recieve(msg)


def smth(a,):
    pass


interfec = USB_CAN.USB_CAN(0, 1000000, on_msg)
protoc = CanOpen301.CanOpen301(interfec, smth, smth, smth, smth, smth)
# interfec.open_connection()

while 1:
    protoc.send_speed(1, 22)
    time.sleep(1)
    protoc.read_speed(1)
    # time.sleep(1)
