from app.defines import CHROME_BROWSER_PATH
from . mojos import MojosChecker
import threading
import webbrowser
import pyautogui
import datetime

webbrowser.get(CHROME_BROWSER_PATH['windows10'])
urls = ['www.google.com']


class Engine:

    def __init__(self, parser):
        self.__parser = parser
        self.__thread_event = threading.Event()

    def set_thread_event(self):
        self.__thread_event.set()

    def run(self):
        checker = None
        while True and not self.__thread_event.is_set():
            start_time = int(self.__parser.start_time)
            interval = int(self.__parser.interval)
            interval = ((start_time + interval) % 60)
            if datetime.datetime.now().minute == start_time:
                status = pyautogui.confirm(
                    text='Start Automatic 7Mojos Stream Test? \n'
                         'The test is mouse related, \n'
                         'so please dont move your mouse'
                         'during the test.',
                    title='7Mojos Stream Test', buttons=['Yes', 'No'])

                if status == 'Yes':
                    for url in urls:
                        webbrowser.open(url)
                        checker = MojosChecker()
                        checker.run()
                    pyautogui.alert(text="STREAM TEST COMPLETE. \nDon't forget to send Skype message!",
                                    title='7Mojos Stream Test', button='OK')
                    start_time += interval + interval
                    start_time %= 60
                    self.__thread_event.wait(timeout=interval - 1)
                else:
                    self.__thread_event.wait(timeout=interval - 1)
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
                self.__thread_event.wait(timeout=3)
        checker.set_thread_event()
