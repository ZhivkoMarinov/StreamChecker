from tkinter import *
from tkinter import ttk
from app.defines import GUI_SETTINGS
from . abs_frame_class import MainFrame

NAME = GUI_SETTINGS['app_name']


class MainWindow(MainFrame):
    def __init__(self, name=NAME):
        super().__init__(name)
        self.column_left = Frame(self.root, borderwidth=5)
        self.column_left.grid(row=1, column=0, padx=10, pady=10)

        self.column_right = Frame(self.root, borderwidth=5)
        self.column_right.grid(row=1, column=1, padx=10, pady=10)

        self.text_box_frame = Frame(self.column_right)
        self.text_box_frame.grid(row=0, column=0)

        self.text_box_btns_frame = Frame(self.column_right, pady=10)
        self.text_box_btns_frame.grid(row=1, column=0)

        self.st_label = self.start_time_label()
        self.st_entry = self.start_time_entry()
        self.int_label = self.interval_label()
        self.int_entry = self.interval_entry()
        self.text_box = self.create_text_box()
        self.submit_btn = self.submit_button()
        self.add_btn = self.add_button()
        self.edit_btn = self.edit_button()
        self.delete_btn = self.delete_button()
        self.root.mainloop()        

    def submit_button(self):
        submit_btn = Button(self.column_left, text='START', bg='green')
        submit_btn.grid(row=2, column=0, pady=10, sticky=E)
        return submit_btn
    
    def add_button(self):
        add_btn = Button(self.text_box_btns_frame, text='Add')
        add_btn.grid(row=1, column=0, padx=5)
        return add_btn
    
    def edit_button(self):
        edit_btn = Button(self.text_box_btns_frame, text='Edit')
        edit_btn.grid(row=1, column=1, padx=5)
        return edit_btn

    def delete_button(self):    
        delete_btn = Button(self.text_box_btns_frame, text='Delete')
        delete_btn.grid(row=1, column=2, padx=5)
        return delete_btn

    def start_time_label(self):
        start_time = Label(self.column_left, text='Start time (0-59): ')
        start_time.grid(row=0, column=0, sticky=NW, pady=10)
        return start_time

    def start_time_entry(self):
        start_time_entry = Entry(self.column_left, width=5, bd=2)
        start_time_entry.insert(0, '12')
        start_time_entry.grid(row=0, column=1, pady=10)
        return start_time_entry
    
    def interval_label(self):
        interval = Label(self.column_left, text='Interval (5-55): ')
        interval.grid(row=1, column=0, sticky=NW, pady=10)
        return interval

    def interval_entry(self):
        interval_entry = Entry(self.column_left, width=5, bd=2)
        interval_entry.insert(0, '30')
        interval_entry.grid(row=1, column=1, pady=10)
        return interval_entry

    def create_text_box(self):
        box = Text(self.text_box_frame, state=DISABLED)
        box.config(width=30, height=10)
        box.grid(row=0, column=0)
        return box

    def create_label(self):
        pass
