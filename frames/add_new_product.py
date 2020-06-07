import tkinter as tk
from tkinter import ttk
from tkintertable import TableCanvas


class AddNewProd(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)

        self.controller = controller
        # Center your Frame in the middele-top.
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        # Add some buttons.
        go_back_button = ttk.Button(
            self,
            text="🔙",
            command=lambda: controller.show_frame("StartPage"),
            width=3
        )
        go_back_button.grid(row=0, column=1, sticky="NE")

        submit_button = ttk.Button(
            self,
            text="Submit product",
            command=lambda: self.submit_new_prod(),
            width=36
        )
        submit_button.grid(row=5, columnspan=3)
        
        # Create a forum to add new products, asking for all the information.
        # All labels.
        label_barcode = ttk.Label(self, text="Barcode:")
        label_barcode.grid(row=1, column=0, sticky="E")

        label_name = ttk.Label(self, text="Name:")
        label_name.grid(row=2, column=0, sticky="E")

        label_amount = ttk.Label(self, text="Amount:")
        label_amount.grid(row=3, column=0, sticky="E")

        label_price_piece = ttk.Label(self, text="Price/Piece:")
        label_price_piece.grid(row=4, column=0, sticky="E")

        # All entry fields.
        self.entry_barcode = ttk.Entry(self, width=40)
        self.entry_barcode.grid(row=1, column=1, sticky="W")

        self.entry_name = ttk.Entry(self, width=40)
        self.entry_name.grid(row=2, column=1, sticky="W")

        self.entry_amount = ttk.Entry(self, width=40)
        self.entry_amount.grid(row=3, column=1, sticky="W")

        self.entry_price_piece = ttk.Entry(self, width=40)
        self.entry_price_piece.grid(row=4, column=1, sticky="W")

        # Add padding in between every label.
        for child in self.winfo_children():
            child.grid_configure(padx=16, pady=16)
        
        # Put this dowm here so you can customize the 'padx'.
        label_1 = ttk.Label(
            self,
            text="Please enter all the information,\n" + 
                "   and don't edit the barcode!"
        )
        label_1.grid(row=0, columnspan=2, pady=60)

    def submit_new_prod(self):
        self.entry_barcode.delete(0, "end")
        self.entry_name.delete(0, "end")
        self.entry_amount.delete(0, "end")
        self.entry_price_piece.delete(0, "end")
        self.entry_barcode.focus()
