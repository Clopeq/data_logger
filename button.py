
from PySide6.QtWidgets import QPushButton

class Button(QPushButton):
    def __init__(self, button, on_click_func, ui_elements, args=None, *Qargs, **kwargs):
        super().__init__(*Qargs, **kwargs)
        self.ui_elements = ui_elements
        self.button = button
        self.on_click_func = on_click_func
        self.set_on_click(self.button, self.on_click_func, args)

    def set_on_click(self, button, on_click_func, args=None):
        """
        button: .findChild(QPushButton, "buttonName")
        on_click_func: a function which is to be executed when the button is pressed
        args: arguments for the on_click_func
        """

        if args == None:
            func = lambda: on_click_func()
        else:
            func = lambda: on_click_func(*args)

        button.clicked.connect(func)

