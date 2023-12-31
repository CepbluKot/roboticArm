from tkinter import *


class GeneralParamsRepo:
    def __init__(self) -> None:
        self.repo = {} # servo_id: { val name: widget}
    
    def set(self, axis_id: int, widget, value_name: str):
        if not axis_id in self.repo:
            self.repo[axis_id] = {}

        print('added ', value_name)

        self.repo[axis_id][value_name] = widget

    def getall(self):
        return self.repo

    def get(self, servo_id: int, value_name) -> Label:
        if servo_id in self.repo:
            if value_name in self.repo[servo_id]:
                return self.repo[servo_id][value_name]
        else:
            return 0
