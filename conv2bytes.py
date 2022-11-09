import threading
import copy

class MessagesBuffer:
    def __init__(self, lock: threading.Lock) -> None:
        self.messages_buffer = {}
        self.lock = lock

    def get(self):
        with self.lock:
            return copy.deepcopy(self.messages_buffer)

    def set(self, command_id, servo_id):
        with self.lock:
            return self.messages_buffer[command_id][servo_id]

    def delete(self, command_id, servo_id):
        with self.lock:
            if command_id in self.messages_buffer:
                self.messages_buffer[command_id].pop(servo_id)

globl_lock = threading.Lock()
buf = MessagesBuffer(globl_lock)

thr1 = threading.Thread


def thread1(buffer: MessagesBuffer):
    data = buffer.get()
    data[]
