from time import sleep
from servo_realisation.servo import (
    Servo,
    ServoPdoControlTheProcessOfFindingTheOrigin,
    ServoPdoPositionInterpolationMode,
    ServoSdoAbsolutePositionMode,
    ServoPdoSpeedMode,
    ServoSdoAbsolutePositionMode,
    ServoSdoRelativePositionMode,
    ServoSdoSpeedMode,
)
from servo_realisation.servo_abstraction import (
    ServoPdoControlTheProcessOfFindingTheOriginAbstraction,
    ServoPdoPositionInterpolationModeAbstraction,
    ServoPdoAbsolutePositionModeAbstraction,
    ServoPdoSpeedModeAbstraction,
    ServoSdoAbsolutePositionModeAbstraction,
    ServoSdoRelativePositionModeAbstraction,
    ServoSdoSpeedModeAbstraction,
)

srv = Servo(device_id=0)


servo_sdo_absolute_position_mode = ServoSdoAbsolutePositionMode(servo_interface=srv)
servo_sdo_absolute_position_mode_abs = ServoSdoAbsolutePositionModeAbstraction(
    servo_interface=srv,
    servo_sdo_absolute_position_mode_interface=servo_sdo_absolute_position_mode,
)


servo_sdo_relative_position_mode = ServoSdoRelativePositionMode(servo_interface=srv)
servo_sdo_relative_position_mode_abs = ServoSdoRelativePositionModeAbstraction(
    servo_interface=srv,
    servo_sdo_relative_position_mode_interface=servo_sdo_relative_position_mode,
)


servo_sdo_speed_mode = ServoSdoSpeedMode(servo_interface=srv)
servo_sdo_speed_mode_abs = ServoSdoSpeedModeAbstraction(
    servo_interface=srv, servo_sdo_speed_mode_interface=servo_sdo_speed_mode
)


servo_pdo_control_the_process_of_finding_the_origin = (
    ServoPdoControlTheProcessOfFindingTheOrigin(servo_interface=srv)
)
servo_pdo_control_the_process_of_finding_the_origin_abs = ServoPdoControlTheProcessOfFindingTheOriginAbstraction(
    servo_interface=srv,
    servo_pdo_control_the_process_of_finding_the_origin_interface=servo_pdo_control_the_process_of_finding_the_origin,
)


servo_pdo_position_mode = ServoSdoAbsolutePositionMode(servo_interface=srv)
servo_pdo_position_mode_abs = ServoPdoAbsolutePositionModeAbstraction(
    servo_interface=srv, servo_pdo_position_mode_interface=servo_pdo_position_mode
)


servo_pdo_speed_mode = ServoPdoSpeedMode(servo_interface=srv)
servo_pdo_speed_mode_abs = ServoPdoSpeedModeAbstraction(
    servo_interface=srv, servo_pdo_speed_mode_interface=servo_pdo_speed_mode
)


servo_pdo_position_interpolation_mode = ServoPdoPositionInterpolationMode(
    servo_interface=srv
)
servo_pdo_position_interpolation_mode_abs = ServoPdoPositionInterpolationModeAbstraction(
    servo_interface=srv,
    servo_pdo_position_interpolation_mode_interface=servo_pdo_position_interpolation_mode,
)


print(servo_sdo_speed_mode_abs.speed_mode())
# sleep(5)
print(
    servo_pdo_speed_mode_abs.control_word_working_mode_target_speed_current_position_status_word(
        speed=0
    )
)

# print(servo_sdo_absolute_position_mode_abs.working_mode())
print(servo_sdo_absolute_position_mode_abs.control_word_1())
print(servo_sdo_absolute_position_mode_abs.control_word_2())
print(servo_sdo_absolute_position_mode_abs.status_word_read())
# print(servo_sdo_absolute_position_mode_abs.location_cache())
# print(servo_sdo_absolute_position_mode_abs.actual_position())
# print(servo_sdo_absolute_position_mode_abs.trapezoidal_speed())
