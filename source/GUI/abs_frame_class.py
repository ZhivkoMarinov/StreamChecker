from abc import ABC, abstractmethod
from tkinter import *


class MainFrame(ABC):
    def __init__(self, name: str):
        self.root = Tk()
        self.root.title(name)
        self.create_label()
        self.root.geometry('+600+300')
        # self.create_buttons()

    # @abstractmethod
    # def create_buttons(self):
    #     pass

    # @abstractmethod
    # def create_label(self):
    #     pass
