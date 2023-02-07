import os
from tkinter import *
from tkinter import ttk
from app.defines import OPERATORS, GUI_SETTINGS, LOGS
from . abs_frame_class import MainFrame

NAME = GUI_SETTINGS['selection_window']['name']
GEOMETRY = GUI_SETTINGS['selection_window']['geometry']


class SelectionFrame(MainFrame):
    def __init__(self, name=NAME, geometry=GEOMETRY):
        super().__init__(name, geometry)

    def create_buttons(self):
        for idx, operator in enumerate(OPERATORS):
            btn = Button(self.root,
                         height=2,
                         width=10,
                         text=operator.upper(),
                         command=lambda m=operator: self.select_operator_and_quit(m)
                         )
            btn.grid(padx=10, pady=10, column=idx, row=1)

    def create_label(self):
        Label(self.frame, text="Select operator").grid(column=0, row=0)

    def select_operator_and_quit(self, button_pressed):
        with open(os.path.join(LOGS['args_log']['dir'], LOGS['args_log']['file']), 'w+') as file:
            file.write(button_pressed)
        self.root.destroy()
