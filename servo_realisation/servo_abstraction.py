from servo_realisation import servo_interface
import canalystii
# to - do

# create base class and use it as parent class
# https://stackoverflow.com/questions/70970877/how-to-group-methods-in-python-class


class ServoSdoAbsolutePositionModeAbstraction(
    servo_interface.ServoSdoAbsolutePositionModeInterface
):
    def __init__(
        self,
        servo_interface: servo_interface.ServoInterface,
        servo_sdo_absolute_position_mode_interface: servo_interface.ServoSdoAbsolutePositionModeInterface,
    ) -> None:
        self.servo_interface = servo_interface
        self.servo_sdo_absolute_position_mode_interface = (
            servo_sdo_absolute_position_mode_interface
        )

    def control_word_1(self) -> str:
        return self.servo_sdo_absolute_position_mode_interface.control_word()
    
    def control_word_2(self) -> str:
        return self.servo_sdo_absolute_position_mode_interface.control_word()

    def working_mode(self) -> str:
        return self.servo_sdo_absolute_position_mode_interface.working_mode()

    def actual_position(self) -> str:
        return self.servo_sdo_absolute_position_mode_interface.actual_position()

    def trapezoidal_speed(self) -> str:
        return self.servo_sdo_absolute_position_mode_interface.trapezoidal_speed()

    def trapezoidal_acceleration(self) -> str:
        return (
            self.servo_sdo_absolute_position_mode_interface.trapezoidal_acceleration()
        )

    def location_cache(self) -> str:
        return self.servo_sdo_absolute_position_mode_interface.location_cache()

    def status_word_read(self) -> str:
        return self.servo_sdo_absolute_position_mode_interface.status_word_read()


class ServoSdoRelativePositionModeAbstraction(
    servo_interface.ServoSdoRelativePositionModeInterface
):
    def __init__(
        self,
        servo_interface: servo_interface.ServoInterface,
        servo_sdo_relative_position_mode_interface: servo_interface.ServoSdoRelativePositionModeInterface,
    ) -> None:
        self.servo_interface = servo_interface
        self.servo_sdo_relative_position_mode_interface = (
            servo_sdo_relative_position_mode_interface
        )

    def control_word(self) -> str:
        return self.servo_sdo_relative_position_mode_interface.control_word()

    def working_mode(self) -> str:
        return self.servo_sdo_relative_position_mode_interface.working_mode()

    def actual_position(self) -> str:
        return self.servo_sdo_relative_position_mode_interface.actual_position()

    def trapezoidal_speed(self) -> str:
        return self.servo_sdo_relative_position_mode_interface.trapezoidal_speed()

    def trapezoidal_acceleration(self) -> str:
        return (
            self.servo_sdo_relative_position_mode_interface.trapezoidal_acceleration()
        )

    def control_word(self) -> str:
        return self.servo_sdo_relative_position_mode_interface.control_word()

    def location_cache(self) -> str:
        return self.servo_sdo_relative_position_mode_interface.location_cache()

    def status_word_read(self) -> str:
        return self.servo_sdo_relative_position_mode_interface.status_word_read()


class ServoSdoSpeedModeAbstraction(servo_interface.ServoSdoSpeedModeInterface):
    def __init__(
        self,
        servo_interface: servo_interface.ServoInterface,
        servo_sdo_speed_mode_interface: servo_interface.ServoSdoSpeedModeInterface,
    ) -> None:
        self.servo_interface = servo_interface
        self.servo_sdo_speed_mode_interface = servo_sdo_speed_mode_interface

    def working_mode(self) -> str:
        return self.servo_sdo_speed_mode_interface.working_mode()

    def speed_mode(self) -> str:
        return self.servo_sdo_speed_mode_interface.speed_mode()

    def control_word(self) -> str:
        return self.servo_sdo_speed_mode_interface.control_word()

    def status_word(self) -> str:
        return self.servo_sdo_speed_mode_interface.status_word()


class ServoPdoControlTheProcessOfFindingTheOriginAbstraction(
    servo_interface.ServoPdoControlTheProcessOfFindingTheOriginInterface
):
    def __init__(
        self,
        servo_interface: servo_interface.ServoInterface,
        servo_pdo_control_the_process_of_finding_the_origin_interface: servo_interface.ServoPdoControlTheProcessOfFindingTheOriginInterface,
    ) -> None:
        self.servo_interface = servo_interface
        self.servo_pdo_control_the_process_of_finding_the_origin_interface = (
            servo_pdo_control_the_process_of_finding_the_origin_interface
        )

    def find_the_origin(self) -> str:
        return (
            self.servo_pdo_control_the_process_of_finding_the_origin_interface.find_the_origin()
        )

    def working_mode(self) -> str:
        return (
            self.servo_pdo_control_the_process_of_finding_the_origin_interface.working_mode()
        )

    def status_word(self) -> str:
        return (
            self.servo_pdo_control_the_process_of_finding_the_origin_interface.status_word()
        )


class ServoPdoAbsolutePositionModeAbstraction(servo_interface.ServoPdoAbsolutePositionModeInterface):
    def __init__(
        self,
        servo_interface: servo_interface.ServoInterface,
        servo_pdo_position_mode_interface: servo_interface.ServoPdoAbsolutePositionModeInterface,
    ) -> None:
        self.servo_interface = servo_interface
        self.servo_pdo_position_mode_interface = servo_pdo_position_mode_interface

    def find_the_origin(self) -> str:
        return self.servo_pdo_position_mode_interface.find_the_origin()

    def target_position_trapezoidal_velocity_current_position_status_word(self) -> str:
        return (
            self.servo_pdo_position_mode_interface.target_position_trapezoidal_velocity_current_position_status_word()
        )

    def control_word_working_mode_target_position_current_position_status_word(
        self,
    ) -> str:
        return (
            self.servo_pdo_position_mode_interface.control_word_working_mode_target_position_current_position_status_word()
        )


class ServoPdoSpeedModeAbstraction(servo_interface.ServoPdoSpeedModeInterface):
    def __init__(
        self,
        servo_interface: servo_interface.ServoInterface,
        servo_pdo_speed_mode_interface: servo_interface.ServoPdoSpeedModeInterface,
    ) -> None:
        self.servo_interface = servo_interface
        self.servo_pdo_speed_mode_interface = servo_pdo_speed_mode_interface

    def control_word_working_mode_target_speed_current_position_status_word(
        self,
    ) -> str:
        return (
            self.servo_pdo_speed_mode_interface.control_word_working_mode_target_speed_current_position_status_word()
        )


class ServoPdoPositionInterpolationModeAbstraction(
    servo_interface.ServoPdoPositionInterpolationModeInterface
):
    def __init__(
        self,
        servo_interface: servo_interface.ServoInterface,
        servo_pdo_position_interpolation_mode_interface: servo_interface.ServoPdoPositionInterpolationModeInterface,
    ) -> None:
        self.servo_interface = servo_interface
        self.servo_pdo_position_interpolation_mode_interface = (
            servo_pdo_position_interpolation_mode_interface
        )

    def destination_location(self) -> str:
        return (
            self.servo_pdo_position_interpolation_mode_interface.destination_location()
        )

    def current_position_status_word(self) -> str:
        return (
            self.servo_pdo_position_interpolation_mode_interface.current_position_status_word()
        )

    def target_location(self) -> str:
        return self.servo_pdo_position_interpolation_mode_interface.target_location()
