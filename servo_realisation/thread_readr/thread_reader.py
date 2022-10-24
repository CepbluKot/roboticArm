import canalystii

import servo_realisation.commands_abstraction.commads_storage
import servo_realisation.commands_reader.input_output_realisation

from servo_realisation.commands_abstraction.commads_storage import servo_info_storage

command_reader = servo_realisation.commands_reader.input_output_realisation.create_servo_commands_reader()


def thread_reader(can_object: canalystii.CanalystDevice):

    # ONLY FOR READ
    while True:
        recieved = can_object.receive(channel=0)

        for one_recieved_command in recieved:
            one_recieved_command = command_reader.read_recieve(one_recieved_command)
            
            if one_recieved_command.decoded_data != 'success' and one_recieved_command.decoded_data != 'fail':
                # check servo
                if one_recieved_command.servo_id in servo_info_storage:
                
                    if int(one_recieved_command.id / 10) == 48:
                        servo_info_storage[one_recieved_command.servo_id].commands_info_storage["interpolation"].set_value(one_recieved_command.decoded_data)
                        servo_info_storage[one_recieved_command.servo_id].commands_info_storage["interpolation"].set_flag(1)
                        print('THREAD READ INTERPOL', one_recieved_command.servo_id, servo_info_storage[one_recieved_command.servo_id].commands_info_storage["interpolation"].value_link, servo_info_storage[one_recieved_command.servo_id].commands_info_storage["interpolation"].read_flag())

                    
                    elif one_recieved_command.command_data in servo_info_storage[one_recieved_command.servo_id].commands_info_storage:
                        

                       
                        servo_info_storage[one_recieved_command.servo_id].commands_info_storage[one_recieved_command.command_data].set_value(one_recieved_command.decoded_data)
                        servo_info_storage[one_recieved_command.servo_id].commands_info_storage[one_recieved_command.command_data].set_flag(1)
                        # print('THREAD READ ', one_recieved_command.servo_id, servo_info_storage[one_recieved_command.servo_id].commands_info_storage[one_recieved_command.command_data].value_link, servo_info_storage[one_recieved_command.servo_id].commands_info_storage[one_recieved_command.command_data].read_flag())
