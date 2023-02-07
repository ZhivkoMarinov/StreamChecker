from GUI.main_app_frame import MainWindow
from GUI.selection_frame import SelectionFrame
from app.arg_parser import CommandLineArguments


class Manager:
    def __init__(self):
        self.parser = CommandLineArguments()
        if not self.parser.is_complete:
            self.selection_frame = SelectionFrame()
            self.main_window = MainWindow()

