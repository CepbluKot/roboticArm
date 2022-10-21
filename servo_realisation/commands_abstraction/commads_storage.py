import typing
# import pydantic

import servo_realisation.control_objects.servo_interface

class CommandData():
    def __init__(self, answer_code: int, send_address: int) -> None:
        self.send_address = send_address
        self.answer_code = answer_code


class ServoCommandData():
    def __init__(self, answer_code: int, send_address: int, value_link, is_new_value: bool) -> None:
        self.send_address = send_address
        self.answer_code = answer_code
        self.value_link = value_link
        self.is_new_value = is_new_value


class ServoData():
    speed = -1
    pos = -1
    mode = -1
    servo_id = -1
    commands_info_storage: typing.Dict[str, ServoCommandData] = {
        "6060": ServoCommandData(answer_code=0x580+servo_id, send_address=0x600+servo_id, value_link=mode, is_new_value=0), # mode
        "6081": ServoCommandData(answer_code=0x580+servo_id, send_address=0x600+servo_id, value_link=speed, is_new_value=0), # speed 
        "6064": ServoCommandData(answer_code=0x580+servo_id, send_address=0x600+servo_id, value_link=pos, is_new_value=0), # pos
    }

    def __init__(self, speed_value: int, pos_value: int, mode_value: int, servo_object: servo_realisation.control_objects.servo_interface.ServoInterface) -> None:
        self.speed = speed_value
        self.pos = pos_value
        self.mode = mode_value
        self.servo_id = servo_object.servo_id


general_commands_info_storage: typing.Dict[str, CommandData] = {
    "60600008": CommandData(answer_code=0x580, send_address=0x600), # mode
    "60810020": CommandData(answer_code=0x580, send_address=0x600), # speed 
    "60640020": CommandData(answer_code=0x580, send_address=0x600), # pos
    "26140010": CommandData(answer_code=0x580, send_address=0x600), # save    
    '606C0010': CommandData(answer_code=0x580, send_address=0x600), 
}


servo_info_storage: typing.Dict[int, ServoData] = {}
