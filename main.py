
from time import time
from app import App
# from button import TareButton



def main(): # UI consumer thread

    # init
    app = App()
    # tare_button = TareButton(app.get_ui_element("tareButton"))

    # tare_button = app.get_ui_element("tareButton")
    # app.set_on_click("tareButton", func)
    # app.set_label("")

    # tare_button.on_click(func, args)
    
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
