from typing import Dict
import typing
from servo_realisation.hardware_interface.USB_CAN import QueueMessage



def syncronise(movement_time: int, current_positions: Dict[int, int], target_positions: Dict[int, int], max_acceleration: int=300, max_speed: int=100):
    percent_of_time_for_acceleration = 5 / 100 #   для ускорения и замедления
    percent_of_time_for_const_speed_move = (100 - percent_of_time_for_acceleration) / 100

    time_for_accel = movement_time * percent_of_time_for_acceleration
    time_for_const_speed_move = movement_time * percent_of_time_for_const_speed_move

    accelerations = {}
    speeds = {}

    for servo_id in current_positions:
        if current_positions[servo_id] > 4000000000:
            current_positions[servo_id] = 0
        
        distance = abs(current_positions[servo_id] - target_positions[servo_id]) 

        if distance < 500:
            continue

        axis_speed = distance / ((1/time_for_const_speed_move) + time_for_accel)
        axis_speed = axis_speed / ( 32768 * 50 / 60)
        axis_acceleration = axis_speed / time_for_accel

        if axis_speed > max_speed:
            print('speed err', servo_id, axis_speed)
            return None
        
        if axis_acceleration > max_acceleration:
            print('accel err', servo_id, axis_acceleration)
            return None

        accelerations[servo_id] = axis_acceleration
        speeds[servo_id] = axis_speed

    return speeds, accelerations


def syncronise_2(current_positions: Dict[int, int], target_positions: Dict[int, int], max_speed: int=400):
    percent_for_acceleration = 40 / 100
    percent_for_speed = 80 / 100

    base_speed = percent_for_speed * max_speed
    base_accel = percent_for_acceleration * max_speed

    max_distance = -1
    distances = {}
    accelerations = {}
    speeds = {}

    # print('current_positions',current_positions)
    # print('target_positions',target_positions)

    for servo_id in current_positions:
        if current_positions[servo_id] > 4000000000:
            current_positions[servo_id] = 0
        
        distance = abs(current_positions[servo_id] - target_positions[servo_id]) 
        distances[servo_id] = distance

    # print('distances',distances)

    if distances:

        max_distance_axis_id = max(distances, key=distances.get)
        max_distance = distances[max_distance_axis_id]

        for servo_id in distances :
            if distances[servo_id] < 500:
                continue
            
            axis_sync_coef = distances[servo_id] / max_distance

            axis_speed = base_speed * axis_sync_coef
            axis_acceleration = base_accel * axis_sync_coef

            accelerations[servo_id] = axis_acceleration
            speeds[servo_id] = axis_speed

        return speeds, accelerations

    else:
        return None, None
