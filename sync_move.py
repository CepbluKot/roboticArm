import servo_realisation.commands_constructor.input_output_realisation

import canalystii, time


servo_1 = servo_realisation.servo.Servo(device_id=0)
servo_2 = servo_1
create_command_servo_1 = servo_realisation.commands_constructor.input_output_realisation.ServoCommander(servo_object=servo_1)
create_command_servo_2 = servo_realisation.commands_constructor.input_output_realisation.ServoCommander(servo_object=servo_2)



def move_to_pos_sync(servo_1_target_pos=0, servo_2_target_pos=0, servo_3_target_pos=0, servo_4_target_pos=0, servo_5_target_pos=0, servo_6_target_pos=0):
    get_servo_1_pos = create_command_servo_1.create_command(command_from_documentation='60640020', is_read=1, address=0x601)
    get_servo_2_pos = create_command_servo_2.create_command(command_from_documentation='60640020', is_read=1, address=0x602)


    time.sleep(0.1)
    servo_1.send(channel=0, messages=get_servo_1_pos)
    time.sleep(0.1)
    servo_1_current_pos = 0
    while not servo_1_current_pos:
        servo_1_current_pos = servo_1.receive(channel=0)

    servo_1_current_pos = str(servo_1_current_pos[0])[-8:]

    print(servo_1_current_pos)
    servo_1_current_pos = convert_read(servo_1_current_pos)
    time.sleep(0.1)
    servo_2.send(channel=0, messages=get_servo_2_pos)
    servo_2_current_pos = 0


    while not servo_2_current_pos:
        servo_2_current_pos = servo_2.receive(channel=0)
        print(' servo_2_current_pos',servo_2_current_pos)
        


    servo_2_current_pos = str(servo_2_current_pos[0])[-8:]

    servo_2_current_pos = convert_read(servo_2_current_pos)


    servo_1_distance_delta = servo_1_target_pos - servo_1_current_pos
    servo_2_distance_delta = servo_2_target_pos - servo_2_current_pos

    read_speed_1 = create_command_servo_1.create_command(
                    command_from_documentation="60810020", is_read=1, address=0x601
                )

    read_speed_2 = create_command_servo_2.create_command(
                    command_from_documentation="60810020", is_read=1, address=0x602
                )



    target_time = 0
    if abs(servo_1_distance_delta) > abs(servo_2_distance_delta):
        time.sleep(0.1)
        servo_1.send(channel=0, messages=read_speed_1)
        servo_1_current_speed = 0
        while not servo_1_current_speed:
            servo_1_current_speed = servo_1.receive(channel=0)
            print('servo_1_current_speed', servo_1_current_speed)
        
        servo_1_current_speed = str(servo_1_current_speed[0])
        
        
        servo_1_current_speed = convert_read(servo_1_current_speed[-8:])
        print('servo_1_current_speed ',servo_1_current_speed)
        target_time = abs(servo_1_distance_delta) / servo_1_current_speed

        servo_2_target_speed = abs(servo_2_distance_delta / target_time)

        print('targ sped ', servo_2_target_speed)

        servo_2_set_speed = create_command_servo_2.create_command(command_from_documentation='60810020', address=0x602, is_write=1, write_value=servo_2_target_speed)
        time.sleep(0.1)
        servo_2.send(channel=0, messages=servo_2_set_speed)

    else:
        time.sleep(0.1)
        servo_1.send(channel=0, messages=read_speed_2)
        time.sleep(0.1)
        servo_2_current_speed = 0


        while not servo_2_current_speed:
            servo_2_current_speed = servo_1.receive(channel=0)

        servo_2_current_speed = str(servo_2_current_speed[0])[-8:]

        
        servo_2_current_speed = convert_read(servo_2_current_speed[-8:])
        print(servo_2_current_speed, 'servo_2_current_speed')
        time.sleep(0.1)

        
     
        # print(servo_1_current_speed, 'servo_2_current_speed')


        
        target_time = abs(servo_2_distance_delta) / servo_2_current_speed

        servo_1_target_speed = abs(servo_1_distance_delta / target_time)
        servo_1_set_speed = create_command_servo_1.create_command(command_from_documentation='60810020', address=0x601, is_write=1, write_value=servo_1_target_speed)
        time.sleep(0.1)
        servo_1.send(channel=0, messages=servo_1_set_speed)


    print('traget', 32768*50/360*servo_1_target_pos, 32768*50/360*servo_2_target_pos)

    pos1 = transform(write_value=int(32768*50/360*servo_1_target_pos), address=0x501)
    pos2 = transform(write_value=int(32768*50/360*servo_2_target_pos), address=0x502)
    time.sleep(0.1)
    servo_1.send(channel=0, messages=pos1)
    time.sleep(0.1)
    servo_2.send(channel=0, messages=pos2)
    time.sleep(0.1)
    
    start_move_to_target_pos = canalystii.Message(
    can_id=0x80,
    remote=False,
    extended=False,
    data_len=0,
    data=(0x80,),
)
    time.sleep(0.1)
    servo_1.send(channel=0, messages=start_move_to_target_pos)

    print(pos1, pos2)


move_to_pos_sync(servo_1_target_pos=70, servo_2_target_pos=50)
