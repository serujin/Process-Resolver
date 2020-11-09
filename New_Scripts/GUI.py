from tkinter import Tk, Frame

class GUI():
    def __init__(self, title):
        self.root = Tk()
        self.root.title(title)
        self.start_constants()
        self.format_window()

    def start_constants(self):
        self.screen_w = int(self.root.winfo_screenwidth() / 4)
        self.screen_h = int(self.root.winfo_screenheight() / 4)

    def format_window(self):
        window_size = str(self.screen_w) + "x" + str(self.screen_h)
        self.root.resizable(False, False)
        self.root.geometry(window_size)

    def start(self):
        self.root.mainloop()

GUI("Process-Resolver").start()