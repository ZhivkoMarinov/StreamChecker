from abc import ABC, abstractmethod
from tkinter import *
from tkinter import ttk


class MainFrame(ABC):
    def __init__(self, name: str, geometry: str):
        self.root = Tk()
        self.root.title(name)
        self.frame = ttk.Frame(self.root, padding=10)
        self.frame.grid()
        self.root.geometry(geometry)
        self.create_buttons()
        self.root.mainloop()

    @abstractmethod
    def create_buttons(self):
        pass

