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
        button1.pack(fill="both", expand=True, padx=6, pady=6)

        button2 = ttk.Button(
            self,
            text="Scan a product",
            command=lambda: controller.show_frame("ScanProd"),
            width=16
        )
        button2.pack(fill="both", expand=True, padx=6, pady=6)

        button3 = ttk.Button(
            self,
            text="Update stock",
            command=lambda: controller.show_frame("UpdateStock"),
            width=16
        )
        button3.pack(fill="both", expand=True, padx=6, pady=6)
    
    
    def focus_on_entry(self):
        pass

    def redraw_tables(self):
        pass