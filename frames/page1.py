import tkinter as tk
from tkinter import ttk


class Page1(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)

        self.controller = controller
        # Center your Frame in the middele-top.
        self.columnconfigure(0, weight=1)

        label = ttk.Label(self, text="Stock")
        label.grid()

        button_1 = ttk.Button(
            self,
            text="Add new prod",
            command=lambda: controller.show_frame("Page3"),
            width=16
        )
        button_1.grid()

        button_2 = ttk.Button(
            self,
            text="Delete prod",
            command=lambda: controller.show_frame("Page4"),
            width=16
        )
        button_2.grid()

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
