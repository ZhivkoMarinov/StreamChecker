from GUI.main_app_frame import MainWindow
from GUI.selection_frame import SelectionFrame
from GUI.json_create import JsonHandler
from app.arg_parser import CommandLineArguments
from . defines import LOGS


class Manager:
    def __init__(self):
        self.parser = CommandLineArguments()
        self.arg_json = JsonHandler(LOGS['args_log']['dir'], LOGS['args_log']['file'])
        self.arg_json.json_init()
        if not self.parser.is_complete:
            self.selection_frame = SelectionFrame(self.arg_json)
            self.main_window = MainWindow(self.arg_json)

