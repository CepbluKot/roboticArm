from servo_realisation import servo_interface
import canalystii

class ServoAbstraction:
    servo_id: int


class ServoSdoAbsolutePositionModeAbstraction:
    def control_word_1(self) -> str:
        new_message = canalystii.Message(
    can_id=0x601,
    remote=False,
    extended=False,
    data_len=6,
    data=(0x2b, 0x40, 0x60, 0x00, 0x0f, 0x00),
)

    def working_mode(self) -> str:
        new_message = canalystii.Message(
    can_id=0x601,
    remote=False,
    extended=False,
    data_len=5,
    data=(0x2F, 0x60, 0x60, 0x00, 0x01),
)

    def actual_position(self) -> str:
        new_message = canalystii.Message(
    can_id=0x601,
    remote=False,
    extended=False,
    data_len=4,
    data=(0x40, 0x64, 0x60, 0x00),
)

    def trapezoidal_speed(self) -> str:
        new_message = canalystii.Message(
    can_id=0x601,
    remote=False,
    extended=False,
    data_len=8,
    data=(0x23, 0x81, 0x60, 0x00, 0xe8, 0x03, 0x00, 0x00),
)

    def trapezoidal_acceleration(self) -> str:
        new_message = canalystii.Message(
    can_id=0x601,
    remote=False,
    extended=False,
    data_len=8,
    data=(0x23, 0x83, 0x60, 0x00, 0x20, 0x4E, 0x00, 0x00),
)

    def control_word_2(self) -> str:
        new_message = canalystii.Message(
    can_id=0x601,
    remote=False,
    extended=False,
    data_len=6,
    data=(0x2b, 0x40, 0x60, 0x00, 0x2f, 0x00),
)

    def location_cache(self) -> str:
        new_message = canalystii.Message(
    can_id=0x601,
    remote=False,
    extended=False,
    data_len=8,
    data=(0x23, 0x7A, 0x60, 0x00, 0x50, 0xC3, 0x00, 0x00),
)

    def status_word_read(self) -> str:
        new_message = canalystii.Message(
    can_id=0x601,
    remote=False,
    extended=False,
    data_len=4,
    data=(0x40, 0x41, 0x60, 0x00),
)


class ServoSdoRelativePositionModeAbstraction:
    def control_word(self) -> str:
        new_message = canalystii.Message(
    can_id=0x601,
    remote=False,
    extended=False,
    data_len=6,
    data=(0x2b, 0x40, 0x60, 0x00, 0x0f, 0x00),
)

    def working_mode(self) -> str:
        new_message = canalystii.Message(
    can_id=0x601,
    remote=False,
    extended=False,
    data_len=5,
    data=(0x2f, 0x60, 0x60, 0x00, 0x01),
)

    def actual_position(self) -> str:
        new_message = canalystii.Message(
    can_id=0x601,
    remote=False,
    extended=False,
    data_len=9,
    data=(0x23, 0x7a, 0x60, 0x00, 0x50, 0xC3, 0x00, 0x00, 0x00),
)

    def trapezoidal_speed(self) -> str:
        new_message = canalystii.Message(
    can_id=0x601,
    remote=False,
    extended=False,
    data_len=7,
    data=(0x23, 0x81, 0x60, 0x00, 0xe8, 0x03, 0x00, 0x00),
)

    def trapezoidal_acceleration(self) -> str:
        new_message = canalystii.Message(
    can_id=0x601,
    remote=False,
    extended=False,
    data_len=8,
    data=(0x23, 0x83, 0x60, 0x00, 0x20, 0x4e, 0x00, 0x00),
)

    def control_word(self) -> str:
        new_message = canalystii.Message(
    can_id=0x601,
    remote=False,
    extended=False,
    data_len=7,
    data=(0x2b, 0x40, 0x60, 0x00, 0x00, 0x00, 0x00),
)

    def location_cache(self) -> str:
        new_message = canalystii.Message(
    can_id=0x401,
    remote=False,
    extended=False,
    data_len=7,
    data=(0x0F, 0x00, 0x03, 0x00, 0x00, 0x00, 0x00),
)

    def status_word_read(self) -> str:
        new_message = canalystii.Message(
    can_id=0x401,
    remote=False,
    extended=False,
    data_len=7,
    data=(0x0F, 0x00, 0x03, 0x00, 0x00, 0x00, 0x00),
)


class ServoSdoSpeedModeAbstraction:
    def working_mode(self) -> str:
        new_message = canalystii.Message(
    can_id=0x401,
    remote=False,
    extended=False,
    data_len=7,
    data=(0x0F, 0x00, 0x03, 0x00, 0x00, 0x00, 0x00),
)

    def speed_mode(self) -> str:
        new_message = canalystii.Message(
    can_id=0x401,
    remote=False,
    extended=False,
    data_len=7,
    data=(0x0F, 0x00, 0x03, 0x00, 0x00, 0x00, 0x00),
)

    def control_word(self) -> str:
        new_message = canalystii.Message(
    can_id=0x401,
    remote=False,
    extended=False,
    data_len=7,
    data=(0x0F, 0x00, 0x03, 0x00, 0x00, 0x00, 0x00),
)

    def status_word(self) -> str:
        new_message = canalystii.Message(
    can_id=0x401,
    remote=False,
    extended=False,
    data_len=7,
    data=(0x0F, 0x00, 0x03, 0x00, 0x00, 0x00, 0x00),
)


class ServoPdoControlTheProcessOfFindingTheOriginAbstraction:
    def find_the_origin(self) -> str:
        new_message = canalystii.Message(
    can_id=0x401,
    remote=False,
    extended=False,
    data_len=7,
    data=(0x0F, 0x00, 0x03, 0x00, 0x00, 0x00, 0x00),
)

    def working_mode(self) -> str:
        new_message = canalystii.Message(
    can_id=0x401,
    remote=False,
    extended=False,
    data_len=7,
    data=(0x0F, 0x00, 0x03, 0x00, 0x00, 0x00, 0x00),
)

    def status_word(self) -> str:
        new_message = canalystii.Message(
    can_id=0x401,
    remote=False,
    extended=False,
    data_len=7,
    data=(0x0F, 0x00, 0x03, 0x00, 0x00, 0x00, 0x00),
)


class ServoPdoPositionModeAbstraction(servo_interface.ServoPdoPositionModeInterface):
    def find_the_origin(self) -> str:
        new_message = canalystii.Message(
    can_id=0x401,
    remote=False,
    extended=False,
    data_len=7,
    data=(0x0F, 0x00, 0x03, 0x00, 0x00, 0x00, 0x00),
)

    def target_position_trapezoidal_velocity_current_position_status_word(self) -> str:
        new_message = canalystii.Message(
    can_id=0x401,
    remote=False,
    extended=False,
    data_len=7,
    data=(0x0F, 0x00, 0x03, 0x00, 0x00, 0x00, 0x00),
)

    def control_word_working_mode_target_position_current_position_status_word(
        self,
    ) -> str:
        new_message = canalystii.Message(
    can_id=0x401,
    remote=False,
    extended=False,
    data_len=7,
    data=(0x0F, 0x00, 0x03, 0x00, 0x00, 0x00, 0x00),
)


class ServoPdoSpeedModeAbstraction(servo_interface.ServoPdoSpeedModeInterface):
    def control_word_working_mode_target_speed_current_position_status_word(
        self,
    ) -> str:
        new_message = canalystii.Message(
    can_id=0x401,
    remote=False,
    extended=False,
    data_len=7,
    data=(0x0F, 0x00, 0x03, 0x00, 0x00, 0x00, 0x00),
)


class ServoPdoPositionInterpolationModeAbstraction(
    servo_interface.ServoPdoPositionInterpolationModeInterface
):
    def destination_location(self) -> str:
        new_message = canalystii.Message(
    can_id=0x401,
    remote=False,
    extended=False,
    data_len=7,
    data=(0x0F, 0x00, 0x03, 0x00, 0x00, 0x00, 0x00),
)

    def current_position_status_word(self) -> str:
        new_message = canalystii.Message(
    can_id=0x401,
    remote=False,
    extended=False,
    data_len=7,
    data=(0x0F, 0x00, 0x03, 0x00, 0x00, 0x00, 0x00),
)

    def target_location(self) -> str:
        new_message = canalystii.Message(
    can_id=0x401,
    remote=False,
    extended=False,
    data_len=7,
    data=(0x0F, 0x00, 0x03, 0x00, 0x00, 0x00, 0x00),
)
