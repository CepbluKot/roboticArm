from servo_realisation.output import robot


def save_settings_first_axis_call():
    robot.save_settings(1)

def save_settings_sec_axis_call():
    robot.save_settings(2)

def save_settings_third_axis_call():
    robot.save_settings(3)

def save_settings_fourth_axis_call():
    robot.save_settings(4)

def save_settings_fifth_axis_call():
    robot.save_settings(5)

def save_settings_sixth_axis_call():
    robot.save_settings(6)


save_settings_calls_output = {1:save_settings_first_axis_call, 2:save_settings_sec_axis_call, 3:save_settings_third_axis_call, 4:save_settings_fourth_axis_call, 5:save_settings_fifth_axis_call, 6:save_settings_sixth_axis_call}
