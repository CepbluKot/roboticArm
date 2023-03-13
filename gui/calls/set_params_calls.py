from servo_realisation.output import robot


def set_speed_call(value):
    robot.send_all_axis_speeds(float(value))

def set_accel_call(value):
    robot.send_all_axis_acceleration(float(value))

def set_sync_call(value):
    # robot.set_speed(60)
    pass
