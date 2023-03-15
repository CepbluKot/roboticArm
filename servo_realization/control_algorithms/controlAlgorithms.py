import threading
from typing import Dict
from servo_realization.robot.robot import Robot


class ControlAlgorithms:
    def __init__(self, robot_obj: Robot) -> None:
        self.__robot = robot_obj
    
    def __sync_algorithm_anin(self, movement_time: int, current_positions: Dict[int, int], target_positions: Dict[int, int], max_acceleration: int=300, max_speed: int=100):
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
                raise('ERROR - anin sync algorithm speed error', servo_id, axis_speed)

            if axis_acceleration > max_acceleration:
                raise('ERROR - anin sync algorithm accel error ', servo_id, axis_acceleration)

            accelerations[servo_id] = axis_acceleration
            speeds[servo_id] = axis_speed

        return speeds, accelerations

    def __sync_algorithm_gorelov(self, current_positions: Dict[int, int], target_positions: Dict[int, int], max_speed: int=400):
        if len(current_positions) != len(target_positions):
            raise('error - sync algorithm - len curr pos != len target pos')
        
        percent_for_acceleration = 40 / 100
        percent_for_speed = 80 / 100

        base_speed = percent_for_speed * max_speed
        base_accel = percent_for_acceleration * max_speed

        max_distance = -1
        distances = {}
        accelerations = {}
        speeds = {}

        for servo_id in current_positions:
            if current_positions[servo_id] > 4000000000:
                current_positions[servo_id] = 0
            
            distance = abs(current_positions[servo_id] - target_positions[servo_id]) 
            distances[servo_id] = distance

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
    
    
    def __check_is_buffer_empty_filtered(self):
        is_empty = True
        for servo_id in self.__robot.servos:
            if not self.__robot.servos[servo_id].are_move_commands_sent():
                is_empty = False
        
        return is_empty

    def __are_positions_allowed(self, positions: Dict[int, int]):
        for servo_id in self.__robot.servos:
            servo = self.__robot.servos[servo_id]
        
            if servo_id == 1 and positions[1] > servo.pulses_per_revolution*servo.gearbox_value/360.0*300.0:
                return False
            if servo_id == 2 and positions[2] > servo.pulses_per_revolution*servo.gearbox_value/360.0*160.0:
                return False
            if servo_id == 3 and positions[3] > servo.pulses_per_revolution*servo.gearbox_value/360.0*150.0:
                return False
            if servo_id == 4 and positions[4] > servo.pulses_per_revolution*servo.gearbox_value/360.0*90.0:
                return False
            if servo_id == 5 and positions[5] > servo.pulses_per_revolution*servo.gearbox_value/360.0*180.0:
                return False
            return True


    def __are_speeds_allowed(self, speeds: Dict[int, int]):
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


    def __are_accels_allowed(self, accelerations: Dict[int, int]):
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

    def move_to_point(self, max_speed: int, target_angles: Dict[int, int]):
        def move_to_point_for_thread():
            print('move to point speed', max_speed)
            current_positions = {}
            target_positions = {}
            speeds, accelerations = {}, {}

            for axis_id in target_angles:
                axis_data = self.__robot.servos[axis_id]
                axis_target_angle = target_angles[axis_id]
                target_positions[axis_id] = round(axis_data.pulses_per_revolution*axis_data.gearbox_value/360.0*axis_target_angle)
                
                current_positions[axis_id] = axis_data.current_pos

            if not self.__are_positions_allowed(target_positions):
                raise('error - position not allowed')
            
            self.__robot.send_target_pos(target_positions)

            speeds, accelerations = self.__sync_algorithm_gorelov(current_positions=current_positions, target_positions=target_positions, max_speed=max_speed)

            if not accelerations:
                raise('error - no accelerations')
            
            
            if not speeds:
                raise('error - no speeds')
            

            if not self.__are_speeds_allowed(speeds):
                raise('error - speeds are not allowed')
            

            if not self.__are_accels_allowed(accelerations):
                raise('error - accels are not allowed')
                

            for servo_id in accelerations:
                self.__robot.send_axis_accel(servo_id, accelerations[servo_id])
                self.__robot.send_axis_speed(servo_id, speeds[servo_id])

            while not self.__check_is_buffer_empty_filtered():
                pass

            self.__robot.move()

        move_to_point_thr = threading.Thread(target=move_to_point_for_thread, daemon=True)
        move_to_point_thr.start()
