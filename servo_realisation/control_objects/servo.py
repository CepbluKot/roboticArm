import canalystii
import servo_realisation.control_objects.servo_interface


class Servo(servo_realisation.control_objects.servo_interface.ServoInterface):
    def __init__(self, device_object: canalystii.device.CanalystDevice, servo_id: int) -> None:
        self.servo_id = servo_id
        self.device = device_object

    def recieve(self, channel: int):
        return self.device.receive(channel=channel)

    def send(self, channel: int, messages):
        return self.device.send(channel=channel, messages=messages)
