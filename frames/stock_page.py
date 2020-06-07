import tkinter as tk
from tkinter import ttk
from tkintertable import TableCanvas


class StockPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)

        self.controller = controller
        # Center your Frame in the middele-top.
        self.columnconfigure(1, weight=1)

        # Add some buttons.
        button_1 = ttk.Button(
            self,
            text="Add new prod",
            command=lambda: controller.show_frame("AddNewProd"),
            width=13
        )
        button_1.grid(row=0, column=0)

        button_2 = ttk.Button(
            self,
            text="Delete prod",
            command=lambda: controller.show_frame("DeleteProd"),
            width=13
        )
        button_2.grid(row=0, column=1, sticky="W")

        go_back_button = ttk.Button(
            self,
            text="🔙",
            command=lambda: controller.show_frame("StartPage"),
            width=3
        )
        go_back_button.grid(row=0, column=3, sticky="E")

        # The data from th API.
        request =[
            {
                "name": "Choco",
                "ammount": 5,
                "price_p_p": 2.5,
                "barcode": "12345"
            },
            {
                "name": "Cheakpeas",
                "ammount": 10,
                "price_p_p": 0.7,
                "barcode": "789456"
            },
            {
                "name": "Bread",
                "ammount": 3,
                "price_p_p": 2.57,
                "barcode": "585844"
            }
        ]

        # Transform the API's data to the TableCanvas' form.
        # Use the unique index for the rows in the TableCanvas.
        data = {}
        for i in request:
            data[request.index(i)] = i

        # Create a new frame for the TableCanvas.
        tframe = ttk.Frame(self)
        tframe.grid(row=2, columnspan=4)
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
            child.grid_configure(padx=12, pady=12)
