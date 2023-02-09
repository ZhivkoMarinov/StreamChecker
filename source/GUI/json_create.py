import os
import json

JSON_DICT = {
            'operator': None,
            'start_time': None,
            'interval': None
        }

class JsonHandler:
    
    def __init__(self, dir_path, file_name):
        self.dir_path = dir_path
        self.file_name = file_name
        if not os.path.exists(self.dir_path):
            os.mkdir(self.dir_path)
        self.json_init()

    def json_init(self):
        with open(os.path.join(self.dir_path, self.file_name), 'w+') as file:
            json.dump(JSON_DICT, file)
        if not os.path.isfile(os.path.join(self.dir_path, self.file_name)):
            raise SystemError("Can't create file system. Check folder permissions. Terminating!")
            exit(1)

    def open_json(self):
        with open(os.path.join(self.dir_path, self.file_name), 'r') as file:
            json_object = json.load(file)
            return json_object

    def write_to_json(self, json_object):
        with open(os.path.join(self.dir_path, self.file_name), 'w+') as file:
            json.dump(json_object, file)

    def save_operator(self, value):
        json_object = self.open_json()
        json_object['operator'] = value
        self.write_to_json(json_object)            

        