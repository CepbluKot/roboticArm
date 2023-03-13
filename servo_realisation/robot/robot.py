import typing, time, threading, copy

from servo_realisation.protocol_interface.protocol_interface import ProtocolInterface
from servo_realisation.robot.servo_motor import ServoMotorAliexpress


class Robot:
    def __init__(
        self,
        DoF: int,
        servos: typing.List[ServoMotorAliexpress]
    ) -> None:
        self.DoF = DoF

        servos_to_dict = {}

        for servo in servos:
            servos_to_dict[servo.id] = servo

        self.servos: typing.Dict[int, ServoMotorAliexpress] = servos_to_dict.copy()

        if len(servos) != DoF:
            raise Exception('ERROR - len(assigned_servos_ids) != DoF')
            
        params_check_thr = threading.Thread(target=self.params_checker, daemon=True)
        params_check_thr.start()


    def update_acceleration_callback(self, servo_id: int, value: int):
        self.servos[servo_id].acceleration = value 
    
    def update_mode_callback(self, servo_id: int, value: int):
        self.servos[servo_id].mode = value

    def update_speed_callback(self, servo_id: int, value: int):
        self.servos[servo_id].speed = value

    def update_position_callback(self, servo_id: int, value: int):
        self.servos[servo_id].current_pos = value

    def send_mode(self, value: int):
        for servo_id in self.servos:
            self.servos[servo_id].send_mode(value=value)

    def send_all_axis_speeds(self, value: int):
        for servo_id in self.servos:
            self.servos[servo_id].send_speed(value=value)

    def send_axis_speed(self, axis_id: int, value: int):
        self.servos[axis_id].send_mode(value=value)

    def send_all_axis_acceleration(self, value: int):
        for servo_id in self.servos:
            self.servos[servo_id].send_acceleration(value=value)
    
    def send_axis_accel(self, axis_id: int, value: int,):
        self.servos[axis_id].send_acceleration(value=value)

    def send_target_pos(self, positions: typing.List[int]):
        for servo_id in self.servos:
            if positions[servo_id] != -1:
                self.servos[servo_id].send_target_pos(value=positions[servo_id])

    def send_zero_pos(self, servo_id: int):
        self.servos[servo_id].send_zero_pos_set()
        
    def save_settings(self, servo_id: int):
        self.servos[servo_id].send_save()

    def move(self):
        self.servos[1].send_move()

    def read_mode(self, servo_id: int):
        self.servos[servo_id].read_mode()

    def read_speed(self, servo_id: int):
        self.servos[servo_id].read_speed()

    def read_acceleration(self, servo_id: int):
        self.servos[servo_id].read_acceleration()

    def send_enable_modbus(self, servo_id: int):
        self.servos[servo_id].send_modbus_status(value=1)

    def send_disable_modbus(self, servo_id: int):
        self.servos[servo_id].send_modbus_status(value=0)
        
    def send_enable_output(self, servo_id: int):
        self.servos[servo_id].send_driver_output_permission(value=1)

    def send_disable_output(self, servo_id: int):
        self.servos[servo_id].send_driver_output_permission(value=0)

    def send_weak_magnet_angle(self, servo_id: int, value: int):
        self.servos[servo_id].send_weak_magnet_angle(value=value)

    def send_speed_loop_scale_coefficient(self, servo_id: int, value: int):
        self.servos[servo_id].send_speed_loop_scale_coefficient(value=value)

    def send_position_loop_scale_coefficient(self, servo_id: int, value: int):
        self.servos[servo_id].send_position_loop_scale_coefficient(value=value)

    def send_polarity_dir(self, servo_id: int, value: int):
        self.servos[servo_id].send_polarity_dir(value=value)

    def send_electronic_gear_molecules(self, servo_id: int, value: int):
        self.servos[servo_id].send_electronic_gear_molecules(value=value)

    def send_transfer_electronic_denominator(self, servo_id: int, value: int):
        self.servos[servo_id].send_electrical_transmission_denominator(value=value)

    def send_incremental_position(self, servo_id: int, value: int):
        self.servos[servo_id].send_incremental_position(value=value)

    def send_servo_address(self, servo_id: int, value: int):
        self.servos[servo_id].send_servo_address(value=value)

    def send_stationary_max_power(self, servo_id: int, value: int):
        self.servos[servo_id].send_stationary_max_power(value=value)

    def send_specials(self, servo_id: int, value: int):
        self.servos[servo_id].send_specials(value=value)

    def send_target_location_cache(self, servo_id: int, value: int):
        self.servos[servo_id].send_target_position_cache(value=value)

    def send_speed_mode_speed(self, servo_id: int, value: int):
        self.servos[servo_id].send_speed_mode_speed(value=value)

    def send_can_connection_sync_speed_word(self, servo_id: int, value: int):
        self.servos[servo_id].send_can_connection_sync_speed_word(value=value)

    def send_max_current(self, servo_id: int, value: int):
        self.servos[servo_id].send_max_current(value=value)

    def send_control_words(self, servo_id: int, value: int):
        self.servos[servo_id].send_control_words(value=value)

    def send_status_word(self, servo_id: int, value: int):
        self.servos[servo_id].send_status_word(value=value)

    def send_work_mode(self, servo_id: int, value: int):
        self.servos[servo_id].send_work_mode(value=value)

    def send_goto_home_mode(self, servo_id: int, value: int):
        self.servos[servo_id].send_goto_home_mode(value=value)

    def params_checker(self):
        while True:
            time.sleep(0.1)
            for axis_id in range(1,7):
                pass
                # self.protocol_interface.read_speed(axis_id)
                # self.protocol_interface.read_accelearation(axis_id)
                # self.protocol_interface.read_current(axis_id)
                self.servos[axis_id].read_position()
                # self.protocol_interface.read_mode(axis_id)
                # self.protocol_interface.read_error_checker(axis_id)
                # self.protocol_interface.read_temperature(axis_id)
                # self.protocol_interface.read_voltage(axis_id)
