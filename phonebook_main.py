


import tkinter as tk4
from tkinter import *

# Be sure to import other modules if needed (we need them) so you have access to them!
import phonebook_gui
import phonebook_func


# Frame is the tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self,master,*args,**kwargs):
        Frame.__init__(self,master,*args,**kwargs)

        # define our master frame configuration:
        self.master=master
        self.master.minsize(500,300)
        self.master.maxsize(500,300)
        # This CenterWindow method will canter our app on the user's screen
        phonebook_func.center_window(self,500,300)
        self.master.title("The Tkinter Phonebook Demo")
        self.master.configure(bg="#002240")
        # This protocol method is a tkinter built-in method to catch if
        # the user clicks the upper corner "X" on windows OS
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg=self.master

        # load in the GUI widgets from a seperate module,
        # keeping the code compartmentalized and clutter free
        phonebook_gui.load_gui(self)


        

if __name__=="__main__":
    root=tk.Tk()
    App=ParentWindow(root)
    root.mainloop()
