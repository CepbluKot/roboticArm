import servo_realisation.commands_reader.commands_reader_abstraction
import servo_realisation.commands_reader.commands_reader
import servo_realisation.servo_object.input_output_realisation


def create_commands_reader(device_id=0):
    commands_reader = servo_realisation.commands_reader.commands_reader.CommandsReader()
    commands_reader_abs = servo_realisation.commands_reader.commands_reader_abstraction.CommandsReaderAbstraction(commands_reader)
    return commands_reader_abs
