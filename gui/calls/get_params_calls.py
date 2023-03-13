import canalystii
from servo_realisation.protocol_interface.CanOpen301 import CanOpen301, ReceievedMessage
from gui.general_params_tab.storages.output import general_params_repo
from servo_realisation.axis_positions_storage import current_positions


def on_read_speed_gui_call(receieved_message: ReceievedMessage):
    widget = general_params_repo.get(receieved_message.servo_id, 'speed')
    if widget:
        widget.config(text=receieved_message.decoded_data)

def on_read_accel_gui_call(receieved_message: ReceievedMessage):
    widget =general_params_repo.get(receieved_message.servo_id, 'accel')
    if widget:
        widget.config(text=receieved_message.decoded_data)

def on_read_mode_gui_call(receieved_message: ReceievedMessage):
    widget =general_params_repo.get(receieved_message.servo_id, 'mode')
    if widget:
        widget.config(text=receieved_message.decoded_data)

def on_read_pos_gui_call(receieved_message: ReceievedMessage):

    current_positions[receieved_message.servo_id] = receieved_message.decoded_data

    widget =general_params_repo.get(receieved_message.servo_id, 'positon')
    if widget:
        widget.config(text=receieved_message.decoded_data)

def on_read_target_pos_gui_call(receieved_message: ReceievedMessage):
    widget =general_params_repo.get(receieved_message.servo_id, 'target position')
    if widget:
        widget.config(text=receieved_message.decoded_data)
        
def on_read_error_check_gui_call(receieved_message: ReceievedMessage):
    widget =general_params_repo.get(receieved_message.servo_id, 'error code')
    if widget:
        widget.config(text=receieved_message.decoded_data)
        
def on_voltage_check_gui_call(receieved_message: ReceievedMessage):
    widget =general_params_repo.get(receieved_message.servo_id, 'voltage')
    if widget:
        widget.config(text=receieved_message.decoded_data/327)
        
def on_temperature_check_gui_call(receieved_message: ReceievedMessage):
    widget =general_params_repo.get(receieved_message.servo_id, 'temperature')
    if widget:
        widget.config(text=receieved_message.decoded_data)

def on_current_check_gui_call(receieved_message: ReceievedMessage):
    widget =general_params_repo.get(receieved_message.servo_id, 'current')
    if widget:
        widget.config(text=receieved_message.decoded_data)
        
def on_pwm_check_gui_call(receieved_message: ReceievedMessage):
    pass

def on_saved_parameters_check_gui_call(receieved_message: ReceievedMessage):
    pass

def on_speed_loop_integration_time_gui_call(receieved_message: ReceievedMessage):
    pass
