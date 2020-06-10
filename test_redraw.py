import tkinter as tk
from tkintertable import TableCanvas
import requests



data = {
    1: {'a': 'a1', 'b': 'b1', 'c': 'c1'},
    2: {'a': 'a2', 'b': 'b2', 'c': 'c2'},
    3: {'a': 'a3', 'b': 'b3', 'c': 'c3'},
    4: {'a': 'a4', 'b': 'b4', 'c': 'c4'},
    5: {'a': 'a5', 'b': 'b5', 'c': 'c5'},
}

row = 5
nmbr_a = 5
nmbr_b = 5
nmbr_c = 5

def redraw_table(row, nmbr_a, nmbr_b, nmbr_c):
    row += 1
    nmbr_a += 1
    nmbr_b += 1
    nmbr_c += 1

    add_data = {}

    add_data[row] = {'a': f'a{nmbr_a}', 'b': f'b{nmbr_b}', 'c': f'c{nmbr_c}'}
    print(add_data)


root = tk.Tk()
root.geometry("600x520")

btn = tk.Button(
    root,
    text="Test Redraw",
    borderwidth=5,
    command=lambda: redraw_table(row, nmbr_a, nmbr_b, nmbr_c),
    font=('Arial', 16)
)
btn.pack(padx=8, pady=8)


tframe = tk.Frame(root)
tframe.pack()

table = TableCanvas(
    tframe,
    data=data,
    width=450,
    height=400,
    cellwidth=150,
    rowheight=40,
    rowheaderwidth=60, # To hide; set value to 0
    thefont=('Arial', 14),
)
table.show()


root.mainloop()