import tkinter as tk
import GUIConstants

class MainFrame(tk.Frame):
    def __init__(self, parent, number):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Process Resolver", font=GUIConstants.LARGE_FONT)
        self.add_button = tk.Button(self, text="Add Process")
        self.del_button = tk.Button(self, text="Delete Process")
        self.ini_button = tk.Button(self, text="Initialize CPU")
        self.process_list = tk.Listbox(self, width=38)
        label.grid(row=0, column=0, columnspan=3)
        self.process_list.grid(row=1, column=0, columnspan=3)
        self.add_button.grid(row=2, column=0)
        self.del_button.grid(row=2, column=1)
        self.ini_button.grid(row=2, column=2)
