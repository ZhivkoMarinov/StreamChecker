from app.defines import CHROME_BROWSER_PATH
from . import mojos as mj
import threading
import webbrowser
import pyautogui
import datetime

webbrowser.get(CHROME_BROWSER_PATH['windows10'])
urls = ['www.google.com']


def engine(parser):
    thread_event = threading.Event()

    while True and not thread_event.is_set():
        print(parser.operator, parser.start_time, parser.interval)
        start_time = int(parser.start_time)
        interval = int(parser.interval)
        interval = ((start_time + interval) % 60)
        if datetime.datetime.now().minute == start_time:
            status = pyautogui.confirm(
                text='Start Automatic 7Mojos Stream Test? \nThe test is mouse related, \nso please dont move your mouse'
                     'during the test.',
                title='7Mojos Stream Test', buttons=['Yes', 'No'])

            if status == 'Yes':
                for url in urls:
                    webbrowser.open(url)
                    mj.run()
                pyautogui.alert(text="STREAM TEST COMPLETE. \nDon't forget to send Skype message!",
                                title='7Mojos Stream Test', button='OK')
                start_time += interval + interval
                start_time %= 60
                thread_event.wait(timeout=interval - 1)
            else:
                thread_event.wait(timeout=interval - 1)
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
            thread_event.wait(timeout=3)
