from typing import Dict


def syncronise(movement_time: int, current_positions: Dict[int, int], target_positions: Dict[int, int]):
    speeds = {}
    for servo_id in current_positions:
        delta = abs(current_positions[servo_id] - target_positions[servo_id])
        print('delta', servo_id,  delta)
        speeds[servo_id] = delta / movement_time
    
    return speeds

move_time = 3
current_positions = {1:1000, 2:250, 3:500, 4:750, 5:999, 6:132}
target_positions = {1:2000,2:0,3:123,4:1500,5:250,6:500}

res = syncronise(move_time, current_positions, target_positions)
print(res)
