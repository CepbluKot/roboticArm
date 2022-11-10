import typing, canalystii, abc


class ProtocolInterface(abc.ABC):
    @abc.abstractmethod
    def send_speed(self, servo_id: int, value: int) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def send_mode(self, servo_id: int, value: int) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def send_acceleration(self, servo_id: int, value: int) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def send_save(self, servo_id: int) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def send_zero_pos_set(self, servo_id: int) -> typing.List[canalystii.Message]:
        raise NotImplemented

    @abc.abstractmethod
    def send_target_pos(self, servo_id: int, value: int) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def send_general_move_command(self) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def read_speed(self, servo_id: int) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def read_accelearation(self, servo_id: int) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def read_mode(self, servo_id: int) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def read_error_checker(self, servo_id: int) -> canalystii.Message:
        raise NotImplemented

    @abc.abstractmethod
    def check_is_buffer_empty(self) -> bool:
        raise NotImplemented

    @abc.abstractmethod
    def get_command_id(self, msg: canalystii.Message):
        raise NotImplemented
