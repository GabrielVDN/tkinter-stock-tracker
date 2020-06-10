import tkinter
import time


root = tkinter.Tk()

input_value = tkinter.StringVar()

search_entry = tkinter.Entry(
    root,
    textvariable=input_value,
    width=24,
    bd=4,
    font=("TkDefaultFont", 14)
)
search_entry.pack(padx=20, pady=20)
search_entry.focus()

def bind_entry_field(event):
    print(input_value.get())
    time.sleep(1) # Sleep for 3 seconds
    search_entry.delete(0, 'end')
    search_entry.focus()

# Bind 'Enter' to the Enty field.
search_entry.bind('<Return>', bind_entry_field)

root.mainloop()