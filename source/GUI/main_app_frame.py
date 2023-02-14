import json
import os
from tkinter import *
from tkinter import ttk
from . import main_app_frame_widgets as widgets
from app.defines import GUI_SETTINGS, LOGS
from . abs_frame_class import MainFrame
from . add_edit_frame import AddEdit

NAME = GUI_SETTINGS['app_name']


class MainWindow(MainFrame):
    def __init__(self, arg_json, name=NAME):
        super().__init__(name)
        self.args_json = arg_json

        self.column_left = Frame(self.root, borderwidth=5)
        self.column_left.grid(row=1, column=0, padx=10, pady=10)

        self.column_right = Frame(self.root, borderwidth=5)
        self.column_right.grid(row=1, column=1, padx=10, pady=10)

        self.list_box_frame = Frame(self.column_right)
        self.list_box_frame.grid(row=0, column=0)

        self.text_box_btns_frame = Frame(self.column_right, pady=10)
        self.text_box_btns_frame.grid(row=1, column=0)

        self.st_label = widgets.start_time_label(self.column_left, 0, 0)
        self.st_entry = widgets.start_time_entry(self.column_left, 0, 1)
        self.int_label = widgets.interval_label(self.column_left, 1, 0)
        self.int_entry = widgets.interval_entry(self.column_left, 1, 1)
        self.list_box = widgets.create_list_box(self.list_box_frame, 0, 0)
        self.submit_btn = widgets.submit_button(self.column_left, 2, 0)
        self.add_btn = widgets.add_button(self.text_box_btns_frame, 1, 0, self.get_add)
        self.edit_btn = widgets.edit_button(self.text_box_btns_frame, 1, 1)
        self.delete_btn = widgets.delete_button(self.text_box_btns_frame, 1, 2)
        self.load_content_to_box()
        self.root.mainloop()

    def load_content_to_box(self):
        operator = self.args_json.open_json()['operator']
        with open(os.path.join(LOGS['args_log']['dir'], operator + '_links')) as file:
            json_obj = json.load(file)
            content = json_obj if json_obj else "EMPTY"
            self.list_box.insert(END, content)

    def get_add(self):
        print("natiskam")
        add_edit = AddEdit(self.root)
        self.root.mainloop()

    def create_label(self):
        pass
