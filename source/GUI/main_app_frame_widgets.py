from tkinter import *


def submit_button(frame, r, c):
    submit_btn = Button(frame, text='START', bg='green')
    submit_btn.grid(row=r, column=c, pady=10, sticky=E)
    return submit_btn


def add_button(frame, r, c, func):
    add_btn = Button(frame, text='Add', command=func)
    add_btn.grid(row=r, column=c, padx=5)
    return add_btn


def edit_button(frame, r, c, func):
    edit_btn = Button(frame, text='Edit', command=func)
    edit_btn.grid(row=r, column=c, padx=5)
    return edit_btn


def delete_button(frame, r, c):
    delete_btn = Button(frame, text='Delete')
    delete_btn.grid(row=r, column=c, padx=5)
    return delete_btn


def start_time_label(frame, r, c):
    start_time = Label(frame, text='Start time (0-59): ')
    start_time.grid(row=r, column=c, sticky=NW, pady=10)
    return start_time


def start_time_entry(frame, r, c):
    entry = Entry(frame, width=5, bd=2)
    entry.insert(0, '12')
    entry.grid(row=r, column=c, pady=10)
    return entry


def interval_label(frame, r, c):
    interval = Label(frame, text='Interval (5-55): ')
    interval.grid(row=r, column=c, sticky=NW, pady=10)
    return interval


def interval_entry(frame, r, c):
    entry = Entry(frame, width=5, bd=2)
    entry.insert(0, '30')
    entry.grid(row=r, column=c, pady=10)
    return entry


def create_list_box(frame, r, c):
    box = Listbox(frame, selectmode=SINGLE)
    scroll = Scrollbar(frame, bg='black')
    box.config(width=30, height=10, yscrollcommand=scroll.set)
    scroll.config(command=box.yview)
    box.grid(row=r, column=c)
    scroll.grid(row=r, column=1)
    return box
