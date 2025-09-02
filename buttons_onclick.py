from thread_communication import send_cmd


def tare_button_onclick(button, ui_elements):
    #print(f"tare_button_onclick({tare_button}, {ui_elements})")
    send_cmd("LIVE_VIEW", "UI")
    print("Tare")

def calibrate_button_onclick(button, ui_elements):
    send_cmd("IDLE", "UI")
    print("Calibrate")

def test_button_onclick(button, ui_elements):
    send_cmd("EXIT", "UI")
    print("test")


