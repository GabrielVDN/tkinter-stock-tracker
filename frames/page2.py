import tkinter as tk
from tkinter import ttk


class Page2(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)

        self.controller = controller
        # Center your Frame in the middele-top.
        self.columnconfigure(0, weight=1)

        label = ttk.Label(self, text="Scan product")
        label.grid()

        button = ttk.Button(
            self,
            text="Go to stock",
            command=lambda: controller.show_frame("Page1"),
            width=16
        )
        button.grid()

        go_back_button = ttk.Button(
            self,
            text="🔙",
            command=lambda: controller.show_frame("StartPage"),
            width=3
        )
        go_back_button.grid(row=0, column=1)
        
        # Add padding in between every label.
        for child in self.winfo_children():
            child.grid_configure(padx=8, pady=8)
