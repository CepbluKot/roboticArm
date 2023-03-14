import canalystii


class QueueMessage:
    def __init__(self, message: canalystii.Message, last_send_time: float) -> None:
        self.message = message
        self.attempts = 0
        self.last_send_time = last_send_time
