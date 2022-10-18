import canalystii
import servo_realisation.control_objects.servo_interface


class Servo(servo_realisation.control_objects.servo_interface.ServoInterface):
    def __init__(
        self, device_object: canalystii.device.CanalystDevice, servo_id: int
    ) -> None:
        self.servo_id = servo_id
        self.device = device_object

    def receive(self, channel: int):
        read = 0
        while not read:
            read = self.device.receive(channel=channel)
        return read

    def send(self, channel: int, messages):
        read = 0
        while not read:
            read = self.device.receive(channel=channel)
        return self.device.send(channel=channel, messages=messages)
