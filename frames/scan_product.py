import tkinter as tk
from tkinter import ttk
from tkintertable import TableCanvas


class ScanProd(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)

        self.controller = controller
        # Center your Frame, all the entry's and labels in the middle. 
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        self.search_entry = ttk.Entry(
            self,
            width=24,
            font=("TkDefaultFont 15")
        )
        self.search_entry.grid(row=0, column=0, padx=(72, 12), sticky="W")

        # Add some buttons.
        search_button = ttk.Button(
            self,
            text="🔍",
            command=lambda: self.search_entry.focus(),
            width=3
        )
        search_button.grid(row=0, column=0, padx=(446, 0), pady=8) # Put it in the same column and adjust padx to be far enough.

        button = ttk.Button(
            self,
            text="Go to stock",
            command=lambda: controller.show_frame("StockPage"),
            width=18
        )
        button.grid(row=0, column=2, sticky="W")

        go_back_button = ttk.Button(
            self,
            text="🔙",
            command=lambda: controller.show_frame("StartPage"),
            width=3
        )
        go_back_button.grid(row=0, column=3, padx=8, pady=8, sticky="NE")
               
        # The data from th API.
        request =[
            {
                "name": "",
                "amount": "",
                "barcode": "",
                "price_piece": ""
            },
        ]

        # Transform the API's data to the TableCanvas' form.
        # Use the unique index for the rows in the TableCanvas.
        data = {}
        for i in request:
            data[request.index(i)] = i

        # Create a new frame for the TableCanvas.
        tframe = ttk.Frame(self)
        tframe.grid(row=1, columnspan=4)
        table = TableCanvas(
            tframe,
            data=data,
            width=1300,
            height=600,
            cellwidth=330,
            rowheight=40,
            rowheaderwidth=60, # To hide; set value to 0.
            thefont=('Arial', 14),
        )
        table.show()


    def focus_on_entry(self):
        self.search_entry.focus()