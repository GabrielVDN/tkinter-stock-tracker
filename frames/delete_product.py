import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import requests

class DeleteProd(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)

        self.controller = controller
        # Center your Frame in the middele-top.
        self.columnconfigure(0, weight=1)

        label = ttk.Label(self, text="Scan barcode")
        label.grid(row=0, columnspan=2, pady=8)

        # Add some buttons.
        go_back_button = ttk.Button(
            self,
            text="🔙",
            command=lambda: controller.show_frame("StartPage"),
            width=3
        )
        go_back_button.grid(row=0, column=1, padx=8, pady=8, sticky="NE")

        delete_button = ttk.Button(
            self,
            text="Delete Product",
            command=lambda: self.delete_product(),
            width=20
        )
        delete_button.grid(row=2, columnspan=2)

        self.entry_barcode = ttk.Entry(
            self, font=("TkDefaultFont", 20), textvariable=controller.delete_prod_barcode
        )
        self.entry_barcode.grid(row=1, columnspan=2, pady=40)


    def delete_product(self):
        '''Delete the product with the given barcode'''
        if messagebox.askokcancel("Delete", "Are you sure you want delete this?!") == True:
            url = f"http://127.0.0.1:8000/products/{self.controller.delete_prod_barcode.get()}/"
            request = requests.delete(url, auth=("gabriel", "1"))
            print(request)
            if request.status_code != 204:
                messagebox.showerror("None Existant Prod", "This product doesn't exist in the stock.")
        self.entry_barcode.focus()
        self.entry_barcode.delete(0, 'end')

    def focus_on_entry(self):
        self.entry_barcode.focus()

    def redraw_tables(self):
        pass