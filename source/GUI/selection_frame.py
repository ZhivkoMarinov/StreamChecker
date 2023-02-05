from tkinter import *
from tkinter import ttk
from app.defines import OPERATORS


class SelectionFrame:
    def __init__(self):
        self.root = Tk()
        self.frame = ttk.Frame(self.root, padding=10)
        self.frame.grid()
        self.root.geometry('400x100')
        self.create_buttons()
        self.root.mainloop()

    def create_buttons(self):
        for idx, operator in enumerate(OPERATORS):
            btn = Button(self.root,
                         height=2,
                         width=10,
                         text=operator.upper(),
                         command=lambda m=f'{operator} is clicked': self.which_button(m)
                         )
            btn.grid(padx=10, pady=10, column=idx, row=1)

    @staticmethod
    def which_button(button_pressed):
        print(button_pressed)


a = SelectionFrame()
a.create_buttons()
