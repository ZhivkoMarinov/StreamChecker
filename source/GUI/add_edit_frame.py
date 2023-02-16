from tkinter import *
from app.defines import LOGS
from . json_handler import JsonHandler


class AddEdit:

    def __init__(self, main_win, file_path):
        self.main_win = main_win
        self.win = Toplevel(main_win)
        self.win.grab_set()
        self.win.attributes('-topmost', True)
        self.win.geometry('+800+400')
        self.main_frame = Frame(self.win)
        self.main_frame.grid(row=0, column=0)
        self.name = self.name()
        self.url = self.url()
        self.ok_btn = self.ok_button()
        self.cancel_btn = self.cancel_button()
        self.file_path = file_path

    def name(self):
        label_name = Label(self.main_frame, text="Name")
        label_name_entry = Entry(self.main_frame)
        label_name.grid(row=0, column=0)
        label_name_entry.grid(row=0, column=1)
        return label_name_entry

    def url(self):
        label_url = Label(self.main_frame, text='URL')
        label_url_entry = Entry(self.main_frame)
        label_url.grid(row=1, column=0)
        label_url_entry.grid(row=1, column=1)
        return label_url_entry

    def ok_button(self):
        ok_btn = Button(self.main_frame, text="Save", command=self.retrieve_input)
        ok_btn.grid(row=2, column=0, padx=50, pady=10)
        return ok_btn

    def retrieve_input(self):
        # json_handler = JsonHandler(LOGS[''])
        # json_dict = {'name': None, 'url': None}
        self.win.destroy()

    def cancel_button(self):
        cancel_btn = Button(self.main_frame, text='Cancel', command=self.win.destroy)
        cancel_btn.grid(row=2, column=1)
        return cancel_btn
