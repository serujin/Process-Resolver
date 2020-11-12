import tkinter as tk
import GUIConstants

class AddProcessFrame(tk.Frame):
    def __init__(self, parent, number):
        tk.Frame.__init__(self, parent)
        self.init_labels()
        self.init_entries() 
        self.init_pid_selector()
        self.init_priority_selector()
        self.init_back_button()
        self.init_add_button()

    def init_labels(self):
        top_label = tk.Label(self, text="Add Process", font=GUIConstants.LARGE_FONT)
        label_1 = tk.Label(self, text="Process Identifier", font=GUIConstants.MEDIUM_FONT)
        label_2 = tk.Label(self, text="Process Arrival", font=GUIConstants.MEDIUM_FONT)
        label_3 = tk.Label(self, text="Process Duration", font=GUIConstants.MEDIUM_FONT)
        label_4 = tk.Label(self, text="Process Priority", font=GUIConstants.MEDIUM_FONT)
        label_5 = tk.Label(self, text="Process IO Exits", font=GUIConstants.MEDIUM_FONT)
        label_6 = tk.Label(self, text="Process IO Durations", font=GUIConstants.MEDIUM_FONT)
        top_label.grid(row=0, column=0, columnspan=2)
        label_1.grid(row=1, column=0)
        label_2.grid(row=2, column=0)
        label_3.grid(row=3, column=0)
        label_4.grid(row=4, column=0)
        label_5.grid(row=5, column=0)
        label_6.grid(row=6, column=0)

    def init_pid_selector(self):
        self.pid = tk.StringVar(self)
        self.pid.set(GUIConstants.PID_OPTIONS[0])
        pid_selector = tk.OptionMenu(self, self.pid, *GUIConstants.PID_OPTIONS)
        pid_selector.grid(row=1, column=1)

    def init_priority_selector(self):
        self.priority = tk.StringVar(self)
        self.priority.set(GUIConstants.PRIORITY_OPTIONS[0])
        priority_selector = tk.OptionMenu(self, self.priority, *GUIConstants.PRIORITY_OPTIONS)
        priority_selector.grid(row=4, column=1)

    def init_back_button(self):
        self.back = tk.Button(self)
        self.back.configure(text="Back")
        self.back.grid(row=7, column=0, padx=10, pady=20)

    def init_add_button(self):
        self.add = tk.Button(self)
        self.add.configure(text="Add")
        self.add.grid(row=7, column=1, padx=10, pady=0)

    def init_entries(self):
        self.arrival_entry = tk.Entry(self)
        self.duration_entry = tk.Entry(self)
        self.io_exits_entry = tk.Entry(self)
        self.io_duration_entry = tk.Entry(self)
        self.arrival_entry.grid(row=2, column=1)
        self.duration_entry.grid(row=3, column=1)
        self.io_exits_entry.grid(row=5, column=1)
        self.io_duration_entry.grid(row=6, column=1)
'''
from tkinter import *

OPTIONS = [
"Jan",
"Feb",
"Mar"
] #etc

master = Tk()

variable = StringVar(master)
variable.set(OPTIONS[0]) # default value

w = OptionMenu(master, variable, *OPTIONS)
w.pack()

mainloop()
'''