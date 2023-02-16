import os
import json
from app.defines import LOGS, OPERATORS

JSON_ARGS_DICT = {
    'operator': None,
    'start_time': None,
    'interval': None
}

LINKS = {
    'links': [
        {
            'name': None,
            'url': None
        }
    ]
}


class JsonHandler:

    def __init__(self, dir_path=None, file_name=None):
        self.dir_path = dir_path
        self.file_name = file_name
        if dir_path and file_name:
            if not os.path.exists(self.dir_path):
                os.mkdir(self.dir_path)

    def json_init(self):
        with open(os.path.join(self.dir_path, self.file_name), 'w+') as file:
            json.dump(JSON_ARGS_DICT, file)

        for operator in OPERATORS:
            try:
                with open(os.path.join(LOGS['args_log']['dir'], operator + '_links'), 'x') as file:
                    json.dump(LINKS, file)
            except FileExistsError:
                pass

        if not os.path.isfile(os.path.join(self.dir_path, self.file_name)):
            raise SystemError("Can't create file. Check folder permissions.")

    def open_json(self, json_path=None):
        default_path = json_path if json_path else os.path.join(self.dir_path, self.file_name)
        if json_path:
            default_path = json_path

        with open(default_path, 'r') as file:
            return json.load(file)

    def write_to_json(self, json_object, file_path=None):
        f_path = file_path if file_path else os.path.join(self.dir_path, self.file_name)
        if f_path:
            with open(f_path, 'w+') as file:
                json.dump(json_object, file)
        else:
            # TODO: needs a pop-up window... maybe
            pass

    def append_to_json(self, new_data, file_path=None):
        f_path = file_path if file_path else os.path.join(self.dir_path, self.file_name)
        if f_path:
            with open(f_path, 'w+') as file:
                file_data = json.load(file)
                file_data['links'].append(new_data)
                json.dump(file_data, file)
        else:
            # TODO: needs a pop-up window... maybe
            pass

    def save_operator(self, value):
        json_object = self.open_json()
        json_object['operator'] = value
        self.write_to_json(json_object)
