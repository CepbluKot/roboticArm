import textwrap
import can
import binascii


import servo_realisation.commands_reader.commands_reader_interface
import servo_realisation.commands_reader.commands_reader_data_structures


class CommandsReader(
    servo_realisation.commands_reader.commands_reader_interface.CommandsReaderInterface
):
    def read_recieve(self, recieve: str) -> servo_realisation.commands_reader.commands_reader_data_structures.RecievedCommand:
        recieve = str(recieve)

        id = int(recieve[recieve.index('ID=') + len('ID=') + 2: recieve.index(' TS=')])
        servo_id = id % 10
        ts = int(recieve[recieve.index('TS=') + len('TS=') + 2: recieve.index(' Data=')], 16)
        data = recieve[recieve.index("Data=") + len("Data=") :]

        recieved_command = servo_realisation.commands_reader.commands_reader_data_structures.RecievedCommand(id=id, ts=ts, data=data)

        data = textwrap.wrap(recieved_command.data, 2)

        recieved_command.command_data = data[2] + data[1]
        recieved_command.servo_id = servo_id

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
            decoded_data += data[4]
            decoded_data += data[3]
            decoded_data += data[2]
            decoded_data += data[1]

            recieved_command.decoded_data = int(decoded_data, 16)

            return recieved_command

        elif num_of_bytes_to_read == "60":
            recieved_command.decoded_data = 'success'
            return recieved_command

        elif num_of_bytes_to_read == "80":
            recieved_command.decoded_data = 'fail'
            return recieved_command

        else:

            return recieved_command


# class CommandsReaderForThread(
#     servo_realisation.commands_reader.commands_reader_interface.CommandsReaderInterface
# ):
#     def read_recieve(self, recieve: str) -> servo_realisation.commands_reader.commands_reader_data_structures.RecievedCommand:
#         recieve = str(recieve)

#         id = int(recieve[recieve.index('ID=') + len('ID=') + 2: recieve.index(' TS=')])
#         ts = int(recieve[recieve.index('TS=') + len('TS=') + 2: recieve.index(' Data=')], 16)
#         data = recieve[recieve.index("Data=") + len("Data=") :]

#         recieved_command = servo_realisation.commands_reader.commands_reader_data_structures.RecievedCommand(id=id, ts=ts, data=data)

#         data = textwrap.wrap(recieved_command.data, 2)

#         recieved_command.command_data = data[2] + data[1]
        
#         num_of_bytes_to_read = data[0]

#         data = data[3:]
#         if num_of_bytes_to_read == "4f":
#             decoded_data = ""
#             decoded_data += data[1]

#             recieved_command.decoded_data = int(decoded_data, 16)
            
#             return recieved_command

#         elif num_of_bytes_to_read == "4b":
#             decoded_data = ""
#             decoded_data += data[2]
#             decoded_data += data[1]
            
#             recieved_command.decoded_data = int(decoded_data, 16)
#             return recieved_command

#         elif num_of_bytes_to_read == "43":
#             decoded_data = ""
#             decoded_data += data[4]
#             decoded_data += data[3]
#             decoded_data += data[2]
#             decoded_data += data[1]

#             recieved_command.decoded_data = int(decoded_data, 16)
#             return recieved_command

#         elif num_of_bytes_to_read == "60":
#             return recieved_command

#         else:
#             return recieved_command



class CommandsReaderCan(
    servo_realisation.commands_reader.commands_reader_interface.CommandsReaderInterface
):
    def read_recieve(self, recieve: can.Message) -> servo_realisation.commands_reader.commands_reader_data_structures.RecievedCommand:
        id = recieve.arbitration_id
        ts = recieve.timestamp
        data = binascii.hexlify(recieve.data).decode()

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
            decoded_data += data[4]
            decoded_data += data[3]
            decoded_data += data[2]
            decoded_data += data[1]

            recieved_command.decoded_data = int(decoded_data, 16)
            return recieved_command

        elif num_of_bytes_to_read == "60":
            return recieved_command

        else:
            return recieved_command

