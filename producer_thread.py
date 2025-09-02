import platform
from random import randint
from timeit import default_timer as timer
from thread_communication import receive_que
from queue import Queue

def producer_loop(ui_refreshrate, writer_que: Queue, ui_que: Queue, cmd_out: Queue, cmd_in: Queue):
    cmd = None
    t = timer()
    STATE = "IDLE"

    while True:

        # evaluate cmd
        STATE = evaluate_cmd(STATE, cmd_in)
        if STATE == "EXIT":
            return
        
        if STATE == "IDLE":
            continue

        if timer() - t > 1/ui_refreshrate:
            ques = (writer_que, ui_que)
            t = timer()
        else:
            ques = (writer_que,)
        
        push_data(ques)


def push_data(ques):
    data = gather_data()
    for que in ques:
        if que.full():
            que.get_nowait()
        que.put_nowait(data)
        
            
            
def gather_data():
    if platform.node() == "DAQ":
        # running on raspberry pi
        return [0,1,2,3,4,5,6,7,8,9]
    else:
        return [randint(1,1023) for _ in range(10)]
    
def evaluate_cmd(state, que):
    cmd = receive_que(que)

    # evaluate mcd
    if cmd == "EXIT":
        print("PRODUCER EXIT")
        state = "EXIT"
    
    if cmd == "GATHER":
        print(f"PRODUCER: {state} -> GATHER")
        state = "GATHER"
    
    if cmd == "IDLE":
        print(f"PRODUCER: {state} -> IDLE")
        state = "IDLE"

    return state