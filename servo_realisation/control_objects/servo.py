import canalystii
import servo_realisation.control_objects.servo_interface
import can


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
        return self.device.send(channel=channel, messages=messages)


class ServoCan(servo_realisation.control_objects.servo_interface.ServoInterfaceCan):
    def __init__(
        self, device_object: can.interface.Bus, servo_id: int
    ) -> None:
        self.servo_id = servo_id
        self.device = device_object

    def receive(self):
        return self.device.recv()

    def send(self, message: can.Message):
        return self.device.send(msg=message)
