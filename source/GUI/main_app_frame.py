from tkinter import *
from tkinter import ttk
from app.defines import GUI_SETTINGS
from . abs_frame_class import MainFrame

NAME = GUI_SETTINGS['app_name']


class MainWindow(MainFrame):
    def __init__(self, name=NAME):
        super().__init__(name)
        self.column_left = Frame(self.root, borderwidth=5)
        self.column_right = Frame(self.root, borderwidth=5)
        self.column_left.grid(row=1, column=0, padx=10, pady=10)
        self.column_right.grid(row=1, column=1, padx=10, pady=10)
        self.create_input_fields()
        self.create_text_box()
        self.create_buttons()
        self.root.mainloop()

    def create_buttons(self):
        submit_btn = Button(self.column_left, text='START', bg='green')
        submit_btn.grid(row=2, column=0)

    def create_input_fields(self):
        start_time = Label(self.column_left, text='Start time (0-59): ')
        start_time.grid(row=0, column=0, sticky=NW)
        interval = Label(self.column_left, text='Interval (5-55): ')
        interval.grid(row=1, column=0, sticky=NW)

        start_time_entry = Entry(self.column_left, width=5, bd=2)
        start_time_entry.insert(0, '12')
        start_time_entry.grid(row=0, column=1)

        interval_entry = Entry(self.column_left, width=5, bd=2)
        interval_entry.insert(0, '30')
        interval_entry.grid(row=1, column=1)

    def create_text_box(self):
        box = Text(self.column_right, state=DISABLED)
        box.config(width=30, height=10)
        box.grid(row=1, column=0)

    def create_label(self):
        pass
