import threading, typing, time
from servo_realisation.output import robot, current_positions, hardware_interface
from servo_realisation.hardware_interface.USB_CAN import QueueMessage
from control_system.axis_sync import syncronise_2


def check_is_buffer_empty_filtered(buffer: typing.Dict[int, typing.Dict[int, typing.Dict[bool, QueueMessage]]]):
    command_ids_to_check = [(96, 129), (96, 131), "interpolation"]

    is_empty = True
    
    if buffer:
        for command_id in buffer:
            if buffer[command_id]:
                for servo_id in buffer[command_id]:
                    if buffer[command_id][servo_id]:
                        for is_read in buffer[command_id][servo_id]:
                            if not is_read and command_id in command_ids_to_check and buffer[command_id][servo_id][is_read]:
                                # print('wtf', buffer[command_id][servo_id][is_read].message)
                                is_empty = False
    
    return is_empty


def interpol_call_for_thread(axis_set_angle_data: typing.Dict[int, int]):
    max_speed = 100
    target_positions = {}
    speeds, accelerations = {}, {}

    for axis_id in axis_set_angle_data:
        axis_target_pos = axis_set_angle_data[axis_id]
        target_positions[axis_id] = 32768*50/360*round(float(axis_target_pos))
        
    robot.set_target_pos(target_positions)
 
    # speeds, accelerations = syncronise(movement_time=4, current_positions=current_positions, target_positions=target_positions, max_acceleration=max_accel, max_speed=max_speed)
    speeds, accelerations = syncronise_2(current_positions=current_positions, target_positions=target_positions, max_speed=max_speed)

    if not accelerations:
        print('INTERPOL MOVE ERROR - accel')
        return None
    
    if not speeds:
        print('INTERPOL MOVE ERROR - speds')
        return None

    for servo_id in accelerations:
        robot.set_axis_accel(servo_id, accelerations[servo_id])
        robot.set_axis_speed(servo_id, speeds[servo_id])
    
    while not check_is_buffer_empty_filtered(hardware_interface.get_buffer()):
        pass

    print('done')
    robot.move()


def interpolation_call(axis_set_angle_data: typing.Dict[int, int]):
    interp_thr = threading.Thread(target=interpol_call_for_thread, args=(axis_set_angle_data,), daemon=True)
    interp_thr.start()
    interp_thr.join()


target_1 = {1: 0, 2: 30, 3: 30, 4: 0, 5: 90, 6: 0}
target_2 = {1: 0, 2: 0, 3: 0, 4: 0, 5: 90, 6: 0}


while True:
    interpolation_call(target_1)
    time.sleep(6)
    interpolation_call(target_2)
    time.sleep(6)
