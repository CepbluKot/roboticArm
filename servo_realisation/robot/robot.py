import typing
import servo_realisation.robot
from servo_realisation.protocol_interface.protocol_interface import ProtocolInterface
import servo_motor


class Robot:
    servos: typing.Dict[int, servo_motor.ServoMotor] = {}

    def __init__(
        self,
        DoF: int,
        protocol_interface: ProtocolInterface,
        assigned_servos_ids: typing.List[int] = [],
    ) -> None:
        self.DoF = DoF
        self.protocol_interface = protocol_interface

        if assigned_servos_ids:
            for servo_id in assigned_servos_ids:
                self.servos[servo_id] = servo_motor(servo_id)

        else:
            for servo_id in range(1, DoF + 1):
                self.servos[servo_id] = servo_motor(servo_id)

    def __modify_acceleration(self, servo_id: int, value: int):
        self.servos[servo_id].set_acceleration(value)

    def __modify_mode(self, servo_id: int, value: int):
        self.servos[servo_id].set_mode(value)

    def __modify_pos_to_zero(self, servo_id: int):
        self.servos[servo_id].set_zero_pos()

    def __modify_speed(self, servo_id: int, value: int):
        self.servos[servo_id].set_speed(value)

    def __modify_target_pos(self, servo_id: int, value: int):
        self.servos[servo_id].set_target_pos(value)

    def set_mode(self, value: int):
        for servo_id in self.servos:
            if self.servos[servo_id].read_mode() != value:
                self.protocol_interface.send_mode(servo_id=servo_id, value=value)
                self.__modify_mode(servo_id=servo_id, value=value)

    def set_speed(self, value: int):
        for servo_id in self.servos:
            if self.servos[servo_id].read_speed() != value:
                self.protocol_interface.send_speed(servo_id=servo_id, value=value)
                self.__modify_speed(servo_id=servo_id, value=value)

    def set_acceleration(self, value: int):
        for servo_id in self.servos:
            if self.servos[servo_id].read_acceleartion() != value:
                self.protocol_interface.send_acceleration(
                    servo_id=servo_id, value=value
                )
                self.__modify_acceleration(servo_id=servo_id, value=value)

    def set_target_pos(self, positions: typing.List[int]):
        for servo_id in self.servos:
            if self.servos[servo_id].read_target_pos() != positions[servo_id]:
                self.protocol_interface.send_target_pos(
                    servo_id=servo_id, value=positions[servo_id]
                )
                self.__modify_target_pos(servo_id=servo_id, value=positions[servo_id])

    def move(self):
        self.protocol_interface.send_general_move_command()
