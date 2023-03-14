from servo_realization.output import robot
from gui.output import speed


def set_speed_call(value):
    global speed
    speed = value
    robot.send_all_axis_speeds(float(value))
