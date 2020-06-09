import tkinter as tk
from tkinter import ttk
from tkintertable import TableCanvas
from tkinter import messagebox
import requests


class AddNewProd(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)

        self.controller = controller
        # Center your Frame in the middele-top.
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        # Create a forum to add new products, asking for all the information.
        # All entry fields.
        self.entry_barcode = ttk.Entry(
            self, width=40, textvariable=controller.add_new_prod_barcode,
            font=("TkDefaultFont", 20)
        )
        self.entry_barcode.grid(row=1, column=1, sticky="W")

        self.entry_name = ttk.Entry(
            self, width=40, textvariable=controller.add_new_prod_name,
            font=("TkDefaultFont", 20)
        )
        self.entry_name.grid(row=2, column=1, sticky="W")

        self.entry_amount = ttk.Entry(
            self, width=40, textvariable=controller.add_new_prod_amount,
            font=("TkDefaultFont", 20)
        )
        self.entry_amount.grid(row=3, column=1, sticky="W")

        self.entry_price_piece = ttk.Entry(
            self, width=40, textvariable=controller.add_new_prod_price_piece,
            font=("TkDefaultFont", 20)
        )
        self.entry_price_piece.grid(row=4, column=1, sticky="W")

        # Add some buttons.
        submit_button = ttk.Button(
            self,
            text="Submit Product",
            command=lambda: self.submit_new_prod(),
            width=50
        )
        submit_button.grid(row=5, columnspan=3)

        # Add padding in between every label.
        for child in self.winfo_children():
            child.grid_configure(padx=16, pady=16)

        
        # Put this dowm here so you can customize the 'padx' and 'pady.
        label_1 = ttk.Label(
            self,
            text="Please enter all the information,\n" + 
                "   and don't edit the barcode!"
        )
        label_1.grid(row=0, columnspan=2, pady=60)

        go_back_button = ttk.Button(
            self,
            text="🔙",
            command=lambda: controller.show_frame("StartPage"),
            width=3
        )
        go_back_button.grid(row=0, column=1, padx=8, pady=8, sticky="NE")

        # All labels.
        label_barcode = ttk.Label(self, text="Barcode*:")
        label_barcode.grid(row=1, column=0, padx=(0,58), sticky="E")

        label_name = ttk.Label(self, text="Name*:")
        label_name.grid(row=2, column=0, padx=(0,98), sticky="E")

        label_amount = ttk.Label(self, text="Amount*:")
        label_amount.grid(row=3, column=0, padx=(0,60), sticky="E")

        label_price_piece = ttk.Label(self, text="Price/Piece:")
        label_price_piece.grid(row=4, column=0, padx=(0,30), sticky="E")

        
    def submit_new_prod(self):
        if self.controller.add_new_prod_barcode.get() and self.controller.add_new_prod_name.get() and self.controller.add_new_prod_amount.get():
            try:
                int(self.controller.add_new_prod_amount.get())
            except:
                messagebox.showerror("Invalid Input", "You need to input an integer for the Amount.")
                self.entry_amount.focus()
                print("..........................................")
            else:
                if self.controller.add_new_prod_price_piece.get():
                    try:
                        self.controller.add_new_prod_price_piece.set(float(self.controller.add_new_prod_price_piece.get()))
                        self.post_to_api()
                    except ValueError:
                        messagebox.showerror("Invalid Input", "You need to input an integer for the Price/Piece.")
                        self.entry_price_piece.focus()
                else: 
                    self.post_to_api()
        else:
            messagebox.showinfo("Missing fields", "You need to input all the required fields.")
            self.entry_barcode.focus()

    def post_to_api(self):
        '''Post to the api if the messagebox is True'''
        if messagebox.askokcancel("Add new product", "Are you sure you want add this?!"):
            self.data_for_post = {}
            self.data_for_post['barcode'] = self.controller.add_new_prod_barcode.get()
            self.data_for_post['name'] = self.controller.add_new_prod_name.get()
            self.data_for_post['amount'] = int(self.controller.add_new_prod_amount.get())
            self.data_for_post['price_piece'] = self.controller.add_new_prod_price_piece.get()
            requests.post("http://127.0.0.1:8000/products/", data=self.data_for_post, auth=("gabriel", "1"))

            self.empty_entry_fields()

    def empty_entry_fields(self):      
        self.entry_barcode.delete(0, "end")
        self.entry_name.delete(0, "end")
        self.entry_amount.delete(0, "end")
        self.entry_price_piece.delete(0, "end")
        self.entry_barcode.focus()


    def focus_on_entry(self):
        self.entry_barcode.focus()

    def redraw_tables(self):
        pass