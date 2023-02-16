from GUI.main_app_frame import MainWindow
from GUI.selection_frame import SelectionFrame
from GUI.json_handler import JsonHandler
from app.arg_parser import CommandLineArguments
from . defines import LOGS


class Manager:
    def __init__(self):
        self.parser = CommandLineArguments()
        self.json_handler = JsonHandler(LOGS['args_log']['dir'], LOGS['args_log']['file'])
        self.json_handler.json_init()
        if not self.parser.is_complete:
            self.selection_frame = SelectionFrame(self.json_handler)
            self.main_window = MainWindow(self.json_handler)

