import tkinter as tk
from tkinter import ttk


class StartPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        
        self.controller = controller
        # Center your Frame in the middele-top.
        self.columnconfigure(0, weight=1)

        button1 = ttk.Button(
            self,
            text="Vieuw Stock",
            command=lambda: controller.show_frame("Page1"),
            width=16
        )
        button1.grid()

        button2 = ttk.Button(
            self,
            text="Scan a product",
            command=lambda: controller.show_frame("Page2"),
            width=16
        )
        button2.grid()

        button3 = ttk.Button(
            self,
            text="Update stock",
            command=lambda: controller.show_frame("Page5"),
            width=16
        )
        button3.grid()


        # Add padding in between every label.
        for child in self.winfo_children():
            child.grid_configure(padx=15, pady=15)