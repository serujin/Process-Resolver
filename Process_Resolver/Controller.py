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

    def init_main_frame(self):
        self.main_frame = MainFrame(self.get_gui_container(), self)
        self.main_frame.add_button.configure(command=self.add_process)
        self.main_frame.del_button.configure(command=self.del_process)
        self.main_frame.ini_button.configure(command=self.ini_process)
        self.main_frame.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, frame_to_show):
        frame_to_show.tkraise()
        
    def add_process(self):
        self.show_frame(self.add_process_frame)

    def del_process(self):
        print("DEL")

    def ini_process(self):
        print("INI")

    def get_gui_container(self):
        return self.GUI.container

    def start_gui(self):
        self.GUI.mainloop()

Controller().start_gui()