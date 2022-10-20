import typing
# import pydantic


class CommandData():
    def __init__(self, answer_code: int, send_address: int) -> None:
        self.send_address = send_address
        self.answer_code = answer_code


class ServoData():
    def __init__(self, speed: int, pos: int, mode: int) -> None:
        self.speed = speed
        self.pos = pos
        self.mode = mode


commands_info_storage: typing.Dict[str, CommandData] = {
    "60600008": CommandData(answer_code=0x580, send_address=0x600), # mode
    "60810020": CommandData(answer_code=0x580, send_address=0x600), # speed 
    "60640020": CommandData(answer_code=0x580, send_address=0x600), # pos
    "26140010": CommandData(answer_code=0x580, send_address=0x600), # save    
    '606C0010': CommandData(answer_code=0x580, send_address=0x600),
}


servo_info_storage: typing.Dict[int, ServoData] = {}
