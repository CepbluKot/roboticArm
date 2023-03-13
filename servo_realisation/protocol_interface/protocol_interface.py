import typing, canalystii, abc


class ProtocolInterface(abc.ABC):
    @abc.abstractmethod
    def send_speed(self, servo_id: int, value: int) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def send_mode(self, servo_id: int, value: int) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def send_acceleration(self, servo_id: int, value: int) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def send_save(self, servo_id: int) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def send_zero_pos_set(self, servo_id: int) -> typing.List[canalystii.Message]:
        raise NotImplemented

    @abc.abstractmethod
    def send_target_pos(self, servo_id: int, value: int) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def send_general_move_command(self) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def read_position(self, servo_id: int) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def read_speed(self, servo_id: int) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def read_accelearation(self, servo_id: int) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def read_mode(self, servo_id: int) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def read_error_checker(self, servo_id: int) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def check_is_buffer_empty(self) -> bool:
        raise NotImplemented

    @abc.abstractmethod
    def read_save(self, servo_id: int) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def read_voltage(self, servo_id: int) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def read_temperature(self, servo_id: int) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def read_current(self, servo_id: int) -> canalystii.Message:
        raise NotImplemented
    
    @abc.abstractmethod
    def read_position(self, servo_id: int) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def read_speed_loop_integration_time(self, servo_id: int) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def send_modbus_status(self, servo_id: int, value: bool) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def read_modbus_status(self, servo_id: int) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def send_driver_output_permission(self, servo_id: int, value: bool) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def read_driver_output_permission(self, servo_id: int) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def send_weak_magnet_angle(self, servo_id: int, value: int) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def read_weak_magnet_angle(self, servo_id: int) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def send_speed_loop_scale_coefficient(self, servo_id: int, value: int) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def read_speed_loop_scale_coefficient(self, servo_id: int) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def send_position_loop_scale_coefficient(self, servo_id: int, value: int) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def send_polarity_dir(self, servo_id: int, value: bool) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def read_polarity_dir(self, servo_id: int) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def send_electronic_gear_molecules(self, servo_id: int, value: int) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def read_electronic_gear_molecules(self, servo_id: int) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def send_electrical_transmission_denominator(self, servo_id: int, value: int) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def read_electrical_transmission_denominator(self, servo_id: int) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def send_incremental_position(self, servo_id: int, value: int) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def read_incremental_position(self, servo_id: int) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def read_current_speed(self, servo_id: int) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def read_system_pwm_output(self, servo_id: int) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def send_servo_address(self, servo_id: int, value: int) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def read_servo_address(self, servo_id: int) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def send_stationary_max_power(self, servo_id: int, value: int) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def read_stationary_max_power(self, servo_id: int) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def send_specials(self, servo_id: int, value: int) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def read_specials(self, servo_id: int) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def send_target_position_cache(self, servo_id: int, value: int) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def read_target_position_cache(self, servo_id: int) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def send_speed_mode_speed(self, servo_id: int, value: int) -> canalystii.Message:
        raise NotImplemented
    
    @abc.abstractmethod
    def send_can_connection_sync_speed_word(self, servo_id: int, value: int) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def read_can_connection_sync_speed_word(self, servo_id: int) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def send_max_current(self, servo_id: int, value: int) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def read_max_current(self, servo_id: int) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def send_control_words(self, servo_id: int, value: int) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def read_control_words(self, servo_id: int) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def send_status_word(self, servo_id: int, value: int) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def read_status_word(self, servo_id: int) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def send_work_mode(self, servo_id: int, value: int) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def read_work_mode(self, servo_id: int) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def send_goto_home_mode(self, servo_id: int, value: int) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def read_goto_home_mode(self, servo_id: int) -> canalystii.Message:
        raise NotImplemented
