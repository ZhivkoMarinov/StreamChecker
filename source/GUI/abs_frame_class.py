from abc import ABC, abstractmethod
from app.defines import GUI_SETTINGS
from tkinter import *

NAME = GUI_SETTINGS['app_name']

class MainFrame(ABC):
    def __init__(self):
        self.root = Tk()
        self.root.title(NAME)
        # self.create_label()
        self.root.geometry('+600+300')
        # self.create_buttons()

    # @abstractmethod
    # def create_buttons(self):
    #     pass

    # @abstractmethod
    # def create_label(self):
    #     pass
