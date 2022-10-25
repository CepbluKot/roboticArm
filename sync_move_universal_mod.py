from typing import Dict
import time
import threading
import servo_realisation.commands_abstraction.commands
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


# servo_1_thread_controller.set_zero_pos()
# servo_2_thread_controller.set_zero_pos()
# servo_3_thread_controller.set_zero_pos()
# servo_4_thread_controller.set_zero_pos()
# servo_5_thread_controller.set_zero_pos()
# servo_6_thread_controller.set_zero_pos()


class AxisData:
    def __init__(self, max_value, current_speed, target_speed, current_pos, target_pos, distance_delta, servo_object_thread: servo_realisation.commands_abstraction.commands.ControlServoThread, acceleration: int) -> None:
        self.current_speed = current_speed
        self.target_speed = target_speed
        self.current_pos = current_pos
        self.target_pos = target_pos
        self.distance_delta = distance_delta
        self.servo_object_thread = servo_object_thread
        self.acceleration = acceleration
        self.max_value = max_value

    
def move_to_pos_sync(servo_1_target_pos=0, servo_2_target_pos=0, servo_3_target_pos=0, servo_4_target_pos=0, servo_5_target_pos=0, servo_6_target_pos=0):
    default_speed = 100
    default_acceleration = 20

    axis_1_max_value = 360
    axis_2_max_value = 100
    axis_3_max_value = 120
    axis_4_max_value = 180
    axis_5_max_value = 180
    axis_6_max_value = 720


    axis_1_max_value = int(32768 * 50 /360 * axis_1_max_value)
    axis_2_max_value = int(32768 * 50 /360 * axis_2_max_value)
    axis_3_max_value = int(32768 * 50 /360 * axis_3_max_value)
    axis_4_max_value = int(32768 * 50 /360 * axis_4_max_value)
    axis_5_max_value = int(32768 * 50 /360 * axis_5_max_value)
    axis_6_max_value = int(32768 * 50 /360 * axis_6_max_value)

    
    axis_data: Dict[int, AxisData] = {
        1: AxisData(max_value=axis_1_max_value, acceleration=default_acceleration, current_speed=default_speed, target_speed=0, current_pos=0, target_pos=int(32768 * 50 /360 * servo_1_target_pos), distance_delta=0, servo_object_thread=servo_1_thread_controller),
        2: AxisData(max_value=axis_2_max_value, acceleration=default_acceleration, current_speed=default_speed, target_speed=0, current_pos=0, target_pos=int(32768 * 50 /360 * servo_2_target_pos), distance_delta=0, servo_object_thread=servo_2_thread_controller),
        3: AxisData(max_value=axis_3_max_value, acceleration=default_acceleration, current_speed=default_speed, target_speed=0, current_pos=0, target_pos=int(32768 * 50 /360 * servo_3_target_pos), distance_delta=0, servo_object_thread=servo_3_thread_controller),
        # 4: AxisData(max_value=axis_4_max_value, acceleration=default_acceleration, current_speed=default_speed, target_speed=0, current_pos=0, target_pos=int(32768 * 50 /360 * servo_4_target_pos), distance_delta=0, servo_object_thread=servo_4_thread_controller),
        5: AxisData(max_value=axis_5_max_value, acceleration=default_acceleration, current_speed=default_speed, target_speed=0, current_pos=0, target_pos=int(32768 * 50 /360 * servo_5_target_pos), distance_delta=0, servo_object_thread=servo_5_thread_controller),
        6: AxisData(max_value=axis_6_max_value, acceleration=default_acceleration, current_speed=default_speed, target_speed=0, current_pos=0, target_pos=int(32768 * 50 /360 * servo_6_target_pos), distance_delta=0, servo_object_thread=servo_6_thread_controller),
    }


    # max val check
    for axis_id in axis_data:
        if axis_data[axis_id].max_value < axis_data[axis_id].target_pos:
            # print( 'axis ', axis_id, 'max value error')
            return

    # set accel
    for axis_id in axis_data:
        axis_data[axis_id].servo_object_thread.set_acceleration(default_acceleration)

    # get pos
    for axis_id in axis_data:
        axis_data[axis_id].current_pos = axis_data[axis_id].servo_object_thread.read_pos()

        if axis_data[axis_id].current_pos >= 4294958900:
            axis_data[axis_id].current_pos = 0

        axis_data[axis_id].distance_delta = abs(axis_data[axis_id].target_pos - axis_data[axis_id].current_pos)


    # get max dist delta
    max_dist_delta = -1
    max_dist_delta_servo_id = 0

    for axis_id in axis_data:
        if axis_data[axis_id].distance_delta > max_dist_delta:
            max_dist_delta = axis_data[axis_id].distance_delta
            max_dist_delta_servo_id = axis_id


    # set target speed
    global_target_time = max_dist_delta / axis_data[max_dist_delta_servo_id].current_speed

    for axis_id in axis_data:
        axis_data[axis_id].target_speed = round(axis_data[axis_id].distance_delta / global_target_time)
        
        # if axis_id == 3:
        #     axis_data[axis_id].servo_object_thread.set_speed(axis_data[axis_id].target_speed * 2)
        
        # else:
        axis_data[axis_id].servo_object_thread.set_speed(axis_data[axis_id].target_speed)
        
        # print('axis ', axis_id, axis_data[axis_id].servo_object_thread.read_speed(), axis_data[axis_id].distance_delta)
   
    # set target pos
    for axis_id in axis_data:
        axis_data[axis_id].servo_object_thread.set_pos(axis_data[axis_id].target_pos)
    

    for axis_id in axis_data:
        axis_data[axis_id].servo_object_thread.print_servo_data()

    servo_1_thread_controller.general_move_command()


can_obj = servo_realisation.control_objects.input_output_realisation.get_can_object()
read_thread = threading.Thread(target=servo_realisation.thread_readr.thread_reader.thread_reader, args=(can_obj, ), daemon=True)
read_thread.start()





servo_1_thread_controller.set_mode(1)
servo_2_thread_controller.set_mode(1)
servo_3_thread_controller.set_mode(1)
# servo_4_thread_controller.set_mode(1)
servo_5_thread_controller.set_mode(1)
servo_6_thread_controller.set_mode(1)

# 15.2-4.2+7.6 !!!


# axis X

axis_1_start_pos = 0
axis_6_start_pos = 180

axis_1_target_pos = 180
axis_6_target_pos = 0
axis_5_center_pos = 90+3.4

# axis Y

axis_3_fix = 15.2-4.2+7.6

axis_2_start_pos = 0
axis_3_start_pos = axis_3_fix
axis_5_start_pos = axis_5_center_pos

axis_2_target_pos = 22
axis_3_target_pos = 30*2 + axis_3_fix
axis_5_target_pos = axis_5_center_pos + 2* axis_2_target_pos 




try:
    while 1:
        move_to_pos_sync(servo_2_target_pos=axis_2_target_pos, servo_3_target_pos=axis_3_target_pos, servo_5_target_pos=axis_5_target_pos, servo_1_target_pos=axis_1_target_pos, servo_6_target_pos=axis_6_target_pos)
        
        time.sleep(20)
        move_to_pos_sync(servo_2_target_pos=axis_2_start_pos, servo_3_target_pos=axis_3_start_pos, servo_5_target_pos=axis_5_start_pos, servo_1_target_pos=axis_1_start_pos, servo_6_target_pos=axis_6_start_pos)
        time.sleep(20)
    pass
except:
    print('err')

# move_to_pos_sync(axis_1_start_pos, 0, 15.2-4.2+7.6, 0, 0, axis_6_start_pos)
# print(servo_6_thread_controller.read_pos())
# time.sleep(10)

# while True:

# servo_1_thread_controller.set_acceleration(50)
# servo_6_thread_controller.set_acceleration(50)






# while True:
#     move_to_pos_sync(servo_1_target_pos=axis_1_start_pos, servo_6_target_pos=axis_6_start_pos, servo_2_target_pos=axis_2_start_pos, servo_3_target_pos=15.2-4.2+7.6+axis_3_start_pos, servo_5_target_pos=axis_5_start_pos)
#     time.sleep(20)
#     move_to_pos_sync(servo_1_target_pos=axis_1_target_pos, servo_6_target_pos=axis_6_target_pos, servo_2_target_pos=axis_2_target_pos, servo_3_target_pos=15.2-4.2+7.6+axis_3_target_pos, servo_5_target_pos=axis_5_target_pos)
#     time.sleep(20)


#15.2-4.2+7.6

# move_to_pos_sync( servo_3_target_pos=axis_3_target_pos, servo_2_target_pos=axis_2_target_pos)
# move_to_pos_sync( servo_3_target_pos=axis_3_start_pos, servo_2_target_pos=axis_2_start_pos)



# print('ser1', servo_1_thread_controller.read_pos())
# print('ser2',servo_2_thread_controller.read_pos())
# print('ser3',servo_3_thread_controller.read_pos())
# print('ser5',servo_5_thread_controller.read_pos())
# print('ser6',servo_6_thread_controller.read_pos())
