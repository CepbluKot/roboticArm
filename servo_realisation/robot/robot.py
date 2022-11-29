import typing

from servo_realisation.protocol_interface.protocol_interface import ProtocolInterface
from servo_realisation.robot.servo_motor import ServoMotor


class Robot:
    servos: typing.Dict[int, ServoMotor] = {}

    def __init__(
        self,
        DoF: int,
        protocol_interface: ProtocolInterface,
        assigned_servos_ids: typing.List[int] = [],
    ) -> None:
        self.DoF = DoF
        self.protocol_interface = protocol_interface


        if len(assigned_servos_ids) != DoF:
            raise Exception('ERROR len(assigned_servos_ids) != DoF')
            

        if assigned_servos_ids:
            for servo_id in assigned_servos_ids:
                self.servos[servo_id] = ServoMotor(servo_id)

        else:
            for servo_id in range(1, DoF + 1):
                self.servos[servo_id] = ServoMotor(servo_id)


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

    def __read_acceleration(self, servo_id: int):
        return self.servos[servo_id].read_acceleration()

    def __read_mode(self, servo_id: int):
        return self.servos[servo_id].read_mode()

    def __read_speed(self, servo_id: int):
        return self.servos[servo_id].read_speed()

    def __read_target_pos(self, servo_id: int):
        return self.servos[servo_id].read_target_pos()

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
            if self.servos[servo_id].read_acceleration() != value:
                self.protocol_interface.send_acceleration(
                    servo_id=servo_id, value=value
                )
                self.__modify_acceleration(servo_id=servo_id, value=value)

    def set_target_pos(self, positions: typing.List[int]):
        for servo_id in self.servos:
            if self.servos[servo_id].read_target_pos() != positions[servo_id]:
                if positions[servo_id] != -1:
                    print('send', servo_id, positions[servo_id])
                    self.protocol_interface.send_target_pos(
                        servo_id=servo_id, value=positions[servo_id]
                    )
                    self.__modify_target_pos(servo_id=servo_id, value=positions[servo_id])

    def set_zero_pos(self, servo_id: int):
        self.protocol_interface.send_zero_pos_set(servo_id)
        
    def save_settings(self, servo_id: int):
        self.protocol_interface.send_save(servo_id)

    def move(self):
        self.protocol_interface.send_general_move_command()

    def read_mode(self, servo_id: int):
        return self.__read_mode(servo_id=servo_id)

    def read_speed(self, servo_id: int):
        return self.__read_speed(servo_id=servo_id)

    def read_acceleration(self, servo_id: int):
        return self.__read_acceleration(servo_id=servo_id)

    def read_target_pos(self, servo_id: int):
        return self.__read_target_pos(servo_id=servo_id)
