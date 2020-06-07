import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from frames.start_page import StartPage
from frames.stock_page import StockPage
from frames.add_new_product import AddNewProd
from frames.delete_product import DeleteProd
from frames.update_stock import UpdateStock
from frames.scan_product import ScanProd
from frames.update_stock import UpdateStock
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)


# Create a Tkinter Widget.
class StockTracker(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = ttk.Frame(self)
        container.grid()

        # Set the style to 'clam'.
        style = ttk.Style()
        style.theme_use("clam")
        
        # Give the Widget a name.
        self.title("Stock tracker")
        # Give the Widget a size.
        self.geometry("1450x780")
        # Center your Frame in the middele-top.
        self.columnconfigure(0, weight=1)

        # Set the overall fontsize to 15 instead of 10.
        font.nametofont("TkDefaultFont").configure(size=20)

        self.frames = {}

        for F in (StartPage, StockPage, AddNewProd, DeleteProd, UpdateStock, ScanProd, UpdateStock):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="NSEW")

        self.show_frame("StartPage")
        
    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
        frame.focus_on_entry()

GUI = StockTracker()
GUI.mainloop()
