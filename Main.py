import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from frames import StartPage, Page1, Page2, Page3, Page4, Page5
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)


# Create a Tkinter Widget.
class BasementGui(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = ttk.Frame(self)
        container.grid()

        # Set the style to 'clam'.
        style = ttk.Style()
        style.theme_use("clam")
        
        # Give the Frame a name.
        self.title("Basement stock")
        # Give the Frame a size.
        self.geometry("505x280")
        # Center your Frame in the middele-top.
        self.columnconfigure(0, weight=1)

        # Set the overall fontsize to 15 instead of 10.
        font.nametofont("TkDefaultFont").configure(size=15)

        self.frames = {}

        for F in (StartPage, Page1, Page2, Page3, Page4, Page5):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")
        
    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

GUI = BasementGui()
GUI.mainloop()