from queue import Queue

PRODUCER_CMD_OUT = Queue()
PRODUCER_CMD_IN = Queue()
WRITER_CMD_OUT = Queue()
WRITER_CMD_IN = Queue()
UI_CMD_OUT = Queue()
UI_CMD_IN = Queue()
WRITER_QUE = Queue()
UI_QUE = Queue(maxsize=3)

que_dict = {
    "PRODUCER": PRODUCER_CMD_IN,
    "WRITER": WRITER_CMD_IN,
    "UI": UI_CMD_IN,
}

def send_cmd(command, receiver):
    if not (receiver in que_dict):
        raise ValueError(f"Receiver has not been found: {receiver}")
    
    que_dict[receiver].put(command)