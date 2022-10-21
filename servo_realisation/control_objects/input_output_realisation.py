import canalystii
import can
import servo_realisation.control_objects.servo
import servo_realisation.control_objects.servo_abstraction


device = canalystii.CanalystDevice(bitrate=1000000, device_index=0)
# device_can = can.interface.Bus(bustype='canalystii', channel=0, bitrate=1000000)
# device_can = can.ThreadSafeBus(bustype='canalystii', channel=0, bitrate=1000000)

def create_servo_object(servo_id):
    servo = servo_realisation.control_objects.servo.Servo(
        device_object=device, servo_id=servo_id
    )
    servo_abs = servo_realisation.control_objects.servo_abstraction.ServoAbstraction(
        servo
    )
    return servo_abs


def get_can_object():
    return device


# def create_servo_object_can(servo_id):
#     servo = servo_realisation.control_objects.servo.ServoCan(
#         device_object=device_can, servo_id=servo_id
#     )
#     servo_abs = servo_realisation.control_objects.servo_abstraction.ServoAbstractionCan(
#         servo
#     )
#     return servo_abs
