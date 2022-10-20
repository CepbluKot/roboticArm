import servo_realisation.commands_reader.commands_reader_abstraction
import servo_realisation.commands_reader.commands_reader


def create_servo_commands_reader():
    commands_reader = servo_realisation.commands_reader.commands_reader.CommandsReader()
    commands_reader_abs = servo_realisation.commands_reader.commands_reader_abstraction.CommandsReaderAbstraction(
        commands_reader
    )
    return commands_reader_abs


def create_servo_commands_reader_can():
    commands_reader = servo_realisation.commands_reader.commands_reader.CommandsReaderCan()
    commands_reader_abs = servo_realisation.commands_reader.commands_reader_abstraction.CommandsReaderAbstraction(
        commands_reader
    )
    return commands_reader_abs
