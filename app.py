
from PySide6.QtWidgets import QApplication, QPushButton, QLabel, QLineEdit
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QObject, Signal
from constants import UI_FILE, UI_ELEMENTS
import sys



class App():
    def __init__(self):
        self.__app = QApplication([]) # initialize application
 
        self.__window = self.__load_ui(UI_FILE)
        self.__window.show()

        self.ui_elements = self.__load_ui_elements(self.__window)

    
    def exec(self):
        """
        Starts the application

        WARNING! This is an infinite loop, make sure all of the threads and initialization happens before this method is called
        """
        return self.__app.exec()
    
    def on_click(self, button, on_click_func, args=None):
        """
        button: .findChild(QPushButton, "buttonName")
        on_click_func: a function which is to be executed when the button is pressed
        args: arguments for the on_click_func
        """

        if args == None:
            func = lambda: on_click_func()
        else:
            func = lambda: on_click_func(args)

        if button is not None:
            button.clicked.connect(func)
        else:
            raise Exception(f"Error: '{button}' not found in the TUI")
        
    def __load_ui_elements(self, window):
        ui_elements = {}
        for element in UI_ELEMENTS:
            ui_elements[element] = window.findChild(UI_ELEMENTS[element], element)

        return ui_elements

    def __load_ui(self, ui_file_path, ):
        """
        Loads the .ui file from the ui_file_path and returns the QMainWindow widged
        """
        
        # load the UI
        ui_file = QFile(ui_file_path)
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        local_window = loader.load(ui_file)
        ui_file.close()

        if local_window is None:
            raise Exception(f"Error: Failed to load UI from {ui_file_path}")

        return local_window