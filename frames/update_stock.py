import tkinter as tk
from tkinter import ttk
from tkintertable import TableCanvas
import requests
import time


class UpdateStock(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)

        self.controller = controller
        # Center your Frame, all the entry's and labels in the middle. 
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.search_entry = ttk.Entry(
            self,
            textvariable=controller.update_stock_barcode,
            width=24,
            font=("TkDefaultFont 15")
        )
        self.search_entry.grid(row=0, column=0, padx=(72, 12), sticky="W")

        def bind_entry_field(event):
            print(controller.update_stock_barcode.get())
            time.sleep(1) # Sleep for 1 seconds
            self.search_entry.delete(0, 'end')
            self.get_tables()

        # Bind 'Enter' to the Enty field.
        self.search_entry.bind('<Return>', bind_entry_field)

        # Add some buttons.
        search_button = ttk.Button(
            self,
            text="🔍",
            command=lambda: [self.search_entry.focus(), bind_entry_field(None)],
            width=3
        )
        search_button.grid(row=0, column=0, padx=(200, 0), pady=8) # Put it in the same column and adjust padx to be far enough.

        go_back_button = ttk.Button(
            self,
            text="🔙",
            command=lambda: controller.show_frame("StartPage"),
            width=3
        )
        go_back_button.grid(row=0, column=1, padx=8, pady=8, sticky="NE")

        # Create a new frame for the TableCanvas.
        tframe = ttk.Frame(self)
        tframe.grid(row=1, columnspan=4, padx=10, pady=10)
        self.table = TableCanvas(
            tframe,
            data={1:{"name": "", "amount": "", "barcode": "", "price_piece": ""}},
            width=1300,
            height=600,
            cellwidth=325,
            rowheight=40,
            rowheaderwidth=60, # To hide; set value to 0.
            thefont=('Arial', 14),
        )
        self.table.show()

    
    def focus_on_entry(self):
        pass

    def redraw_tables(self):
        # Create a new frame for the TableCanvas.
        tframe = ttk.Frame(self)
        tframe.grid(row=1, columnspan=4, padx=10, pady=10)
        self.table = TableCanvas(
            tframe,
            data={1:{"name": "", "amount": "", "barcode": "", "price_piece": ""}},
            width=1300,
            height=600,
            cellwidth=325,
            rowheight=40,
            rowheaderwidth=60, # To hide; set value to 0.
            thefont=('Arial', 14),
        )
        self.table.show()
        
    def get_tables(self):
        # The data from th API.
        url = f"http://127.0.0.1:8000/products/{self.controller.update_stock_barcode.get()}"
        request = requests.get(url, auth=("gabriel", "1"))

        # Transform the API's data to the TableCanvas' form.
        # Use the unique index for the rows in the TableCanvas.
        data = {}
        for i in request.json():
            data[request.json().index(i)] = i

        # Create a new frame for the TableCanvas.
        tframe = ttk.Frame(self)
        tframe.grid(row=1, columnspan=4, padx=10, pady=10)
        self.table = TableCanvas(
            tframe,
            data=data,
            width=1300,
            height=600,
            cellwidth=325,
            rowheight=40,
            rowheaderwidth=60, # To hide; set value to 0.
            thefont=('Arial', 14),
        )
        self.table.show()