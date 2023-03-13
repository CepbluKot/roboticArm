class ConfigCallbacksRepo:
    def __init__(self) -> None:
        self.repo = {} # servo_id: { val name: widget}
    
    def set(self, axis_id: int, call, value_name: str):
        if not axis_id in self.repo:
            self.repo[axis_id] = {}
    
        self.repo[axis_id][value_name] = call

    def getall(self):
        return self.repo

    def get(self, servo_id: int, value_name):
        if servo_id in self.repo:
            return self.repo[servo_id][value_name]
        else:
            return 0
