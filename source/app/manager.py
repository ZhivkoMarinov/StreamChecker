from GUI.selection_frame import SelectionFrame
from GUI.json_handler import JsonHandler
from app.arg_parser import CommandLineArguments
from . defines import LOGS
import threading


class Manager:
    def __init__(self):
        self.parser = CommandLineArguments()
        self.json_handler = JsonHandler(dir_path=LOGS['args_log']['dir'], file_name=LOGS['args_log']['file'])
        self.json_handler.json_init()
        if not self.parser.is_complete:
            threading.Thread(target=SelectionFrame, args=(self.json_handler, self.parser.argument_parser)).start()
            # self.selection_frame = SelectionFrame(self.json_handler, self.parser.argument_parser)
            # self.main_window = MainWindow(self.json_handler, self.parser.argument_parser)
