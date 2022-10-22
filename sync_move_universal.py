from typing import Dict
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


servo_1_thread_controller.set_zero_pos()
servo_2_thread_controller.set_zero_pos()
servo_3_thread_controller.set_zero_pos()
servo_4_thread_controller.set_zero_pos()
servo_5_thread_controller.set_zero_pos()
servo_6_thread_controller.set_zero_pos()


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
    default_acceleration = 5

    axis_1_max_value = 360
    axis_2_max_value = 100
    axis_3_max_value = 120
    axis_4_max_value = 180
    axis_5_max_value = 180
    axis_6_max_value = 180


    axis_data: Dict[int, AxisData] = {
        1: AxisData(max_value=axis_1_max_value, acceleration=default_acceleration, current_speed=default_speed, target_speed=0, current_pos=0, target_pos=int(32768 * 50 /360 * servo_1_target_pos), distance_delta=0, servo_object_thread=servo_1_thread_controller),
        2: AxisData(max_value=axis_2_max_value, acceleration=default_acceleration, current_speed=default_speed, target_speed=0, current_pos=0, target_pos=int(32768 * 50 /360 * servo_2_target_pos), distance_delta=0, servo_object_thread=servo_2_thread_controller),
        3: AxisData(max_value=axis_3_max_value, acceleration=default_acceleration, current_speed=default_speed, target_speed=0, current_pos=0, target_pos=int(32768 * 50 /360 * servo_3_target_pos), distance_delta=0, servo_object_thread=servo_3_thread_controller),
        4: AxisData(max_value=axis_4_max_value, acceleration=default_acceleration, current_speed=default_speed, target_speed=0, current_pos=0, target_pos=int(32768 * 50 /360 * servo_4_target_pos), distance_delta=0, servo_object_thread=servo_4_thread_controller),
        5: AxisData(max_value=axis_5_max_value, acceleration=default_acceleration, current_speed=default_speed, target_speed=0, current_pos=0, target_pos=int(32768 * 50 /360 * servo_5_target_pos), distance_delta=0, servo_object_thread=servo_5_thread_controller),
        6: AxisData(max_value=axis_6_max_value, acceleration=default_acceleration, current_speed=default_speed, target_speed=0, current_pos=0, target_pos=int(32768 * 50 /360 * servo_6_target_pos), distance_delta=0, servo_object_thread=servo_6_thread_controller),
    }


    # max val check
    for axis_id in axis_data:
        if axis_data[axis_id].max_value < axis_data[axis_id].target_pos:
            print( 'axis ', axis_id, 'max value error')
            return

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
        axis_data[axis_id].servo_object_thread.set_speed(axis_data[axis_id].target_speed)
        print('axis ', axis_id, axis_data[axis_id].servo_object_thread.read_speed())
   
    # set target pos
    for axis_id in axis_data:
        axis_data[axis_id].servo_object_thread.set_pos(axis_data[axis_id].target_pos)
    
    servo_1_thread_controller.general_move_command()


# can_obj = servo_realisation.control_objects.input_output_realisation.get_can_object()
# read_thread = threading.Thread(target=servo_realisation.thread_readr.thread_reader.thread_reader, args=(can_obj, ), daemon=True)
# read_thread.start()
