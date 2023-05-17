from GUI.selection_frame import SelectionFrame
from GUI.main_app_frame import MainWindow
from app.json_handler import JsonHandler
from app.arg_parser import CommandLineArguments
from app.engine import Engine
from . defines import LOGS


class Manager:
    def __init__(self):
        self.parser = CommandLineArguments()
        self.json_handler = JsonHandler(dir_path=LOGS['args_log']['dir'], file_name=LOGS['args_log']['file'])
        self.json_handler.json_init()
        if not self.parser.is_complete:
            self.selection_frame = SelectionFrame(self.json_handler)
            self.main_window = MainWindow(self.json_handler)
            args = self.json_handler.open_json()
            engine = Engine(args['operator'], args['start_time'], args['interval'])
            engine.run()
