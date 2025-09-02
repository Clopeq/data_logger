from PySide6.QtWidgets import QPushButton, QLabel, QLineEdit
from buttons_onclick import *

UI_FILE = "app.ui"
UI_REFRESHRATE = 12
UI_ELEMENTS = {
    "tareButton": QPushButton,
    "titleLabel": QLabel,
    "calibrateButton": QPushButton,
    "actualValue": QLineEdit,
    "testButton": QPushButton
}

BUTTON_ONCLICK = {
    "tareButton": tare_button_onclick,
    "calibrateButton": calibrate_button_onclick,
    "testButton": test_button_onclick
}