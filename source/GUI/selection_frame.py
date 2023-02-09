import os
from tkinter import *
from tkinter import ttk
from .json_create import JsonHandler
from .abs_frame_class import MainFrame
from app.defines import OPERATORS, GUI_SETTINGS, LOGS

NAME = GUI_SETTINGS['app_name']


class SelectionFrame(MainFrame):
    def __init__(self, name=NAME):
        super().__init__(name)
        self.create_buttons()
        self.root.mainloop()

    def create_buttons(self):
        for idx, operator in enumerate(OPERATORS):
            btn = Button(
                self.root,
                height=2,
                width=10,
                text=operator.upper(),
                command=lambda m=operator: self.select_operator_and_quit(m)
            )
            btn.grid(row=2, column=idx, padx=10, pady=10)

    def create_label(self):
        label = Label(self.root, text='Select operator', font='bold')
        label.grid(row=1, column=1)

    def select_operator_and_quit(self, button_pressed):
        handler = JsonHandler(LOGS['args_log']['dir'], LOGS['args_log']['file'])
        handler.save_operator(button_pressed)
        self.root.destroy()
