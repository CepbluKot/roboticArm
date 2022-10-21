# import pydantic


class RecievedCommand():
    def __init__(self, id: int, ts: str, data: str) -> None:
        self.id = id
        self.ts = ts
        self.data = data
        self.servo_id = int()
        self.decoded_data = int()
        self.command_data = str()
