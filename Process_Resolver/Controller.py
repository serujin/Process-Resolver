import tkinter as tk
from MainFrame import MainFrame
from AddProcessFrame import AddProcessFrame
from GUI import GUI

class Controller():
    def __init__(self):
        self.frames = {}
        self.GUI = GUI()
        self.init_frames()

    def init_frames(self):
        self.init_main_frame()
        self.init_add_process_frame()
        self.show_frame(self.main_frame)

    def init_add_process_frame(self):
        self.add_process_frame = AddProcessFrame(self.get_gui_container(), self)
        self.add_process_frame.grid(row=0, column=0, sticky="nsew")
        self.add_process_frame.back.configure(command=self.go_to_main_frame)
        self.add_process_frame.add.configure(command=self.add_process_to_list)

    def init_main_frame(self):
        self.main_frame = MainFrame(self.get_gui_container(), self)
        self.main_frame.add_button.configure(command=self.add_process)
        self.main_frame.del_button.configure(command=self.del_process)
        self.main_frame.ini_button.configure(command=self.ini_process)
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        
    def add_process(self):
        self.show_frame(self.add_process_frame)

    def add_process_to_list(self):
        self.main_frame.process_list.insert(tk.END, " " + self.format_process())

    def format_process(self):
        process = ""
        process += self.add_process_frame.pid.get() + " | "
        process += self.add_process_frame.arrival_entry.get() + " | "
        process += self.add_process_frame.duration_entry.get() + " | "
        process += self.add_process_frame.priority.get() + " | "
        process += self.add_process_frame.io_exits_entry.get() + " | "
        process += self.add_process_frame.io_duration_entry.get()
        return process

    def del_process(self):
        self.main_frame.process_list.delete(self.main_frame.process_list.curselection())

    def ini_process(self):
        print("INI")

    def go_to_main_frame(self):
        self.show_frame(self.main_frame)

    def get_gui_container(self):
        return self.GUI.container

    def show_frame(self, frame_to_show):
        frame_to_show.tkraise()

    def start_gui(self):
        self.GUI.mainloop()

Controller().start_gui()