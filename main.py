
from time import time
import sys
from app import App

def foo():
    print("foo")

def main(): # UI consumer thread


    # init
    app = App()

    tare_button = app.get_ui_element("tareButton")

    tare_button.on_click(func, args)
    
    app.exec()


    # loop
    t = time()
    while time()-t < 3:
        print(time()-t)
        t2 = time()
        while time()-t2 < 1:
            pass


if __name__ == "__main__":
    main()
