import canalystii
import servo_realisation.control_objects.servo_interface
import servo_realisation.commands_constructor.commands_constructor_interface


def get_bytes_code(num_of_bytes: int = None, is_read: bool = False):
    if is_read:
        return "0x40"

    else:
        if num_of_bytes == 1:
            return "0x2F"

        elif num_of_bytes == 2:
            return "0x2B"

        elif num_of_bytes == 4:
            return "0x23"


class CommandConstructor(servo_realisation.commands_constructor.commands_constructor_interface.CommandConstructorInterface):
    def __init__(
        self,
        servo_object: servo_realisation.control_objects.servo_interface.ServoInterface,
    ):
        self.servo = servo_object

    def general_move_command(self):
        final_command = canalystii.Message(
            remote=False, extended=False, data_len=0, can_id=0x80
        )
        return final_command

    def create_command(
        self, address: int, command_from_documentation: str, write_value: int = None
    ) -> canalystii.Message:
        result = []
        num_of_bytes_for_command = int(int(command_from_documentation[-2:], 16) / 8)

        command_byte_first = command_from_documentation[:2]
        command_byte_second = command_from_documentation[2:4]

        if write_value:

            result.append(get_bytes_code(num_of_bytes=num_of_bytes_for_command))

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

            final_command = canalystii.Message(
                remote=False,
                extended=False,
                data_len=len(convert_to_hex),
                data=convert_to_hex,
                can_id=address + self.servo.servo_id,
            )

            return final_command

        else:
            result.append(
                get_bytes_code(num_of_bytes=num_of_bytes_for_command, is_read=True)
            )
            result.append("0x" + command_byte_second)
            result.append("0x" + command_byte_first)
            result.append("0x00")

            convert_to_hex = ()
            for element in result:
                convert_to_hex += (int(element, 0),)

            final_command = canalystii.Message(
                remote=False,
                extended=False,
                data_len=len(convert_to_hex),
                data=convert_to_hex,
                can_id=address + self.servo.servo_id,
            )
            return final_command
