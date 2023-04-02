import tkinter as tk
from tkinter import ttk


def a_button():
    print("clicked", entry_value.get())
    label_text.set(entry_value.get())


# creating window
window = tk.Tk()
window.title("New Way")
window.geometry('800x600')

# creating widgets using tk
text = tk.Text(master=window)

# ttk widgets
# creating this var to render the dynamic text from the entry widgets to this label
label_text = tk.StringVar()
label = ttk.Label(master=window, text='This is a test',
                  textvariable=label_text)
label.pack()
text.pack()

entry_value = tk.StringVar()

entry = ttk.Entry(master=window, textvariable=entry_value)
entry.pack()

btn = ttk.Button(master=window, text="A button", command=a_button)
btn.pack()
window.mainloop()
