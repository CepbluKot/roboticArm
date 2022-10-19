import textwrap
import servo_realisation.commands_reader.commands_reader_interface
import servo_realisation.commands_reader.commands_reader_data_structures


class CommandsReader(
    servo_realisation.commands_reader.commands_reader_interface.CommandsReaderInterface
):
    def read_recieve(self, recieve: str) -> servo_realisation.commands_reader.commands_reader_data_structures.RecievedCommand:
        recieve = str(recieve[0])

        id = int(recieve[recieve.index('ID=') + len('ID=') + 2: recieve.index(' TS=')])
        ts = recieve[recieve.index('TS=') + len('TS=') + 2: recieve.index(' Data=')]
        data = recieve[recieve.index("Data=") + len("Data=") :]

        recieved_command = servo_realisation.commands_reader.commands_reader_data_structures.RecievedCommand(id=id, ts=ts, data=data)

        data = textwrap.wrap(recieved_command.data, 2)

        recieved_command.command_data = data[2] + data[1]
        
        num_of_bytes_to_read = data[0]

        data = data[3:]
        if num_of_bytes_to_read == "4f":
            decoded_data = ""
            decoded_data += data[1]

            recieved_command.decoded_data = int(decoded_data, 16)
            
            return recieved_command

        elif num_of_bytes_to_read == "4b":
            decoded_data = ""
            decoded_data += data[2]
            decoded_data += data[1]
            
            recieved_command.decoded_data = int(decoded_data, 16)
            return recieved_command

        elif num_of_bytes_to_read == "43":
            decoded_data = ""
            decoded_data += recieve[4]
            decoded_data += recieve[3]
            decoded_data += recieve[2]
            decoded_data += recieve[1]

            recieved_command.decoded_data = int(decoded_data, 16)
            return recieved_command

        else:
            recieved_command = servo_realisation.commands_reader.commands_reader_data_structures.RecievedCommand(id=-1, ts="", data="")
            return recieved_command
