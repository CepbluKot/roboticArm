import canalystii
import servo_realisation.control_objects.servo
import servo_realisation.control_objects.servo_abstraction


device = canalystii.CanalystDevice(bitrate=1000000, device_index=0)


def create_servo_object(servo_id):
    servo = servo_realisation.control_objects.servo.Servo(
        device_object=device, servo_id=servo_id
    )
    servo_abs = servo_realisation.control_objects.servo_abstraction.ServoAbstraction(
        servo
    )
    return servo_abs
