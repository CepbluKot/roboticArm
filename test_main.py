from servo_realisation.servo import Servo, ServoPdoControlTheProcessOfFindingTheOrigin, ServoPdoPositionInterpolationMode, ServoPdoPositionMode, ServoPdoSpeedMode, ServoSdoAbsolutePositionMode, ServoSdoRelativePositionMode, ServoSdoSpeedMode
from servo_realisation.servo_abstraction import ServoAbstraction, ServoPdoControlTheProcessOfFindingTheOriginAbstraction, ServoPdoPositionInterpolationModeAbstraction, ServoPdoPositionModeAbstraction, ServoPdoSpeedModeAbstraction, ServoSdoAbsolutePositionModeAbstraction, ServoSdoRelativePositionModeAbstraction, ServoSdoSpeedModeAbstraction

srv = Servo()
srv_abs = ServoAbstraction()
srv.servo_id = 1

servo_sdo_absolute_position_mode = ServoSdoAbsolutePositionMode(servo_interface=srv_abs)
servo_sdo_absolute_position_mode_abs = ServoSdoAbsolutePositionModeAbstraction(servo_interface=srv, servo_sdo_absolute_position_mode_interface=)

servo_sdo_relative_position_mode = ServoSdoRelativePositionMode(servo_interface=srv_abs)
servo_sdo_relative_position_mode_abs = ServoSdoRelativePositionModeAbstraction(servo_interface=srv_abs, servo_sdo_relative_position_mode_interface=servo_sdo_relative_position_mode)


servo_sdo_speed_mode = ServoSdoSpeedMode()
servo_sdo_speed_mode_abs = ServoSdoSpeedModeAbstraction(servo_interface=srv_abs, servo_sdo_speed_mode_interface=servo_sdo_speed_mode)


servo_pdo_control_the_process_of_finding_the_origin = ServoPdoControlTheProcessOfFindingTheOrigin(servo_interface=srv_abs)
servo_pdo_control_the_process_of_finding_the_origin_abs = ServoPdoControlTheProcessOfFindingTheOriginAbstraction(servo_interface=srv_abs, servo_pdo_control_the_process_of_finding_the_origin_interface=servo_pdo_control_the_process_of_finding_the_origin)


servo_pdo_position_mode = ServoPdoPositionMode(servo_interface=srv_abs)
servo_pdo_position_mode_abs = ServoPdoPositionModeAbstraction(servo_interface=srv_abs, servo_pdo_position_mode_interface=servo_pdo_position_mode)


servo_pdo_speed_mode = ServoPdoSpeedMode(servo_interface=srv_abs)
servo_pdo_speed_mode_abs = ServoPdoSpeedModeAbstraction(servo_interface=srv_abs, servo_pdo_speed_mode_interface=servo_pdo_speed_mode)


servo_pdo_position_interpolation_mode = ServoPdoPositionInterpolationMode(servo_interface=srv_abs)
servo_pdo_position_interpolation_mode_abs = ServoPdoPositionInterpolationModeAbstraction(servo_interface=srv_abs, servo_pdo_position_interpolation_mode_interface=servo_pdo_position_interpolation_mode)
