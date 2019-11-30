#Morgan Foster
#1021803
# GUI Programming

# Imports
import tkinter

# Creating a Window
def create_window():
    main_window = tkinter.Tk()  # Creates window object
    tkinter.mainloop()  # Keeps the window open

create_window()

# Creating Gui Class
class MyGui:
    def __init__( self ):
        self.main_window = tkinter.Tk()
        tkinter.mainloop()

my_gui = MyGui()

# Need Frames to hold Widgets
