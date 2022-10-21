import threading
import can
import time


import servo_realisation.commands_constructor.input_output_realisation
import servo_realisation.commands_reader.input_output_realisation
import servo_realisation.control_objects.input_output_realisation
import servo_realisation.commands_constructor.commands_constructor_interface
import servo_realisation.control_objects.servo_interface
import servo_realisation.commands_abstraction.commands

import servo_realisation.commands_abstraction.input_output_realisation


import servo_realisation.commands_reader.input_output_realisation

import servo_realisation.thread_readr.thread_reader

import servo_realisation.commands_abstraction.commads_storage

# servo_1 = servo_realisation.control_objects.input_output_realisation.create_servo_object_can(
#     servo_id=1
# )
# servo_2 = servo_realisation.control_objects.input_output_realisation.create_servo_object_can(
#     servo_id=2
# )
# servo_3 = servo_realisation.control_objects.input_output_realisation.create_servo_object_can(
#     servo_id=3
# )
# servo_4 = servo_realisation.control_objects.input_output_realisation.create_servo_object_can(
#     servo_id=4
# )
# servo_5 = servo_realisation.control_objects.input_output_realisation.create_servo_object_can(
#     servo_id=5
# )
# servo_6 = servo_realisation.control_objects.input_output_realisation.create_servo_object_can(
#     servo_id=6
# )


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

# servo_1_abs = servo_realisation.commands_abstraction.input_output_realisation.create_servo_commands_abstraction_can(
#     servo_object=servo_1
# )
# servo_2_abs = servo_realisation.commands_abstraction.input_output_realisation.create_servo_commands_abstraction_can(
#     servo_object=servo_2
# )
# servo_3_abs = servo_realisation.commands_abstraction.input_output_realisation.create_servo_commands_abstraction_can(
#     servo_object=servo_3
# )
# servo_4_abs = servo_realisation.commands_abstraction.input_output_realisation.create_servo_commands_abstraction_can(
#     servo_object=servo_4
# )
# servo_5_abs = servo_realisation.commands_abstraction.input_output_realisation.create_servo_commands_abstraction_can(
#     servo_object=servo_5
# )
# servo_6_abs = servo_realisation.commands_abstraction.input_output_realisation.create_servo_commands_abstraction_can(
#     servo_object=servo_6
# )

servo_1_abs = servo_realisation.commands_abstraction.input_output_realisation.create_servo_commands_abstraction(
    servo_object=servo_1
)
servo_2_abs = servo_realisation.commands_abstraction.input_output_realisation.create_servo_commands_abstraction(
    servo_object=servo_2
)
servo_3_abs = servo_realisation.commands_abstraction.input_output_realisation.create_servo_commands_abstraction(
    servo_object=servo_3
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


def thread_operations():
    pass
# todo



def move_to_pos_sync(servo_1_target_pos=0, servo_2_target_pos=0, servo_3_target_pos=0, servo_4_target_pos=0, servo_5_target_pos=0, servo_6_target_pos=0):
    spd1 = 100
    spd2 = 100
    servo_1_abs.set_speed(value=spd1)
    servo_2_abs.set_speed(value=spd2)
    # getting SPEED
     
    servo_1_current_speed = servo_1_abs.read_speed().decoded_data
    servo_2_current_speed = servo_2_abs.read_speed().decoded_data

    # getting POSITION
    servo_1_current_pos = servo_1_abs.read_pos().decoded_data
    servo_2_current_pos = servo_2_abs.read_pos().decoded_data


    if servo_1_current_pos >= 42949672900:
        servo_1_current_pos = 0

    if servo_2_current_pos >= 42949672900:
        servo_2_current_pos = 0

    

    servo_1_target_pos = int(32768 * 50 /360 * servo_1_target_pos)
    servo_2_target_pos = int(32768 * 50 /360 * servo_2_target_pos)
   
    servo_1_distance_delta = abs(servo_1_target_pos - servo_1_current_pos)
    servo_2_distance_delta = abs(servo_2_target_pos - servo_2_current_pos)


    if not servo_1_current_speed:
        n =spd1
        servo_1_abs.set_speed(value=n)
        servo_1_current_speed = n

    if not servo_2_current_speed:
        n = spd2
        servo_2_abs.set_speed(value=n)
        servo_2_current_speed = n

    target_time = 0
    servo_1_target_speed = servo_1_current_speed
    servo_2_target_speed = servo_2_current_speed


    if abs(servo_1_distance_delta) >= abs(servo_2_distance_delta):
        print("PRIORITY - SERVO 1")
        target_time = abs(servo_1_distance_delta) / servo_1_current_speed
        print('CALC TARG TIME: ', abs(servo_1_distance_delta), ' /', servo_1_current_speed, ' =', target_time)
        if target_time:
            # print(target_time)
            servo_2_target_speed = abs(servo_2_distance_delta / target_time)

            if not servo_2_target_speed:
                servo_2_target_speed = 10

            servo_2_abs.set_speed(value=servo_2_target_speed)
        else:
            servo_2_abs.set_speed(value=0)
        

    else:
        print("PRIORITY - SERVO 2")
        target_time = abs(servo_2_distance_delta) / servo_2_current_speed
        print('CALC TARG TIME: ', abs(servo_2_distance_delta), ' /', servo_2_current_speed, ' =', target_time)
        if target_time:
            servo_1_target_speed = abs(servo_1_distance_delta / target_time)
            
            if not servo_1_target_speed:
                servo_1_target_speed = 10

            servo_1_abs.set_speed(value=servo_1_target_speed)
        else:
            servo_1_abs.set_speed(value=0)

       

    print('servo_1_current_pos', servo_1_current_pos, 'servo_1_target_pos', servo_1_target_pos)
    print('servo_2_current_pos', servo_2_current_pos, 'servo_2_target_pos', servo_2_target_pos)
    
    
    servo_1_abs.set_pos(value=servo_1_target_pos)
    servo_2_abs.set_pos(value=servo_2_target_pos)

    servo_3_abs.set_pos(value=0)
    servo_4_abs.set_pos(value=0)
    servo_5_abs.set_pos(value=0)
    servo_6_abs.set_pos(value=0)

    print('servo_1_speed', servo_1_target_speed, 'servo_2_speed', servo_2_target_speed)

    
    servo_1_abs.general_move_command()

    while servo_1_abs.read_cur_speed().decoded_data and servo_2_abs.read_cur_speed().decoded_data:
        pass

# servo_1_abs.set_mode(value=1)
# servo_2_abs.set_mode(value=1)



def reader():
    print('start read')
    start_time = 0
    while True:
        tem = time.time()
        if tem - start_time >= 1:
            print('1 sec passed')
            start_time = tem
        
        read_1 = servo_1.receive(channel=0)
        # read_1 = servo_1_abs.decode_everyth(read_1)
        # if read_1.arbitration_id == 0x581:
            # tiem = time.time()
            # print(  "!!!      read ", read_1)
            # recv_time = tiem
        print(read_1)
        # print(read_1.id, read_1.ts)

def test_writer():
    print('start write')
    # start_time = time.time()
    
    a = [servo_1_abs, servo_2_abs, servo_3_abs, servo_4_abs, servo_5_abs, servo_6_abs, ]
    while True:
        # if time.time() - start_time >= 0.1:

            for x in a:
                x.read_speed()
                print('sent', x.servo.servo_id)

            # servo_1_abs.read_speed()
            # start_time = time.time()

def writer():
    # while 1:
        a, b = input('input').split(' ')
        # print(int(a), int(b))
        move_to_pos_sync(servo_1_target_pos=int(a), servo_2_target_pos=int(b))


def write_test_2():
    # while 1:
        print('sent sped')

        servo_1_abs.read_speed()
        time.sleep(1)


        print('sent mod')

        servo_1_abs.read_mode()
        time.sleep(1)

        print('sent pos')

        servo_1_abs.read_pos()
        time.sleep(1)






# def write_test_3():
#     while 1:
#         a = [servo_1_abs,  servo_2_abs,servo_3_abs,servo_4_abs,servo_5_abs,servo_6_abs,]
#         for x in a:
#             x.set_speed(20)



redr = servo_realisation.commands_reader.input_output_realisation.create_servo_commands_reader()
servo_info_storage = servo_realisation.commands_abstraction.commads_storage.servo_info_storage

def read_test_2():
    while 1:
        


        # res2 = servo_1_abs.decode_everyth(res)
        
        res = servo_1.receive(0)
        res2 = []
        for elem in res:
            elem = redr.read_recieve(recieve=elem)
            res2.append(elem)



# writer()

# read_thread = threading.Thread(target=read_test_2)
# write_thread = threading.Thread(target=write_test_2)
# write_thread.start()
# read_thread.start()


can_obj = servo_realisation.control_objects.input_output_realisation.get_can_object()

# write_test_2()

# write_test_2()

# write_test_2()
write_thread = threading.Thread(target=write_test_2)
read_thread = threading.Thread(target=servo_realisation.thread_readr.thread_reader.thread_reader, args=(can_obj, ))
write_thread.start()
read_thread.start()


# while 1:
#     a = [servo_1_abs, servo_2_abs, servo_3_abs, servo_4_abs, servo_5_abs, servo_6_abs, ]
#     for x in a:

#         x.read_speed()
#     print(servo_1.receive(0))


# while 1:
#     fir = servo_3_abs.read_pos()
#     sec = servo_4_abs.read_pos()
#     print('fir', fir.decoded_data, 'sec', sec.decoded_data)

# pos = 0
# while 1: 
    
#     pos = servo_6_abs.read_pos().decoded_data
#     print('pos', pos)

# servo_6_abs.general_move_command()




# servo_1_abs.set_zero_pos()
# servo_2_abs.set_zero_pos()
# servo_3_abs.set_zero_pos()
# servo_4_abs.set_zero_pos()
# servo_5_abs.set_zero_pos()
# servo_6_abs.set_zero_pos()

# servo_1_abs.set_speed(30)
# servo_2_abs.set_speed(30)
# servo_3_abs.set_speed(30)
# servo_4_abs.set_speed(30)
# servo_5_abs.set_speed(30)
# servo_6_abs.set_speed(30)

# servo_1_abs.save_settings()
# servo_2_abs.save_settings()
# servo_3_abs.save_settings()
# servo_4_abs.save_settings()
# servo_5_abs.save_settings()
# servo_6_abs.save_settings()


# servo_1_abs.set_mode(1)
# servo_2_abs.set_mode(1)
# servo_3_abs.set_mode(1)
# servo_4_abs.set_mode(1)
# servo_5_abs.set_mode(1)
# servo_6_abs.set_mode(1)


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
