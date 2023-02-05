from tkinter import *
from tkinter import ttk
from abs_frame_class import MainFrame


class MainWindow(MainFrame):
    def __init__(self, name: str, geometry: str):
        super().__init__(name, geometry)

    def create_buttons(self):
        pass


if __name__ == "__main__":
    a = MainWindow('StreamChecker', '1200x900')
