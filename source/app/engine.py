from defines import CHROME_BROWSER_PATH, LOGS
from mojos import MojosChecker
from json_handler import JsonHandler
import webbrowser
import pyautogui
import datetime
import time
import sys
import os

webbrowser.get(CHROME_BROWSER_PATH['windows10'])
test_urls = ['www.google.com']


class Engine:

    def __init__(self, operator, start_time, interval):
        self.operator = operator
        self.start_time = start_time
        self.interval = interval
        self.json_handler = JsonHandler()
        self.links_file_path = os.path.join(LOGS['args_log']['dir'], self.operator + '_links')
        self.urls = self.get_urls()

    def get_urls(self):
        if os.path.exists(self.links_file_path):
            json_obj = self.json_handler.open_json(self.links_file_path)
            urls = [url['url'] for url in json_obj['links']]
            return urls
        else:
            print("URL file not found!")
            exit(1)

    def run(self):
        while True:
            start_time = int(self.start_time)
            interval = int(self.interval)
            interval = ((start_time + interval) % 60)
            if datetime.datetime.now().minute == start_time:
                status = pyautogui.confirm(
                    text='Start Automatic 7Mojos Stream Test? \n'
                         'The test is mouse related, \n'
                         'so please dont move your mouse'
                         'during the test.',
                    title='7Mojos Stream Test', buttons=['Yes', 'No'])

                if status == 'Yes':
                    for url in self.urls:
                        webbrowser.open(url)
                        checker = MojosChecker()
                        checker.run()
                    pyautogui.alert(text="STREAM TEST COMPLETE. \nDon't forget to send Skype message!",
                                    title='7Mojos Stream Test', button='OK')
                    start_time += interval + interval
                    start_time %= 60
                    time.sleep(60)
            else:
                if start_time < datetime.datetime.now().minute < interval:
                    next_check_time = interval - datetime.datetime.now().minute
                    print(f"Time to next check: {next_check_time} minutes")
                else:
                    if start_time < datetime.datetime.now().minute < 60:
                        next_check_time = start_time + (60 - datetime.datetime.now().minute)
                        print(f"Time to next check: {next_check_time} minutes")
                    else:
                        next_check_time = start_time - datetime.datetime.now().minute
                        print(f"Time to next check: {next_check_time} minutes")
                time.sleep(60)


if __name__ == "__main__":
    print(sys.argv)
    engine = Engine(sys.argv[1], sys.argv[2], sys.argv[3])
    engine.run()
