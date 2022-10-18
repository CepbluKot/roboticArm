import textwrap
import servo_realisation.commands_reader.commands_reader_interface


class CommandsReader(
    servo_realisation.commands_reader.commands_reader_interface.CommandsReaderInterface
):
    def read_recieve(self, recieve: str):
        recieve = str(recieve[0])
        recieve = recieve[recieve.index("Data=") + len("Data=") :]
        recieve = textwrap.wrap(recieve, 2)

        command_data = recieve[2] + recieve[1]
        num_of_bytes_to_read = recieve[0]

        recieve = recieve[3:]

        if num_of_bytes_to_read == "4f":
            data = ""
            data += recieve[1]

            return int(data, 16), command_data

        elif num_of_bytes_to_read == "4b":
            data = ""
            data += recieve[2]
            data += recieve[1]
            return int(data, 16), command_data

        elif num_of_bytes_to_read == "43":
            data = ""
            data += recieve[4]
            data += recieve[3]
            data += recieve[2]
            data += recieve[1]
            return int(data, 16), command_data
