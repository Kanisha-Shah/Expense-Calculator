from tkinter import *
from tkinter import ttk
from tkinter import Tk


window = Tk()
notebook = ttk.Notebook(window)
notebook.pack()
subframe = ttk.Frame(window)
subframe.pack()
notebook.add(subframe, text="tab", state="normal")
def buttonaction():
    notebook.tab(0, state="disabled")
button = ttk.Button(subframe, command=buttonaction, text="click to disable tab")
button.pack()

if __name__ == "__main__":
    window.mainloop()