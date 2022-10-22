import threading

import servo_realisation.commands_abstraction.commads_storage
import servo_realisation.commands_abstraction.input_output_realisation
import servo_realisation.control_objects.input_output_realisation
import servo_realisation.thread_readr.thread_reader


storage = servo_realisation.commands_abstraction.commads_storage.servo_info_storage

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


servo_1_thread_controller = servo_realisation.commands_abstraction.input_output_realisation.create_servo_commands_abstraction(servo_object=servo_1)
servo_2_thread_controller = servo_realisation.commands_abstraction.input_output_realisation.create_servo_commands_abstraction(servo_object=servo_2)
servo_3_thread_controller = servo_realisation.commands_abstraction.input_output_realisation.create_servo_commands_abstraction(servo_object=servo_3)
servo_4_thread_controller = servo_realisation.commands_abstraction.input_output_realisation.create_servo_commands_abstraction(servo_object=servo_4)
servo_5_thread_controller = servo_realisation.commands_abstraction.input_output_realisation.create_servo_commands_abstraction(servo_object=servo_5)
servo_6_thread_controller = servo_realisation.commands_abstraction.input_output_realisation.create_servo_commands_abstraction(servo_object=servo_6)


# # print(storage)



can_obj = servo_realisation.control_objects.input_output_realisation.get_can_object()
read_thread = threading.Thread(target=servo_realisation.thread_readr.thread_reader.thread_reader, args=(can_obj, ), daemon=True)
read_thread.start()


def move_to_pos_sync(servo_1_target_pos=0, servo_2_target_pos=0, servo_3_target_pos=0, servo_4_target_pos=0, servo_5_target_pos=0, servo_6_target_pos=0):
    spd1 = 100
    spd2 = 100
    servo_1_thread_controller.set_speed(value=spd1)
    servo_2_thread_controller.set_speed(value=spd2)

    # getting SPEED
     
    servo_1_current_speed = servo_1_thread_controller.read_speed()
    servo_2_current_speed = servo_2_thread_controller.read_speed()

    # getting POSITION
   
    servo_1_current_pos = servo_1_thread_controller.read_pos()
    servo_2_current_pos = servo_2_thread_controller.read_pos()

    

    if servo_1_current_pos >= 4294958900:
        servo_1_current_pos = 0

    if servo_2_current_pos >= 4294958900:
        servo_2_current_pos = 0

    

    servo_1_target_pos = int(32768 * 50 /360 * servo_1_target_pos)
    servo_2_target_pos = int(32768 * 50 /360 * servo_2_target_pos)
   
    servo_1_distance_delta = abs(servo_1_target_pos - servo_1_current_pos)
    servo_2_distance_delta = abs(servo_2_target_pos - servo_2_current_pos)


    if not servo_1_current_speed:
        n =spd1
        servo_1_thread_controller.set_speed(value=n)
        servo_1_current_speed = n

    if not servo_2_current_speed:
        n = spd2
        servo_2_thread_controller.set_speed(value=n)
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

            servo_2_thread_controller.set_speed(value=servo_2_target_speed)
        else:
            servo_2_thread_controller.set_speed(value=0)
        

    else:
        print("PRIORITY - SERVO 2")
        target_time = abs(servo_2_distance_delta) / servo_2_current_speed
        print('CALC TARG TIME: ', abs(servo_2_distance_delta), ' /', servo_2_current_speed, ' =', target_time)
        if target_time:
            servo_1_target_speed = abs(servo_1_distance_delta / target_time)
            
            if not servo_1_target_speed:
                servo_1_target_speed = 10

            servo_2_thread_controller.set_speed(value=servo_1_target_speed)
        else:
            servo_2_thread_controller.set_speed(value=0)

       

    # print('servo_1_current_pos', servo_1_current_pos, 'servo_1_target_pos', servo_1_target_pos)
    # print('servo_2_current_pos', servo_2_current_pos, 'servo_2_target_pos', servo_2_target_pos)
    
    
    servo_1_thread_controller.set_pos(value=servo_1_target_pos)
    servo_2_thread_controller.set_pos(value=servo_2_target_pos)

    servo_3_thread_controller.set_pos(value=0)
    servo_4_thread_controller.set_pos(value=0)
    servo_5_thread_controller.set_pos(value=0)
    servo_6_thread_controller.set_pos(value=0)

    print('servo_1_speed', servo_1_target_speed, 'servo_2_speed', servo_2_target_speed)

    
    servo_1_thread_controller.general_move_command()

# servo_1_thread_controller.set_mode(1)
# servo_2_thread_controller.set_mode(1)

# servo_3_thread_controller.set_mode(1)
# servo_4_thread_controller.set_mode(1)
# servo_5_thread_controller.set_mode(1)
# servo_6_thread_controller.set_mode(1)


def writer_thr():
    while 1:
        a, b = input('inpot').split()
        # a, b = 1, 1
        move_to_pos_sync(servo_1_target_pos=int(a), servo_2_target_pos=int(b))
writer_thr()
# wr_thr = threading.Thread(target=writer_thr)
# wr_thr.start()
