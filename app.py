
from PySide6.QtWidgets import QApplication, QPushButton, QLabel, QLineEdit
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QObject, Signal
from constants import BUTTON_ONCLICK, UI_FILE, UI_ELEMENTS
from button import Button
from buttons_onclick import *

"""
class Widget():
    def __init__(self, app):
        self.__ui_elements = app.get

class Button(Widget):



class Label():
    self.label = ""

class LineEdit():

    def get_text():
"""
    



class App():
    def __init__(self):
        self.__app = QApplication([]) # initialize application
        self.__window = self.__load_ui(UI_FILE)
        self.__window.show()
        self.__ui_elements = self.__load_ui_elements(self.__window)

        self.__init_buttons(self.__ui_elements)


    
    def __init_buttons(self, ui_elements):
        buttons = {}
        for element in ui_elements:
            if UI_ELEMENTS[element] == QPushButton:
                qbutton = ui_elements[element]
                onclick = BUTTON_ONCLICK[element]
                buttons[element] = Button(qbutton, onclick, ui_elements, args=(qbutton, ui_elements))

        return buttons


    def exec(self):
        """
        Starts the application

        WARNING! This is an infinite loop, make sure all of the threads and initialization happens before this method is called
        """
        return self.__app.exec()
    
    def get_all_ui_elements(self):
        return self.__ui_elements
        
    def get_ui_element(self, element):
        if element in self.__ui_elements:
            ui_element = (self.__ui_elements[element], element)
        else:
            raise ValueError(f"App.get_ui_element() the UI element has not been found: {element}")
        return ui_element
    


    def __load_ui_elements(self, window):
        ui_elements = {}
        for element in UI_ELEMENTS:
            qtype = UI_ELEMENTS[element] # QPushButton, QLabel, etc.

            ui_elements[element] = window.findChild(qtype, element)

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
        
    

    