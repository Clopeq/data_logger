
from time import time
import sys
from app import App

def main(): # UI consumer thread


    # init
    app = App()

    print(app.get_ui_element("tareButton"))
    
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
