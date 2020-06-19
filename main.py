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
        # Create some custom styles.
        style.configure("Background.TFrame", background="#b8d8e0")
        
        style.configure("Background.TLabel", background="#b8d8e0")

        style.configure(
            "BackButton.TButton", background="#f2e3a0",
            bordercolor="black",
            font=("TkDefaultFont", 10),
            relief="solid"
        )
        style.map(
            "BackButton.TButton",
            background=[("active", "#edd97e")],
            font=[("active",  ("TkDefaultFont", 8))]
        )

        style.configure(
            "SearchButton.TButton", background="#f2e3a0",
            bordercolor="black",
            font=("TkDefaultFont", 16),
            relief="solid"
        )
        style.map(
            "SearchButton.TButton",
            background=[("active", "#edd97e")],
            font=[("active",  ("TkDefaultFont", 18))]
        )

        style.configure(
            "Background.TButton", background="#f2e3a0",
            bordercolor="black",
            relief="solid"
        )
        style.map(
            "Background.TButton",
            background=[("active", "#edd97e")],
            font=[("active",  ("TkDefaultFont", 22))]
        )
        
        style.configure(
            "LabelBackground.TButton", background="#a5c2c9",
            bordercolor="#859ca2",
            relief="solid",
            font=("System", 12),
        )
        style.map(
            "LabelBackground.TButton",
            background=[("active", "#94aeb4")],
        )

        # Set the widget's background.
        self["background"] = "#b8d8e0"
        # Give the Widget a name.
        self.title("Stock tracker")
        # Give the Widget a size.
        self.geometry("1400x740")
        # Center your Frame in the middle-top.
        self.columnconfigure(0, weight=1)

        # Set the overall fontsize to 15 instead of 10.
        font.nametofont("TkDefaultFont").configure(size=20)

        # Create all needed tk.-variables.
        # AddNewProd frame
        self.add_new_prod_barcode = tk.StringVar()
        self.add_new_prod_name = tk.StringVar()
        self.add_new_prod_amount = tk.StringVar()
        self.add_new_prod_price_piece = tk.StringVar()
        #  DeleteProd frame            #
        self.delete_prod_barcode = tk.StringVar()
        #             ScanProd frame             #
        self.scan_prod_barcode = tk.StringVar()
        #            UpdateStock frame           #
        self.update_stock_barcode = tk.StringVar()
        self.update_prod_name = tk.StringVar()
        self.update_prod_amount = tk.StringVar()
        self.update_prod_barcode = tk.StringVar()
        self.update_prod_price_piece = tk.StringVar()

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
        frame.redraw_tables()


GUI = StockTracker()
GUI.mainloop()
