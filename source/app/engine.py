from .defines import CHROME_BROWSER_PATH, LOGS, ALERT_SOUND, MESSAGE_TO_CLIPBOARD
from .mojos import MojosChecker
from .json_handler import JsonHandler
from playsound import playsound
from datetime import datetime
from pathlib import Path
import pyperclip
import webbrowser
import pyautogui
import time
import os

webbrowser.get(CHROME_BROWSER_PATH['windows10'])
test_urls = ['www.google.com']


class Engine:

    def __init__(self, operator: str, start_time: int, interval: int):
        self.operator = operator
        self.start_time = int(start_time)
        self.interval = int(interval)
        self.json_handler = JsonHandler()
        self.links_file_path = os.path.join(LOGS['args_log']['dir'], self.operator + '_links')
        self.urls = self.get_urls()
        self.alert_sound_path = Path().absolute() / ALERT_SOUND

    def get_urls(self):
        if os.path.exists(self.links_file_path):
            json_obj = self.json_handler.open_json(self.links_file_path)
            urls = [url['url'] for url in json_obj['links']]
            return urls
        else:
            print("URL file not found!")
            exit(1)

    def run(self):

        if self.start_time < datetime.now().minute:
            self.adjust_start_time()

        while True:

            if datetime.now().minute == self.start_time:
                sound = playsound(self.alert_sound_path)
                status = pyautogui.confirm(
                    text='Start Automatic Stream Test? \n'
                         'The test is mouse related, \n'
                         'so please dont move your mouse'
                         'until the test ends!',
                    title='Stream Test', buttons=['Yes', 'No'])
                self.adjust_start_time()

                if status == 'Yes':
                    for url in self.urls:
                        webbrowser.open(url)
                        checker = MojosChecker()
                        checker.run()
                    pyautogui.alert(text="STREAM TEST COMPLETE. \nDon't forget to send Skype message!",
                                    title='Stream Test', button='OK')
                    pyperclip.copy(MESSAGE_TO_CLIPBOARD) #message is ready for pasting
                else:
                    time.sleep(60)
            
            else:
                self.print_next_check_time()
            
            time.sleep(60)

    def adjust_start_time(self):
        self.start_time = (self.start_time + self.interval) % 60


    def print_next_check_time(self):
        next_check_time = self.start_time - datetime.now().minute
        print(f"Time to next check: {next_check_time} minutes")