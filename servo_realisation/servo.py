from servo_realisation import servo_interface
import canalystii


class Servo:
    servo_id: int


class ServoSdoAbsolutePositionMode:
    def __init__(self, servo_interface: servo_interface.ServoInterface,) -> None:
        self.servo_interface = servo_interface

        self.dev = canalystii.CanalystDevice(
            bitrate=1000000, device_index=servo_interface.servo_id
        )

    def control_word_1(self) -> str:
        new_message = canalystii.Message(
            can_id=0x601,
            remote=False,
            extended=False,
            data_len=6,
            data=(0x2B, 0x40, 0x60, 0x00, 0x0F, 0x00),
        )
        self.dev.send(0, new_message)
        return self.dev.recieve(0), self.dev.recieve(1)

    def working_mode(self) -> str:
        new_message = canalystii.Message(
            can_id=0x601,
            remote=False,
            extended=False,
            data_len=5,
            data=(0x2F, 0x60, 0x60, 0x00, 0x01),
        )
        self.dev.send(0, new_message)
        return self.dev.recieve(0), self.dev.recieve(1)

    def actual_position(self) -> str:
        new_message = canalystii.Message(
            can_id=0x601,
            remote=False,
            extended=False,
            data_len=4,
            data=(0x40, 0x64, 0x60, 0x00),
        )
        self.dev.send(0, new_message)
        return self.dev.recieve(0), self.dev.recieve(1)

    def trapezoidal_speed(self) -> str:
        new_message = canalystii.Message(
            can_id=0x601,
            remote=False,
            extended=False,
            data_len=8,
            data=(0x23, 0x81, 0x60, 0x00, 0xE8, 0x03, 0x00, 0x00),
        )
        self.dev.send(0, new_message)
        return self.dev.recieve(0), self.dev.recieve(1)

    def trapezoidal_acceleration(self) -> str:
        new_message = canalystii.Message(
            can_id=0x601,
            remote=False,
            extended=False,
            data_len=8,
            data=(0x23, 0x83, 0x60, 0x00, 0x20, 0x4E, 0x00, 0x00),
        )
        self.dev.send(0, new_message)
        return self.dev.recieve(0), self.dev.recieve(1)

    def control_word_2(self) -> str:
        new_message = canalystii.Message(
            can_id=0x601,
            remote=False,
            extended=False,
            data_len=6,
            data=(0x2B, 0x40, 0x60, 0x00, 0x2F, 0x00),
        )
        self.dev.send(0, new_message)
        return self.dev.recieve(0), self.dev.recieve(1)

    def location_cache(self) -> str:
        new_message = canalystii.Message(
            can_id=0x601,
            remote=False,
            extended=False,
            data_len=8,
            data=(0x23, 0x7A, 0x60, 0x00, 0x50, 0xC3, 0x00, 0x00),
        )
        self.dev.send(0, new_message)
        return self.dev.recieve(0), self.dev.recieve(1)

    def status_word_read(self) -> str:
        new_message = canalystii.Message(
            can_id=0x601,
            remote=False,
            extended=False,
            data_len=4,
            data=(0x40, 0x41, 0x60, 0x00),
        )
        self.dev.send(0, new_message)
        return self.dev.recieve(0), self.dev.recieve(1)


class ServoSdoRelativePositionMode:
    def __init__(self, servo_interface: servo_interface.ServoInterface,) -> None:
        self.servo_interface = servo_interface

        self.dev = canalystii.CanalystDevice(
            bitrate=1000000, device_index=servo_interface.servo_id
        )

    def control_word(self) -> str:
        new_message = canalystii.Message(
            can_id=0x601,
            remote=False,
            extended=False,
            data_len=6,
            data=(0x2B, 0x40, 0x60, 0x00, 0x0F, 0x00),
        )
        self.dev.send(0, new_message)
        return self.dev.recieve(0), self.dev.recieve(1)

    def working_mode(self) -> str:
        new_message = canalystii.Message(
            can_id=0x601,
            remote=False,
            extended=False,
            data_len=5,
            data=(0x2F, 0x60, 0x60, 0x00, 0x01),
        )
        self.dev.send(0, new_message)
        return self.dev.recieve(0), self.dev.recieve(1)

    def actual_position(self) -> str:
        new_message = canalystii.Message(
            can_id=0x601,
            remote=False,
            extended=False,
            data_len=9,
            data=(0x23, 0x7A, 0x60, 0x00, 0x50, 0xC3, 0x00, 0x00, 0x00),
        )
        self.dev.send(0, new_message)
        return self.dev.recieve(0), self.dev.recieve(1)

    def trapezoidal_speed(self) -> str:
        new_message = canalystii.Message(
            can_id=0x601,
            remote=False,
            extended=False,
            data_len=7,
            data=(0x23, 0x81, 0x60, 0x00, 0xE8, 0x03, 0x00, 0x00),
        )
        self.dev.send(0, new_message)
        return self.dev.recieve(0), self.dev.recieve(1)

    def trapezoidal_acceleration(self) -> str:
        new_message = canalystii.Message(
            can_id=0x601,
            remote=False,
            extended=False,
            data_len=8,
            data=(0x23, 0x83, 0x60, 0x00, 0x20, 0x4E, 0x00, 0x00),
        )
        self.dev.send(0, new_message)
        return self.dev.recieve(0), self.dev.recieve(1)

    def control_word(self) -> str:
        new_message = canalystii.Message(
            can_id=0x601,
            remote=False,
            extended=False,
            data_len=7,
            data=(0x2B, 0x40, 0x60, 0x00, 0x00, 0x00, 0x00),
        )
        self.dev.send(0, new_message)
        return self.dev.recieve(0), self.dev.recieve(1)

    def location_cache(self) -> str:
        new_message = canalystii.Message(
            can_id=0x601,
            remote=False,
            extended=False,
            data_len=9,
            data=(0x23, 0x7A, 0x60, 0x00, 0x50, 0xC3, 0x00, 0x00, 0x00),
        )
        self.dev.send(0, new_message)
        return self.dev.recieve(0), self.dev.recieve(1)

    def status_word_read(self) -> str:
        new_message = canalystii.Message(
            can_id=0x601,
            remote=False,
            extended=False,
            data_len=4,
            data=(0x40, 0x41, 0x60, 0x00),
        )

        self.dev.send(0, new_message)
        return self.dev.recieve(0), self.dev.recieve(1)


class ServoSdoSpeedMode:
    def __init__(self, servo_interface: servo_interface.ServoInterface,) -> None:
        self.servo_interface = servo_interface

        self.dev = canalystii.CanalystDevice(
            bitrate=1000000, device_index=self.servo_interface.servo_id
        )

    def working_mode(self) -> str:
        new_message = canalystii.Message(
            can_id=0x601,
            remote=False,
            extended=False,
            data_len=5,
            data=(0x2F, 0x60, 0x60, 0x00, 0x03),
        )
        self.dev.send(0, new_message)
        return self.dev.recieve(0), self.dev.recieve(1)

    def speed_mode(self) -> str:
        new_message = canalystii.Message(
            can_id=0x601,
            remote=False,
            extended=False,
            data_len=9,
            data=(0x23, 0xFF, 0x60, 0x00, 0xF4, 0x01, 0x00, 0x00, 0x00),
        )

        self.dev.send(0, new_message)
        return self.dev.recieve(0), self.dev.recieve(1)

    def control_word(self) -> str:
        new_message = canalystii.Message(
            can_id=0x601,
            remote=False,
            extended=False,
            data_len=6,
            data=(0x2B, 0x40, 0x60, 0x00, 0x0F, 0x00),
        )
        self.dev.send(0, new_message)
        return self.dev.recieve(0), self.dev.recieve(1)

    def status_word(self) -> str:
        new_message = canalystii.Message(
            can_id=0x601,
            remote=False,
            extended=False,
            data_len=4,
            data=(0x40, 0x41, 0x60, 0x00),
        )

        self.dev.send(0, new_message)
        return self.dev.recieve(0), self.dev.recieve(1)


class ServoPdoControlTheProcessOfFindingTheOrigin:
    def __init__(self, servo_interface: servo_interface.ServoInterface,) -> None:
        self.servo_interface = servo_interface
        self.dev = canalystii.CanalystDevice(
            bitrate=1000000, device_index=self.servo_interface.servo_id
        )

    def find_the_origin(self) -> str:
        new_message = canalystii.Message(
            can_id=0x601,
            remote=False,
            extended=False,
            data_len=5,
            data=(0x2F, 0x98, 0x60, 0x00, 0x11),
        )
        self.dev.send(0, new_message)
        return self.dev.recieve(0), self.dev.recieve(1)

    def working_mode(self) -> str:
        new_message = canalystii.Message(
            can_id=0x601,
            remote=False,
            extended=False,
            data_len=5,
            data=(0x2F, 0x60, 0x60, 0x00, 0x06),
        )

        self.dev.send(0, new_message)
        return self.dev.recieve(0), self.dev.recieve(1)

    def status_word(self) -> str:
        new_message = canalystii.Message(
            can_id=0x601,
            remote=False,
            extended=False,
            data_len=4,
            data=(0x40, 0x41, 0x60, 0x00),
        )

        self.dev.send(0, new_message)
        return self.dev.recieve(0), self.dev.recieve(1)


class ServoPdoPositionMode(servo_interface.ServoPdoPositionModeInterface):
    def __init__(self, servo_interface: servo_interface.ServoInterface,) -> None:
        self.servo_interface = servo_interface

        self.dev = canalystii.CanalystDevice(
            bitrate=1000000, device_index=self.servo_interface.servo_id
        )

    def find_the_origin(self) -> str:
        new_message = canalystii.Message(
            can_id=0x301,
            remote=False,
            extended=False,
            data_len=10,
            data=(0x50, 0xC3, 0x00, 0x00, 0x00, 0xE8, 0x03, 0x00, 0x00, 0x00),
        )

        self.dev.send(0, new_message)
        return self.dev.recieve(0), self.dev.recieve(1)

    def target_position_trapezoidal_velocity_current_position_status_word(self) -> str:
        new_message = canalystii.Message(
            can_id=0x201,
            remote=False,
            extended=False,
            data_len=8,
            data=(0x2F, 0x00, 0x01, 0x50, 0xC3, 0x00, 0x00, 0x00),
        )

        self.dev.send(0, new_message)
        return self.dev.recieve(0), self.dev.recieve(1)

    def control_word_working_mode_target_position_current_position_status_word(
        self,
    ) -> str:
        new_message = canalystii.Message(
            can_id=0x301,
            remote=False,
            extended=False,
            data_len=10,
            data=(0x50, 0xC3, 0x00, 0x00, 0x00, 0xE8, 0x30, 0x00, 0x00, 0x00),
        )

        self.dev.send(0, new_message)
        return self.dev.recieve(0), self.dev.recieve(1)


class ServoPdoSpeedMode(servo_interface.ServoPdoSpeedModeInterface):
    def __init__(self, servo_interface: servo_interface.ServoInterface,) -> None:
        self.servo_interface = servo_interface

        self.dev = canalystii.CanalystDevice(
            bitrate=1000000, device_index=self.servo_interface.servo_id
        )

    def control_word_working_mode_target_speed_current_position_status_word(
        self,
    ) -> str:
        new_message = canalystii.Message(
            can_id=0x401,
            remote=False,
            extended=False,
            data_len=7,
            data=(0x0F, 0x00, 0x03, 0x58, 0x02, 0x00, 0x00),
        )

        self.dev.send(0, new_message)
        return self.dev.recieve(0), self.dev.recieve(1)


class ServoPdoPositionInterpolationMode(
    servo_interface.ServoPdoPositionInterpolationModeInterface
):
    def __init__(self, servo_interface: servo_interface.ServoInterface,) -> None:
        self.servo_interface = servo_interface

        self.dev = canalystii.CanalystDevice(
            bitrate=1000000, device_index=self.servo_interface.servo_id
        )

    def destination_location(self) -> str:
        new_message = canalystii.Message(
            can_id=0x501,
            remote=False,
            extended=False,
            data_len=4,
            data=(0x50, 0xC3, 0x00, 0x00),
        )
        self.dev.send(0, new_message)
        return self.dev.recieve(0), self.dev.recieve(1)

    def current_position_status_word(self) -> str:
        new_message = canalystii.Message(
            can_id=0x481,
            remote=False,
            extended=False,
            data_len=6,
            data=(0x78, 0x0D, 0x00, 0x00, 0x37, 0x04),
        )
        self.dev.send(0, new_message)
        return self.dev.recieve(0), self.dev.recieve(1)

    def target_location(self) -> str:
        new_message = canalystii.Message(
            can_id=0x501,
            remote=False,
            extended=False,
            data_len=4,
            data=(0x50, 0xC3, 0x00, 0x00),
        )
        self.dev.send(0, new_message)
        return self.dev.recieve(0), self.dev.recieve(1)
