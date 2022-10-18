import servo_realisation.control_objects.servo_interface


class ServoAbstraction(servo_realisation.control_objects.servo_interface.ServoInterface):
    def __init__(self, interface: servo_realisation.control_objects.servo_interface.ServoInterface) -> None:
        self.interface = interface

    def recieve(self, channel: int):
        return self.interface.recieve(channel=channel)

    def send(self, channel: int, messages):
        return self.interface.send(channel=channel, messages=messages)
