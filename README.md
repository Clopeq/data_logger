<!-- <p align="center">
  <img src="https://api.boot.dev/v1/users/public/23b1e6c6-9f95-4efa-9b5e-ab54571b0a85/thumbnail" >
</p> -->


# Adding new UI elements
you have to add elements manually to the constants.py file, otherwise they will not be accesible from within the code. This is how to properly add new ui elements:
1. Open **QtDesigner** app.
2. Add the UI element of your desire
3. Name the UI element in the **"objectName"** field. (You will need this name later)
4. Open **constants.py**.
5. Edit **UI_ELEMENTS** dictionary to contain your new UI element in the format **"objectName": Qtype**
6. Done!


# Adding button functionality
1. First add the ui element as described above
2. open **buttons_onclick.py**
3. write a new function which takes exactly 2 arguments:
  - the reference to the QPushButton you have just added. You can use it to change the apperance of your button dynamically
  - the reference to all of the UI elements in the window. You can use it to manipulate other ui elements, eg. labels
4. open **constants.py**
5. edit **BUTTON_ONCLICK** dictionary in the following format: **"objectName": on_click_function**