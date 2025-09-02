from thread_communication import send_cmd


def tare_button_onclick(button, ui_elements):
    #print(f"tare_button_onclick({tare_button}, {ui_elements})")
    send_cmd("LIVE_VIEW", "UI")
    send_cmd("GATHER", "PRODUCER")

def calibrate_button_onclick(button, ui_elements):
    send_cmd("IDLE", "UI")
    send_cmd("IDLE", "PRODUCER")

def test_button_onclick(button, ui_elements):
    send_cmd("EXIT", "UI")
    send_cmd("EXIT", "PRODUCER")


