import typing
# import pydantic


class CommandData():
    def __init__(self, answer_code: int, send_address: int) -> None:
        self.send_address = send_address
        self.answer_code = answer_code


commands_storage: typing.Dict[str, CommandData] = {
    "60600008": CommandData(answer_code=580, send_address=0x600), # mode
    "60810020": CommandData(answer_code=580, send_address=0x600), # speed 
    "60640020": CommandData(answer_code=580, send_address=0x600), # pos
    "26140010": CommandData(answer_code=580, send_address=0x600), # save
    
}
