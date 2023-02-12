import os
from tkinter import *
from tkinter import ttk
from .abs_frame_class import MainFrame
from app.defines import OPERATORS, GUI_SETTINGS

NAME = GUI_SETTINGS['app_name']


class SelectionFrame(MainFrame):
    def __init__(self, arg_json, name=NAME):
        super().__init__(name)
        self.args_json = arg_json
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
        self.args_json.save_operator(button_pressed)
        self.root.destroy()
