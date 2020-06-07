import tkinter as tk
from tkinter import ttk


class StartPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        
        self.controller = controller
        # Center your Frame in the middle-top.
        self.columnconfigure(0, weight=1)

        # Add some buttons.
        button1 = ttk.Button(
            self,
            text="View Stock",
            command=lambda: controller.show_frame("StockPage"),
            width=16
        )
        button1.grid()

        button2 = ttk.Button(
            self,
            text="Scan a product",
            command=lambda: controller.show_frame("ScanProd"),
            width=16
        )
        button2.grid()

        button3 = ttk.Button(
            self,
            text="Update stock",
            command=lambda: controller.show_frame("UpdateStock"),
            width=16
        )
        button3.grid()


        # Add padding in between every label.
        for child in self.winfo_children():
            child.grid_configure(padx=12, pady=12)
    
    def focus_on_entry(self):
        pass