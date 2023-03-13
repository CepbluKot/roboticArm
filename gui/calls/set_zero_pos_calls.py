from servo_realisation.output import robot


def set_zero_pos_first_axis_call():
    robot.send_zero_pos(1)

def set_zero_pos_sec_axis_call():
    robot.send_zero_pos(2)

def set_zero_pos_third_axis_call():
    robot.send_zero_pos(3)

def set_zero_pos_fourth_axis_call():
    robot.send_zero_pos(4)

def set_zero_pos_fifth_axis_call():
    robot.send_zero_pos(5)

def set_zero_pos_sixth_axis_call():
    robot.send_zero_pos(6)


set_zero_pos_calls_output = {1:set_zero_pos_first_axis_call, 2:set_zero_pos_sec_axis_call, 3:set_zero_pos_third_axis_call, 4:set_zero_pos_fourth_axis_call, 5:set_zero_pos_fifth_axis_call, 6:set_zero_pos_sixth_axis_call} 
