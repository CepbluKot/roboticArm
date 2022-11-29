import servo_realisation.protocol_interface.CanOpen301
import servo_realisation.hardware_interface.USB_CAN
import canalystii, time


def modify_accel(amgus):
    pass


def modify_mode():
    pass


def modify_pos():
    pass


def modify_speed():
    pass


def modify_target_pos():
    pass


dev = servo_realisation.hardware_interface.USB_CAN.USB_CAN(0)
protocol = servo_realisation.protocol_interface.CanOpen301.CanOpen301(
    device=dev,
    on_read_accel=modify_accel,
    on_read_mode=modify_mode,
    on_read_pos=modify_pos,
    on_read_speed=modify_speed,
    on_read_target_pos=modify_target_pos,
)
time.sleep(1)
