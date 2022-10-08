import canalystii
import servo_realisation.servo_interface


def transform(num_of_bytes: int = None, is_read: bool = False, is_write: bool = False):
    if is_read and not is_write:
        return "0x40"

    elif not is_read and is_write:
        if num_of_bytes == 1:

            return "0x2F"

        elif num_of_bytes == 2:

            return "0x2B"

        elif num_of_bytes == 4:
            return "0x23"


class CommandConstructor:
    def __init__(self, servo_object: servo_realisation.servo_interface.ServoInterface):
        self.device_id = servo_object.device_id

    def create_command(
        self,
        command_from_documentation: str,
        is_read: bool = False,
        is_write: bool = False,
        address: int = 601,
        write_value: int = None,
    ) -> canalystii.Message:
        num_of_bytes_for_send_command = int(
            int(command_from_documentation[-2:], 16) / 8
        )
        result = ""
        result += transform(
            num_of_bytes=num_of_bytes_for_send_command,
            is_read=is_read,
            is_write=is_write,
        )[2:]

        parsed_command_bytes_first = command_from_documentation[:2]
        parsed_command_bytes_second = command_from_documentation[2:4]
        result += parsed_command_bytes_second + parsed_command_bytes_first + "00"
        command_in_hex = hex(write_value)[2:]

        num_of_iterations = 0
        while command_in_hex:
            result += command_in_hex[-2:]
            command_in_hex = command_in_hex[:-2]
            num_of_iterations += 1

        if num_of_iterations == 1:
            result += "00"

        return result
