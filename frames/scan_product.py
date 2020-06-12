import tkinter as tk
from tkinter import ttk
from tkintertable import TableCanvas
from tkinter import messagebox
import requests


class ScanProd(ttk.Frame):
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
            textvariable=controller.scan_prod_barcode,
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
            text="SEARCH",
            command=lambda: [self.search_entry.focus(), bind_entry_field(None)],
            width=9,
            style="SearchButton.TButton"
        )
        search_button.grid(row=0, column=0, padx=(446, 0), pady=8) # Put it in the same column and adjust padx to be far enough.

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
            text="BACK",
            command=lambda: controller.show_frame("StartPage"),
            width=5,
            style="BackButton.TButton"
        )
        go_back_button.grid(row=0, column=3, padx=8, pady=8, sticky="NE")

        # Create a new frame for the TableCanvas.
        tframe = ttk.Frame(self)
        tframe.grid(row=1, columnspan=4, padx=10, pady=10)
        self.table = TableCanvas(
            tframe,
            data={1:{"name": "", "amount": "", "barcode": "", "price_piece": ""}},
            width=1300,
            height=600,
            cellwidth=325,
            rowheight=40,
            rowheaderwidth=60, # To hide; set value to 0.
            read_only=True,
            rowselectedcolor=None,  # Get rid of the row selection.
            selectedcolor=None, # Get rid of the cell selection.
            thefont=('Arial', 14),
        )
        self.table.show()


    def focus_on_entry(self):
        pass

    def redraw_tables(self):
        # Create a new frame for the TableCanvas.
        tframe = ttk.Frame(self)
        tframe.grid(row=1, columnspan=4, padx=10, pady=10)
        self.table = TableCanvas(
            tframe,
            data={1:{"name": "", "amount": "", "barcode": "", "price_piece": ""}},
            width=1300,
            height=600,
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
            url = f"http://127.0.0.1:8000/products/{self.controller.scan_prod_barcode.get()}/"
            request = requests.get(url, auth=("gabriel", "1")).json()

            # Updat data
            if request['amount'] > 0:
                request['amount'] -= 1
                requests.put(url, data=request, auth=("gabriel", "1"))
            else:
                messagebox.showerror("No more stock", f"You ran out of {request['name']}.")

            # Transform the API's data to the TableCanvas' form.
            # Use the unique index for the rows in the TableCanvas.
            data = {1: request}
            
                # Create a new frame for the TableCanvas.
            tframe = ttk.Frame(self)
            tframe.grid(row=1, columnspan=4, padx=10, pady=10)
            self.table = TableCanvas(
                tframe,
                data=data,
                width=1300,
                height=600,
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