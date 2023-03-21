import canalystii, typing
from servo_realization.protocol_interface.protocol_interface import ProtocolInterface
from servo_realization.hardware_interface.USB_CAN import QueueMessage


class ServoMotorAliexpress:
    def __init__(self, id: int, pulses_per_revolution: int, gearbox_value: int, protocol: ProtocolInterface) -> None:
        self.id = id
        self.is_active = True
        self.current_pos = -1
        self.target_pos = -1
        self.speed = -1
        self.acceleration = -1
        self.mode = -1
        self.error_code = -1
        self.pulses_per_revolution = pulses_per_revolution
        self.gearbox_value = gearbox_value
        self.protocol = protocol


    def send_move(self):
        self.protocol.send_general_move_command()

    def send_speed(self, value: int):
        if value != self.speed:
            self.protocol.send_speed(servo_id=self.id, value=value)
            self.speed = value

    def send_mode(self, value: int):
        if value != self.mode:
            self.protocol.send_mode(servo_id=self.id, value=value)
            self.mode = value
    
    def send_acceleration(self, value: int):
        if value != self.acceleration:
            self.protocol.send_acceleration(servo_id=self.id, value=value)
            self.acceleration = value

    def send_save(self):
        self.protocol.send_save(servo_id=self.id)

    def send_zero_pos_set(self) -> typing.List[canalystii.Message]:
        self.protocol.send_zero_pos_set(servo_id=self.id)
        self.current_pos = 0

    def send_target_pos(self, value: int):
        self.protocol.send_target_pos(servo_id=self.id, value=value)
        self.target_pos = value

    def send_general_move_command(self):
        self.protocol.send_general_move_command(servo_id=self.id)

    def read_position(self):
        self.protocol.read_position(servo_id=self.id)

    def read_speed(self):
        self.protocol.read_speed(servo_id=self.id)

    def read_acceleration(self, ):
        self.protocol.read_acceleration(servo_id=self.id)

    
    def read_mode(self, ):
        self.protocol.read_mode(servo_id=self.id)

    
    def read_error_checker(self, ):
        self.protocol.read_error_checker(servo_id=self.id)


    def are_move_commands_sent(self) -> bool:
        command_ids_to_check = [(96, 129), (96, 131), "interpolation"]
        servo_id = self.id
        buffer = self.protocol.get_buffer()

        # print('\n',buffer)

        if buffer:
            for command_id in buffer:
                if command_id in buffer:
                    if servo_id in buffer[command_id]:
                        for is_read in buffer[command_id][servo_id]:
                            if is_read in buffer[command_id][servo_id] and not is_read and command_id in command_ids_to_check:
                                return False

        return True
                             
    def read_save(self, ):
        self.protocol.read_save(servo_id=self.id)

    
    def read_voltage(self, ):
        self.protocol.read_voltage(servo_id=self.id)

    
    def read_temperature(self, ):
        self.protocol.read_temperature(servo_id=self.id)

    
    def read_current(self, ):
        self.protocol.read_current(servo_id=self.id)
    
    
    def read_position(self, ):
        self.protocol.read_position(servo_id=self.id)

    
    def send_speed_loop_integration_time(self, value: int): # !!!
        self.protocol.send_speed_loop_integration_time(servo_id=self.id, value=value)
    
    
    def read_speed_loop_integration_time(self, ): # !!!
        self.protocol.read_speed_loop_integration_time(servo_id=self.id)

    
    def send_modbus_status(self, value: bool):
        self.protocol.send_modbus_status(servo_id=self.id, value=value)

    
    def read_modbus_status(self, ):
        self.protocol.read_modbus_status(servo_id=self.id)

    
    def send_driver_output_permission(self, value: bool):
        self.protocol.send_driver_output_permission(servo_id=self.id, value=value)

    
    def read_driver_output_permission(self, ):
        self.protocol.read_driver_output_permission(servo_id=self.id)

    
    def send_weak_magnet_angle(self, value: int):
        self.protocol.send_weak_magnet_angle(servo_id=self.id, value=value)

    
    def read_weak_magnet_angle(self, ):
        self.protocol.read_weak_magnet_angle(servo_id=self.id)

    
    def send_speed_loop_scale_coefficient(self, value: int): # !!!
        self.protocol.send_speed_loop_scale_coefficient(servo_id=self.id, value=value)

    
    def read_speed_loop_scale_coefficient(self, ): # !!!
        self.protocol.read_speed_loop_scale_coefficient(servo_id=self.id)

    
    def send_position_loop_scale_coefficient(self, value: int): # !!!
        self.protocol.send_position_loop_scale_coefficient(servo_id=self.id, value=value)

    
    def read_position_loop_scale_coefficient(self, ): # !!!
        self.protocol.read_position_loop_scale_coefficient(servo_id=self.id)

    
    def send_polarity_dir(self, value: bool):
        self.protocol.send_polarity_dir(servo_id=self.id, value=value)

    
    def read_polarity_dir(self, ):
        self.protocol.read_polarity_dir(servo_id=self.id)

    
    def send_electronic_gear_molecules(self, value: int):
        self.protocol.send_electronic_gear_molecules(servo_id=self.id, value=value)

    
    def read_electronic_gear_molecules(self, ):
        self.protocol.read_electronic_gear_molecules(servo_id=self.id)

    
    def send_electrical_transmission_denominator(self, value: int):
        self.protocol.send_electrical_transmission_denominator(servo_id=self.id, value=value)

    
    def read_electrical_transmission_denominator(self, ):
        self.protocol.read_electrical_transmission_denominator(servo_id=self.id)

    
    def send_incremental_position(self, value: int):
        self.protocol.send_incremental_position(servo_id=self.id, value=value)

    
    def read_incremental_position(self, ):
        self.protocol.read_incremental_position(servo_id=self.id)

    
    def read_current_speed(self, ):
        self.protocol.read_current_speed(servo_id=self.id)

    
    def read_system_pwm_output(self, ):
        self.protocol.read_system_pwm_output(servo_id=self.id)

    
    def send_servo_address(self, value: int):
        self.protocol.send_servo_address(servo_id=self.id, value=value)

    
    def read_servo_address(self, ):
        self.protocol.read_servo_address(servo_id=self.id)

    
    def send_stationary_max_power(self, value: int):
        self.protocol.send_stationary_max_power(servo_id=self.id, value=value)

    
    def read_stationary_max_power(self, ):
        self.protocol.read_stationary_max_power(servo_id=self.id)

    
    def send_specials(self, value: int):
        self.protocol.send_specials(servo_id=self.id, value=value)

    
    def read_specials(self, ):
        self.protocol.read_specials(servo_id=self.id)

    
    def send_target_position_cache(self, value: int):
        self.protocol.send_target_position_cache(servo_id=self.id, value=value)

    
    def read_target_position_cache(self, ):
        self.protocol.read_target_position_cache(servo_id=self.id)

    
    def send_speed_mode_speed(self, value: int):
        self.protocol.send_speed_mode_speed(servo_id=self.id, value=value)
    
    
    def read_speed_mode_speed(self, value: int):
        self.protocol.read_speed_mode_speed(servo_id=self.id, value=value)

    
    def send_can_connection_sync_speed_word(self, value: int):
        self.protocol.send_can_connection_sync_speed_word(servo_id=self.id, value=value)

    
    def read_can_connection_sync_speed_word(self, ):
        self.protocol.read_can_connection_sync_speed_word(servo_id=self.id)

    
    def send_max_current(self, value: int):
        self.protocol.send_max_current(servo_id=self.id, value=value)

    
    def read_max_current(self, ):
        self.protocol.read_max_current(servo_id=self.id)

    
    def send_control_words(self, value: int):
        self.protocol.send_control_words(servo_id=self.id, value=value)

    
    def read_control_words(self, ):
        self.protocol.read_control_words(servo_id=self.id)

    
    def send_status_word(self, value: int):
        self.protocol.send_status_word(servo_id=self.id, value=value)

    
    def read_status_word(self, ):
        self.protocol.read_status_word(servo_id=self.id)

    
    def send_work_mode(self, value: int):
        self.protocol.send_work_mode(servo_id=self.id, value=value)

    
    def read_work_mode(self, ):
        self.protocol.read_work_mode(servo_id=self.id)

    
    def send_goto_home_mode(self, value: int):
        self.protocol.send_goto_home_mode(servo_id=self.id, value=value)

    
    def read_goto_home_mode(self, ):
        self.protocol.read_goto_home_mode(servo_id=self.id)
