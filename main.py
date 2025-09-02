from app import App
from threading import Thread
from producer_thread import producer_loop
from thread_communication import PRODUCER_CMD_IN, PRODUCER_CMD_OUT, WRITER_CMD_IN, WRITER_CMD_OUT, UI_CMD_OUT, UI_CMD_IN, WRITER_QUE, UI_QUE, send_cmd
from ui_thread import ui_loop



def main():
    app = App()

    producer_thread = Thread(target=producer_loop, args=(WRITER_QUE, UI_QUE, PRODUCER_CMD_OUT, PRODUCER_CMD_IN), daemon=True)
    ui_thread = Thread(target=ui_loop, args=(app.get_all_ui_elements(), UI_QUE, UI_CMD_OUT, UI_CMD_IN), daemon=True)
    # writer_thread = Thread(target=writer_consumer, args=(writerQueue, writerCMD))

    producer_thread.start()
    ui_thread.start()


    app.exec()

    # Gracefully terminate all threads

    send_cmd("EXIT", "UI")
    send_cmd("EXIT", "PRODUCER")

    producer_thread.join(timeout=2)
    ui_thread.join(timeout=2)


if __name__ == "__main__":
    main()
