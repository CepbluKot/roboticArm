import servo_realisation.commands_constructor.input_output_realisation
import servo_realisation.commands_reader.input_output_realisation
import servo_realisation.control_objects.input_output_realisation
import servo_realisation.commands_constructor.commands_constructor_interface
import servo_realisation.control_objects.servo_interface


import servo_realisation.commands_abstraction.input_output_realisation


servo_1 = servo_realisation.control_objects.input_output_realisation.create_servo_object(
    servo_id=1
)
servo_2 = servo_realisation.control_objects.input_output_realisation.create_servo_object(
    servo_id=2
)
servo_3 = servo_realisation.control_objects.input_output_realisation.create_servo_object(
    servo_id=3
)
servo_4 = servo_realisation.control_objects.input_output_realisation.create_servo_object(
    servo_id=4
)
servo_5 = servo_realisation.control_objects.input_output_realisation.create_servo_object(
    servo_id=5
)
servo_6 = servo_realisation.control_objects.input_output_realisation.create_servo_object(
    servo_id=6
)


# reader = (
#     servo_realisation.commands_reader.input_output_realisation.create_servo_commands_reader()
# )


servo_1_abs = servo_realisation.commands_abstraction.input_output_realisation.create_servo_commands_abstraction(
    servo_object=servo_1
)
servo_2_abs = servo_realisation.commands_abstraction.input_output_realisation.create_servo_commands_abstraction(
    servo_object=servo_2
)
servo_3_abs = servo_realisation.commands_abstraction.input_output_realisation.create_servo_commands_abstraction(
    servo_object=servo_2
)
servo_4_abs = servo_realisation.commands_abstraction.input_output_realisation.create_servo_commands_abstraction(
    servo_object=servo_4
)
servo_5_abs = servo_realisation.commands_abstraction.input_output_realisation.create_servo_commands_abstraction(
    servo_object=servo_5
)
servo_6_abs = servo_realisation.commands_abstraction.input_output_realisation.create_servo_commands_abstraction(
    servo_object=servo_6
)


def servo_move_to_pos_sync(servo_constructor: servo_realisation.commands_constructor.commands_constructor_interface.CommandConstructorInterface, servo_object: servo_realisation.control_objects.servo_interface.ServoInterface, target_time: int, target_pos: int):
    se = servo_constructor.create_command(command_from_documentation='60640020', address=0x600)
    servo_get_speed_command = servo_constructor.create_command(command_from_documentation='60810020', address=0x600)
    
    servo_object.send(channel=0, messages=servo_get_speed_command)    
    servo_current_speed = reader.read_recieve(servo_object.receive(channel=0))

    servo_object.send(channel=0, messages=servo_get_pos_command)    
    servo_current_pos = reader.read_recieve(servo_object.receive(channel=0))

    servo_target_speed = 0




def move_to_pos_sync(servo_1_target_pos=0, servo_2_target_pos=0, servo_3_target_pos=0, servo_4_target_pos=0, servo_5_target_pos=0, servo_6_target_pos=0):
    

    # getting SPEED
     
    servo_1_current_speed = servo_1_abs.read_speed()
    servo_2_current_speed = servo_2_abs.read_speed()

    # getting POSITION
    servo_1_current_pos = servo_1_abs.read_pos()
    servo_2_current_pos = servo_2_abs.read_pos()


    # print('servo_1_current_speed', servo_1_current_speed)
    # print('servo_2_current_speed', servo_2_current_speed)
    # print('servo_1_current_pos', servo_1_current_pos)
    # print('servo_2_current_pos', servo_2_current_pos)

    servo_1_target_pos = int(32768 * 50 /360 * servo_1_target_pos)
    servo_2_target_pos = int(32768 * 50 /360 * servo_2_target_pos)
   
    servo_1_distance_delta = abs(servo_1_target_pos - servo_1_current_pos)
    servo_2_distance_delta = abs(servo_2_target_pos - servo_2_current_pos)


    if not servo_1_current_speed:
        servo_1_abs.set_speed(value=20)

    if not servo_2_current_speed:
        servo_2_abs.set_speed(value=20)


    target_time = 0
    if abs(servo_1_distance_delta) > abs(servo_2_distance_delta):
        target_time = abs(servo_1_distance_delta) / servo_1_current_speed

        servo_2_target_speed = abs(servo_2_distance_delta / target_time)

        servo_2_abs.set_speed(value=servo_2_target_speed)

        print('servo_1_current_speed', servo_1_current_speed)
        print('servo_2_target_speed', servo_2_target_speed)

    else:
        target_time = abs(servo_2_distance_delta) / servo_2_current_speed
        servo_1_target_speed = abs(servo_1_distance_delta / target_time)
        
        servo_1_abs.set_speed(value=servo_1_target_speed)

        print('servo_1_target_speed', servo_1_target_speed)
        print('servo_2_speed', servo_2_current_speed)


    servo_1_abs.set_pos(value=32768*50/360*servo_1_target_pos)
    servo_2_abs.set_pos(value=32768*50/360*servo_2_target_pos)

    servo_1_abs.general_move_command()


# move_to_pos_sync(servo_1_target_pos=30, servo_2_target_pos=30)




# servo_1_get_pos_command = servo_1_constructor.create_command(command_from_documentation='60640020', address=0x600)
# servo_2_get_pos_command = servo_2_constructor.create_command(command_from_documentation='60640020', address=0x600)

# servo_1_get_speed_command = servo_1_constructor.create_command(command_from_documentation='60810020', address=0x600)
# servo_2_get_speed_command = servo_2_constructor.create_command(command_from_documentation='60810020', address=0x600)


# # getting SPEED
# servo_1.send(channel=0, messages=servo_1_get_speed_command)    
# servo_1_current_speed = reader.read_recieve(servo_1.receive(channel=0))


# servo_2.send(channel=0, messages=servo_2_get_speed_command)
# servo_2_current_speed = reader.read_recieve(servo_2.receive(channel=0))

# # getting POSITION
# servo_1.send(channel=0, messages=servo_1_get_pos_command)    
# servo_1_current_pos = reader.read_recieve(servo_1.receive(channel=0))


# servo_2.send(channel=0, messages=servo_2_get_pos_command)
# servo_2_current_pos = reader.read_recieve(servo_2.receive(channel=0))

# print('servo_1_current_speed', servo_1_current_speed)
# print('servo_2_current_speed', servo_2_current_speed)
# print('servo_1_current_pos', servo_1_current_pos)
# print('servo_2_current_pos', servo_2_current_pos)


# save = ser_abs.create_command(
#                 command_from_documentation="26140010", is_write=1, address=0x601, write_value=1
#             )





# abs = servo_realisation.commands_abstraction.input_output_realisation.create_servo_commands_abstraction(servo_object=servo_3)
# abs.set_mode(1)
# abs.general_move_command()



# check_mode = servo_1_constructor.create_command(
#             command_from_documentation="60600008", address=0x600
#         )

# read_speed_1 = servo_1_constructor.create_command(address=0x600, command_from_documentation='60810020')


# while 1:
#     servo_1.send(channel=0, messages=read_speed_1)
#     read = servo_1.receive(0)
#     print(read)
