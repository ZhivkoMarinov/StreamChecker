from tkinter import *
from tkinter import ttk
from app.defines import OPERATORS, GUI_SETTINGS
from abs_frame_class import MainFrame


class SelectionFrame(MainFrame):
    def __init__(self, name: str, geometry: str):
        super().__init__(name, geometry)

    def create_buttons(self):
        for idx, operator in enumerate(OPERATORS):
            btn = Button(self.root,
                         height=2,
                         width=10,
                         text=operator.upper(),
                         command=lambda m=f'{operator} is clicked': self.which_button(m)
                         )
            btn.grid(padx=10, pady=10, column=idx, row=1)

    def create_label(self):
        Label(self.frame, text="Select operator").grid(column=0, row=0)

    @staticmethod
    def which_button(button_pressed):
        return button_pressed


a = SelectionFrame(GUI_SETTINGS['selection_window']['name'], GUI_SETTINGS['selection_window']['geometry'])
a.create_buttons()
