from tkinter import *
from tkinter import ttk
from app.defines import GUI_SETTINGS
from . abs_frame_class import MainFrame

NAME = GUI_SETTINGS['main_window']['name']
GEOMETRY = GUI_SETTINGS['main_window']['geometry']


class MainWindow(MainFrame):
    def __init__(self, name=NAME, geometry=GEOMETRY):
        super().__init__(name, geometry)

    def create_buttons(self):
        Button(self.root, text='test').grid()
