import threading, typing, time
from servo_realisation.output import robot, current_positions, hardware_interface
from gui.output import axis_set_angle_slider_data
from control_system.axis_sync import syncronise_2
from servo_realisation.hardware_interface.USB_CAN import QueueMessage


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


def are_positions_allowed(positions: typing.Dict[int, int]):
    if 1 in positions and positions[1] > 32768.0*50.0/360.0*300.0:
        return False
    if 2 in positions and positions[2] > 32768.0*50.0/360.0*160.0:
        return False
    if 3 in positions and positions[3] > 32768.0*50.0/360.0*150.0:
        return False
    if 4 in positions and positions[4] > 32768.0*50.0/360.0*90.0:
        return False
    if 5 in positions and positions[5] > 32768.0*50.0/360.0*180.0:
        return False
    return True


def are_speeds_allowed(speeds: typing.Dict[int, int]):
    if 1 in speeds and speeds[1] > 300:
        return False
    if 2 in speeds and speeds[2] > 300:
        return False
    if 3 in speeds and speeds[3] > 300:
        return False
    if 4 in speeds and speeds[4] > 300:
        return False
    if 5 in speeds and speeds[5] > 300:
        return False
    return True


def are_accels_allowed(accelerations: typing.Dict[int, int]):
    if 1 in accelerations and accelerations[1] > 400:
        return False
    if 2 in accelerations and accelerations[2] > 400:
        return False
    if 3 in accelerations and accelerations[3] > 400:
        return False
    if 4 in accelerations and accelerations[4] > 400:
        return False
    if 5 in accelerations and accelerations[5] > 400:
        return False
    return True

def interpol_call_for_thread():
    max_speed = 100
    target_positions = {}
    speeds, accelerations = {}, {}

    for axis_id in axis_set_angle_slider_data:
        axis_target_pos = axis_set_angle_slider_data[axis_id]()
        target_positions[axis_id] = round(32768.0*50.0/360.0*axis_target_pos)
        
    if not are_positions_allowed(target_positions):
        print('error - position not allowed')
        return None

    robot.set_target_pos(target_positions)
 
    # speeds, accelerations = syncronise(movement_time=4, current_positions=current_positions, target_positions=target_positions, max_acceleration=max_accel, max_speed=max_speed)
    speeds, accelerations = syncronise_2(current_positions=current_positions, target_positions=target_positions, max_speed=max_speed)

    if not accelerations:
        print('error - no accelerations')
        return None
    
    if not speeds:
        print('error - no speeds')
        return None

    if not are_speeds_allowed(speeds):
        print('error - speeds are not allowed')
        return None

    if not are_accels_allowed(accelerations):
        print('error - accels are not allowed')
        return None

    for servo_id in accelerations:
        robot.set_axis_accel(servo_id, accelerations[servo_id])
        robot.set_axis_speed(servo_id, speeds[servo_id])
    
    while not check_is_buffer_empty_filtered(hardware_interface.get_buffer()):
        pass

    print('done')
    robot.move()

def interpolation_call():
    interp_thr = threading.Thread(target=interpol_call_for_thread, daemon=True)
    interp_thr.start()
