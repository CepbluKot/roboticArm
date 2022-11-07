class ServoMotor:
    def __init__(self, id: int) -> None:
        self.id = id
        self.is_active = False
        self.current_pos = -1
        self.target_pos = -1
        self.speed = -1
        self.acceleration = -1
        self.mode = -1
        self.error_code = -1
        self.pulses_per_revolution = 32768
        self.gearbox = 50

    def set_zero_pos(self):
        self.current_pos = 0

    def set_mode(self, value: int):
        self.mode = value

    def set_speed(self, value: int):
        self.speed = value

    def set_acceleration(self, value: int):
        self.acceleration = value

    def set_target_pos(self, value: int):
        self.target_pos = value

    def read_mode(self):
        return self.mode

    def read_speed(self):
        return self.speed

    def read_acceleartion(self):
        return self.acceleration

    def read_pos(self):
        return self.current_pos

    def read_target_pos(self):
        return self.target_pos

    def read_error_code(self):
        return self.error_code
