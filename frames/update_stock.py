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
            command=lambda: controller.show_frame("StockPage"),
            width=18,
            style="Background.TButton"
        )
        button.grid(row=0, column=2, sticky="W")

        go_back_button = ttk.Button(
            self,
            text="🔙",
            command=lambda: controller.show_frame("StartPage"),
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
        label_barcode = ttk.Label(
            tframe, style="Background.TLabel", text="Barcode*:"
        )
        label_barcode.grid(row=0, column=0, padx=6, pady=10)

        label_name = ttk.Label(
            tframe, style="Background.TLabel", text="Name*:"
        )
        label_name.grid(row=0, column=1, padx=6, pady=10)

        label_amount = ttk.Label(
            tframe, style="Background.TLabel", text="Amount*:"
        )
        label_amount.grid(row=0, column=2, padx=6, pady=10)

        label_price_piece = ttk.Label(
            tframe, style="Background.TLabel", text="Price/Piece:"
        )
        label_price_piece.grid(row=0, column=3, padx=6, pady=10)

        # All entry fields.
        self.entry_barcode = ttk.Entry(
            tframe, width=15, textvariable=controller.add_new_prod_barcode,
            font=("TkDefaultFont", 20)
        )
        self.entry_barcode.grid(row=1, column=0, sticky="W", padx=6, pady=10)

        self.entry_name = ttk.Entry(
            tframe, width=15, textvariable=controller.add_new_prod_name,
            font=("TkDefaultFont", 20)
        )
        self.entry_name.grid(row=1, column=1, sticky="W", padx=6, pady=10)

        self.entry_amount = ttk.Entry(
            tframe, width=15, textvariable=controller.add_new_prod_amount,
            font=("TkDefaultFont", 20)
        )
        self.entry_amount.grid(row=1, column=2, sticky="W", padx=6, pady=10)

        self.entry_price_piece = ttk.Entry(
            tframe, width=15, textvariable=controller.add_new_prod_price_piece,
            font=("TkDefaultFont", 20)
        )
        self.entry_price_piece.grid(row=1, column=3, sticky="W", padx=6, pady=10)

        # Add some buttons.
        submit_button = ttk.Button(
            tframe,
            text="Submit Product",
            # command=lambda: self.submit_new_prod(),
            width=62,
            style="Background.TButton"
        )
        submit_button.grid(row=4, columnspan=4)


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
            if request == {'detail': 'Not found.'}:
                data={1:{"name": "", "amount": "", "barcode": "", "price_piece": ""}}
                if messagebox.askyesno(
                    "Not In Stock", "This product does not yet exist in stock." +
                    "\nYou need to add it first, do you want to add it?"
                ):
                    self.controller.show_frame("AddNewProd")
            else:
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