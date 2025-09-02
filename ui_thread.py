from constants import UI_REFRESHRATE
from timeit import default_timer as timer
from queue import Queue
import random


def ui_loop(ui, ui_que: Queue, cmd_out: Queue, cmd_in: Queue):
    # init
    cmd = None
    total_timer = timer()
    STATE = "LIVE_VIEW"
    while True:
        delta_time = timer()

        # keep receiving commands even at low refreshrates. This keeps the UI more responisve
        while timer()-delta_time < 1/UI_REFRESHRATE: # block the ui_loop to achieve desired refreshrate
            cmd = receive_que(cmd_in)

            # evaluate mcd
            if cmd == "EXIT":
                print("UI EXIT")
                return 0
            
            if cmd == "LIVE_VIEW":
                print("ui_loop: {STATE} -> LIVE_VIEW")
                STATE = "LIVE_VIEW"
                cmd = None
            
            if cmd == "IDLE":
                print("ui_loop: {STATE} -> IDLE")
                STATE = "IDLE"
                cmd = None
            
        # receive data

        # evaluate the data
        if STATE == "LIVE_VIEW":
            live_view(ui_que, ui["titleLabel"])


        

    


    # Do something with the data

    # update UI


def live_view(que, label):
    # receive data from the que, and display in on the label

    data = receive_que(que)
    if data == None:
        label.setText("No data")
    else: 
        label.setText(str(data))

    return data


def receive_que(que: Queue):
    if que.empty() == False:
        try:
            cmd = que.get(timeout=0.05)
        except:
            cmd = None
    else:
        cmd = None

    return cmd

