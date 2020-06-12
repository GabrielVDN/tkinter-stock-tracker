import tkinter as tk
from tkinter import ttk
from tkintertable import TableCanvas
import requests
from tkinter import messagebox


class UpdateStock(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)

        self.controller = controller
        # Center your Frame, all the entry's and labels in the middle. 
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        # Set the widget's background.
        self["style"] = "Background.TFrame"

        self.search_entry = ttk.Entry(
            self,
            textvariable=controller.update_stock_barcode,
            width=24,
            font=("TkDefaultFont 15")
        )
        self.search_entry.grid(row=0, column=0, padx=(72, 12), sticky="W")

        def bind_entry_field(event):
            self.get_tables()
            self.set_entrys()
            self.search_entry.delete(0, 'end')

        # Bind 'Enter' to the Enty field.
        self.search_entry.bind('<Return>', bind_entry_field)

        # Add some buttons.
        search_button = ttk.Button(
            self,
            text="🔍",
            command=lambda: [self.search_entry.focus(), bind_entry_field(None)],
            width=3,
            style="Background.TButton"
        )
        search_button.grid(row=0, column=0, padx=(446, 0), pady=10) # Put it in the same column and adjust padx to be far enough.

        button = ttk.Button(
            self,
            text="Go To Stock",
            command=lambda: [
                controller.show_frame("StockPage"),
                self.empty_entry_fields(),
                self.block_entry_fields()
            ],
            width=18,
            style="Background.TButton"
        )
        button.grid(row=0, column=2, sticky="W")

        go_back_button = ttk.Button(
            self,
            text="🔙",
            command=lambda: [
                controller.show_frame("StartPage"),
                self.empty_entry_fields(),
                self.block_entry_fields()
            ],
            width=3,
            style="Background.TButton"
        )
        go_back_button.grid(row=0, column=3, padx=8, pady=8, sticky="NE")

        # Create a new frame for the TableCanvas.
        tframe = ttk.Frame(self)
        tframe.grid(row=1, columnspan=4, padx=10, pady=10)
        self.table = TableCanvas(
            tframe,
            data={1:{"name": "", "amount": "", "barcode": "", "price_piece": ""}},
            width=1300,
            height=50,
            cellwidth=325,
            rowheight=40,
            rowheaderwidth=60, # To hide; set value to 0.
            thefont=('Arial', 14),
        )
        self.table.show()

        # Create a new frame for the Labels and Entry's.
        tframe = ttk.Frame(self)
        tframe["style"] = "Background.TFrame"
        tframe.grid(row=2, columnspan=4, pady=80)
        # All labels.
        label_name = ttk.Label(
            tframe, style="Background.TLabel", text="Name*:"
        )
        label_name.grid(row=0, column=0, padx=6, pady=10)

        label_amount = ttk.Label(
            tframe, style="Background.TLabel", text="Amount*:"
        )
        label_amount.grid(row=0, column=1, padx=6, pady=10)

        label_barcode = ttk.Label(
            tframe, style="Background.TLabel", text="Barcode:", font=("System", 20)
        )
        label_barcode.grid(row=0, column=2, padx=6, pady=10)

        label_price_piece = ttk.Label(
            tframe, style="Background.TLabel", text="Price/Piece:"
        )
        label_price_piece.grid(row=0, column=3, padx=6, pady=10)

        # All entry fields.
        self.entry_name = ttk.Entry(
            tframe, width=15, textvariable=controller.update_prod_name,
            font=("TkDefaultFont", 20), state='readonly'
        )
        self.entry_name.grid(row=1, column=0, sticky="W", padx=6, pady=10)

        self.entry_amount = ttk.Entry(
            tframe, width=15, textvariable=controller.update_prod_amount,
            font=("TkDefaultFont", 20), state='readonly'
        )
        self.entry_amount.grid(row=1, column=1, sticky="W", padx=6, pady=10)

        self.entry_barcode = ttk.Entry(
            tframe, width=15, textvariable=controller.update_prod_barcode,
            font=("System", 18), state='readonly'
        )
        self.entry_barcode.grid(row=1, column=2, sticky="W", padx=6, pady=10)

        self.entry_price_piece = ttk.Entry(
            tframe, width=15, textvariable=controller.update_prod_price_piece,
            font=("TkDefaultFont", 20), state='readonly'
        )
        self.entry_price_piece.grid(row=1, column=3, sticky="W", padx=6, pady=10)

        submit_button = ttk.Button(
            tframe,
            text="Submit Product",
            command=lambda: self.submit_new_prod(),
            width=60,
            style="Background.TButton"
        )
        submit_button.grid(row=2, columnspan=4)

        label_1 = ttk.Label(
            tframe, style="Background.TLabel",
            text="If you want to edit the barcode; you should delete  the product first," +
            "\nand add a  new  product after that.",
            font=("System", 12)
        )
        label_1.grid(row=3, columnspan=4, pady=(60, 0))

        delete_button = ttk.Button(
            tframe,
            text="delete",
            command=lambda: controller.show_frame("DeleteProd"),
            width=5.5,
            style="LabelBackground.TButton"
        )
        delete_button.grid(row=3, column=2, sticky="W", padx=(92,0), pady=(30,0))

        # Create a new frame for the button.
        tframe = ttk.Frame(self)
        tframe["style"] = "Background.TFrame"
        tframe.grid(row=2, column=0, padx=(226,0), pady=(316,0))

        new_button = ttk.Button(
            tframe,
            text="new",
            command=lambda: controller.show_frame("AddNewProd"),
            width=4,
            style="LabelBackground.TButton"
        )
        new_button.grid(row=3, column=0)


    def set_entrys(self):
        try:
            # The data from th API.
            url = f"http://127.0.0.1:8000/products/{self.controller.update_stock_barcode.get()}/"
            request = requests.get(url, auth=("gabriel", "1")).json()
            
            self.controller.update_prod_name.set(request['name'])
            self.controller.update_prod_amount.set(request['amount'])
            self.controller.update_prod_barcode.set(request['barcode'])
            if request['price_piece'] == None:
                    request['price_piece'] = ""
            self.controller.update_prod_price_piece.set(request['price_piece'])
            self.entry_name.configure(state='normal')
            self.entry_amount.configure(state='normal')
            self.entry_price_piece.configure(state='normal')
        except:
            pass

    def block_entry_fields(self):
        self.entry_name.configure(state='readonly')
        self.entry_amount.configure(state='readonly')
        self.entry_price_piece.configure(state='readonly')

        
    def submit_new_prod(self):
        if self.controller.update_prod_name.get() and self.controller.update_prod_amount.get() and self.controller.update_prod_barcode.get():
            try:
                int(self.controller.update_prod_amount.get())
            except:
                messagebox.showerror("Invalid Input", "You need to input an integer for the Amount.")
                self.entry_amount.focus()
            else:
                if self.controller.update_prod_price_piece.get():
                    try:
                        self.controller.update_prod_price_piece.set(float(self.controller.update_prod_price_piece.get()))
                        self.put_to_api()
                    except ValueError:
                        messagebox.showerror("Invalid Input", "You need to input an integer for the Price/Piece.")
                        self.entry_price_piece.focus()
                else: 
                    self.put_to_api()
        else:
            messagebox.showinfo("Missing fields", "You need to input all the required fields.")

    def put_to_api(self):
        '''Post to the api if the messagebox is True'''
        try:  
            if messagebox.askokcancel("Submit product", "Are you sure you want submit these new values?!"):
                self.data_for_put = {}
                self.data_for_put['barcode'] = self.controller.update_prod_barcode.get()
                self.data_for_put['name'] = self.controller.update_prod_name.get()
                self.data_for_put['amount'] = int(self.controller.update_prod_amount.get())
                self.data_for_put['price_piece'] = self.controller.update_prod_price_piece.get()

                url = f"http://127.0.0.1:8000/products/{self.controller.update_prod_barcode.get()}/"
                r = requests.put(url, data=self.data_for_put, auth=("gabriel", "1"))
                print(self.data_for_put)
                print(url)
                print(r.status_code)
                self.empty_entry_fields()
                self.block_entry_fields()
                self.redraw_tables()
                
        except:
            messagebox.showerror("API Error", "The api isn't running.")


    def empty_entry_fields(self):
        self.entry_name.delete(0, 'end')
        self.entry_amount.delete(0, 'end')
        self.controller.update_prod_barcode.set('')
        self.entry_price_piece.delete(0, 'end')

        self.entry_name.focus()

    
    def focus_on_entry(self):
        pass

    def redraw_tables(self):
        # Create a new frame for the TableCanvas.
        tframe = ttk.Frame(self)
        tframe.grid(row=1, columnspan=4, pady=10)
        self.table = TableCanvas(
            tframe,
            data={1:{"name": "", "amount": "", "barcode": "", "price_piece": ""}},
            width=1300,
            height=50,
            cellwidth=325,
            rowheight=40,
            rowheaderwidth=60, # To hide; set value to 0.
            read_only=True,
            rowselectedcolor=None,  # Get rid of the row selection.
            selectedcolor=None, # Get rid of the cell selection.
            thefont=('Arial', 14),
        )
        self.table.show()
        
    def get_tables(self):
        try:
            # The data from th API.
            url = f"http://127.0.0.1:8000/products/{self.controller.update_stock_barcode.get()}/"
            request = requests.get(url, auth=("gabriel", "1")).json()

            # Transform the API's data to the TableCanvas' form.
            # Use the unique index for the rows in the TableCanvas.
            if request['price_piece'] == None:
                request['price_piece'] = ""
            
            data = {1: request}

            # Create a new frame for the TableCanvas.
            tframe = ttk.Frame(self)
            tframe.grid(row=1, columnspan=4, pady=10)
            self.table = TableCanvas(
                tframe,
                data=data,
                width=1300,
                height=50,
                cellwidth=325,
                rowheight=40,
                rowheaderwidth=60, # To hide; set value to 0.
                read_only=True,
                rowselectedcolor=None,  # Get rid of the row selection.
                selectedcolor=None, # Get rid of the cell selection.
                thefont=('Arial', 14),
            )
            self.table.show()

        except:
            if messagebox.askyesno(
                "Not In Stock", "This product does not yet exist in stock." +
                "\nYou need to add it first, do you want to add it?"
            ):
                self.controller.show_frame("AddNewProd")