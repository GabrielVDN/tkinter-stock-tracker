import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from tkintertable import TableCanvas


class UpdateStock(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)

        self.controller = controller
        # Center your Frame in the middele-top.
        self.columnconfigure(0, weight=1)

        # Add some buttons.
        search_button = ttk.Button(
            self,
            text="🔍",
            command=lambda: self.search_entry.focus(),
            width=3
        )
        search_button.grid(row=0, column=0, columnspan=3)

        go_back_button = ttk.Button(
            self,
            text="🔙",
            command=lambda: controller.show_frame("StartPage"),
            width=3
        )
        go_back_button.grid(row=0, column=3)
               
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
            rowheaderwidth=60, # To hide; set value to 0
            thefont=('Arial', 14),
        )
        table.show()
        
        # Add padding in between every label.
        for child in self.winfo_children():
            child.grid_configure(padx=8, pady=8)

        # Put this dowm here so you can customize the 'padx'.
        self.search_entry = ttk.Entry(
            self,
            width=30,
            font=("TkDefaultFont 15")
        )
        self.search_entry.grid(row=0, column=0, padx=82, sticky="W")
