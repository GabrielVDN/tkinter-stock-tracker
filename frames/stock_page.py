import tkinter as tk
from tkinter import ttk
from tkintertable import TableCanvas, TableModel


class StockPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)

        self.controller = controller
        # Center your Frame in the middele-top.
        self.columnconfigure(0, weight=1)

        button_1 = ttk.Button(
            self,
            text="Add new prod",
            command=lambda: controller.show_frame("AddNewProd"),
            width=13
        )
        button_1.grid(row=0, column=0, columnspan=2, sticky="E")

        button_2 = ttk.Button(
            self,
            text="Delete prod",
            command=lambda: controller.show_frame("DeleteProd"),
            width=13
        )
        button_2.grid(row=0, column=2, columnspan=2, sticky="W")

        go_back_button = ttk.Button(
            self,
            text="🔙",
            command=lambda: controller.show_frame("StartPage"),
            width=3
        )
        go_back_button.grid(row=0, column=3, sticky="E")

        name_label = ttk.Label(self, text="Name")
        name_label.grid(row=1, column=0)

        name_label = ttk.Label(self, text="Serial number")
        name_label.grid(row=1, column=1)

        name_label = ttk.Label(self, text="Ammount")
        name_label.grid(row=1, column=2)

        name_label = ttk.Label(self, text="Price/piece")
        name_label.grid(row=1, column=3)

        # Add padding in between every label.
        for child in self.winfo_children():
            child.grid_configure(padx=8, pady=8)       

        tframe = ttk.Frame(self)
        tframe.grid(row=2, columnspan=4)
        table = TableCanvas(tframe)
        table.show()


