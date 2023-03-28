import tkinter as tk
from tkinter import ttk


def convert():
    val = entry_int.get()
    kms = 1.60934 * val
    output_string.set(kms)


window = tk.Tk()
window.title("Demo App")
window.geometry('300x150')

title_label = ttk.Label(
    master=window, text='Miles To Kilometers', font="Calibre 12")
title_label.pack(pady=10)

# input field
input_frame = ttk.Frame(master=window)
entry_int = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_int)
button = ttk.Button(master=input_frame, text="Convert", command=convert)
entry.pack(side="left")
button.pack()
input_frame.pack(pady=10)

# Output
output_string = tk.StringVar()
output_label = ttk.Label(
    master=window, font="Calibre 10", textvariable=output_string)

output_label.pack(pady=7)

window.mainloop()
