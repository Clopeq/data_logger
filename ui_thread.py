
from timeit import default_timer as timer
from queue import Queue
import random
from thread_communication import receive_que


def ui_loop(ui, ui_refreshrate, ui_que: Queue, cmd_out: Queue, cmd_in: Queue):
    # init
    cmd = None
    total_timer = timer()
    STATE = "LIVE_VIEW"
    refreshrate = ui_refreshrate

    while True:
        delta_time = timer()

        # keep receiving commands even at low refreshrates. This keeps the UI more responisve
        while timer()-delta_time < 1/refreshrate: # block the ui_loop to achieve desired refreshrate
            STATE = evaluate_cmd(STATE, cmd_in, ui)
            if STATE == "EXIT":
                return
            
        # receive data

        # evaluate the data
        if STATE == "LIVE_VIEW":
            live_view(ui_que, ui["titleLabel"])


    # Do something with the data

    # update UI

def evaluate_cmd(state, que, ui):
    cmd = receive_que(que)

    # evaluate mcd
    if cmd == "EXIT":
        print("UI EXIT")
        return 0
    
    if cmd == "LIVE_VIEW":
        print(f"UI: {state} -> LIVE_VIEW")
        state = "LIVE_VIEW"
    
    if cmd == "IDLE":
        print(f"UI: {state} -> IDLE")
        state = "IDLE"

    return state

def live_view(que, label):
    # receive data from the que, and display in on the label

    data = receive_que(que)
    if data == None:
        label.setText("No data")
    else: 
        label.setText(str(data[0]))

    return data




