import os
from tkinter import *
from . import main_app_frame_widgets as widgets
from app.defines import GUI_SETTINGS, LOGS
from app.engine import Engine
from . abs_frame_class import MainFrame
from . add_edit_frame import AddEdit

NAME = GUI_SETTINGS['app_name']


class MainWindow(MainFrame):
    def __init__(self, json_handler, parser, name=NAME):
        super().__init__(name)
        self.json_handler = json_handler

        # Frames
        self.column_left = Frame(self.root, borderwidth=5)
        self.column_left.grid(row=1, column=0, padx=10, pady=10)
        self.column_right = Frame(self.root, borderwidth=5)
        self.column_right.grid(row=1, column=1, padx=10, pady=10)
        self.list_box_frame = Frame(self.column_right)
        self.list_box_frame.grid(row=0, column=0)
        self.text_box_btns_frame = Frame(self.column_right, pady=10)
        self.text_box_btns_frame.grid(row=1, column=0)

        # Widgets
        self.st_label = widgets.start_time_label(self.column_left, 0, 0)
        self.st_entry = widgets.start_time_entry(self.column_left, 0, 1)
        self.int_label = widgets.interval_label(self.column_left, 1, 0)
        self.int_entry = widgets.interval_entry(self.column_left, 1, 1)
        self.list_box = widgets.create_list_box(self.list_box_frame, 0, 0)
        self.submit_btn = widgets.submit_button(self.column_left, 2, 0, self.start)
        self.add_btn = widgets.add_button(self.text_box_btns_frame, 1, 0, self.add_edit_window)
        self.edit_btn = widgets.edit_button(self.text_box_btns_frame, 1, 1, self.get_listbox_item)
        self.delete_btn = widgets.delete_button(self.text_box_btns_frame, 1, 2, self.delete_item)

        # some class properties and method calls
        self.parser = parser
        self.is_running = False
        self.operator = self.json_handler.open_json()['operator']
        self.links_file_path = os.path.join(LOGS['args_log']['dir'], self.operator + '_links')
        self.load_content_to_box()
        self.root.protocol('WM_DELETE_WINDOW', self.close_window)
        self.root.mainloop()

    def load_content_to_box(self):
        self.list_box.delete(0, END)
        json_obj = self.json_handler.open_json(json_path=self.links_file_path)
        for idx, item in enumerate(json_obj['links']):
            if item['name'] and item['url']:
                self.list_box.insert(END, f"{item['name']}")

    def get_listbox_item(self):
        try:
            selected_item = self.list_box.curselection()[0]
        except IndexError:
            return

        json_obj = self.json_handler.open_json(json_path=self.links_file_path)
        a = AddEdit(self.root, self.json_handler, self.links_file_path, self.load_content_to_box, selected_item)
        a.name.insert(0, json_obj['links'][selected_item]['name'])
        a.url.insert(0, json_obj['links'][selected_item]['url'])

    def add_edit_window(self):
        AddEdit(self.root, self.json_handler, self.links_file_path, self.load_content_to_box)

    def delete_item(self):
        for idx in self.list_box.curselection():
            json_obj = self.json_handler.open_json(json_path=self.links_file_path)
            del json_obj['links'][idx]
            self.json_handler.write_to_json(json_obj, file_path=self.links_file_path)
        self.load_content_to_box()

    def start(self):
        engine = None
        if not self.is_running:
            start_time = self.st_entry.get()
            interval = self.int_entry.get()
            if start_time and interval:
                self.json_handler.save_start_time(start_time)
                self.json_handler.save_interval(interval)
                self.parser.start_time = start_time
                self.parser.interval = interval
                self.submit_btn.configure(text='STOP', bg='red', activebackground='red')
                self.is_running = True
                engine = Engine(self.parser)
                engine.run()
        else:
            self.submit_btn.configure(text='START', bg='green', activebackground='green')
            self.is_running = False
            if engine:
                engine.set_thread_event()

    def create_label(self):
        pass

    def close_window(self):
        self.root.destroy()
