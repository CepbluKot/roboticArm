from servo_realisation import servo_interface


class ServoAbstraction:
    servo_id: int


class ServoSdoAbsolutePositionModeAbstraction:
    def control_word(self) -> str:
        pass

    def working_mode(self) -> str:
        pass

    def actual_position(self) -> str:
        pass

    def trapezoidal_speed(self) -> str:
        pass

    def trapezoidal_acceleration(self) -> str:
        pass

    def control_word(self) -> str:
        pass

    def location_cache(self) -> str:
        pass

    def status_word_read(self) -> str:
        pass


class ServoSdoRelativePositionModeAbstraction:
    def control_word(self) -> str:
        pass

    def working_mode(self) -> str:
        pass

    def actual_position(self) -> str:
        pass

    def trapezoidal_speed(self) -> str:
        pass

    def trapezoidal_acceleration(self) -> str:
        pass

    def control_word(self) -> str:
        pass

    def location_cache(self) -> str:
        pass

    def status_word_read(self) -> str:
        pass


class ServoSdoSpeedModeAbstraction:
    def working_mode(self) -> str:
        pass

    def speed_mode(self) -> str:
        pass

    def control_word(self) -> str:
        pass

    def status_word(self) -> str:
        pass


class ServoPdoControlTheProcessOfFindingTheOriginAbstraction:
    def find_the_origin(self) -> str:
        pass

    def working_mode(self) -> str:
        pass

    def status_word(self) -> str:
        pass


class ServoPdoPositionModeAbstraction(servo_interface.ServoPdoPositionModeInterface):
    def find_the_origin(self) -> str:
        pass

    def target_position_trapezoidal_velocity_current_position_status_word(self) -> str:
        pass

    def control_word_working_mode_target_position_current_position_status_word(
        self,
    ) -> str:
        pass


class ServoPdoSpeedModeAbstraction(servo_interface.ServoPdoSpeedModeInterface):
    def control_word_working_mode_target_speed_current_position_status_word(
        self,
    ) -> str:
        pass


class ServoPdoPositionInterpolationModeAbstraction(
    servo_interface.ServoPdoPositionInterpolationModeInterface
):
    def destination_location(self) -> str:
        pass

    def current_position_status_word(self) -> str:
        pass

    def target_location(self) -> str:
        pass
