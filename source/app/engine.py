from app.defines import CHROME_BROWSER_PATH
from . import mojos as mj
from GUI.json_handler import JsonHandler
import webbrowser
import pyautogui
import datetime
import time

webbrowser.get(CHROME_BROWSER_PATH['windows10'])
urls = ['www.google.com']


def test_func(event):
    x = 0
    while True:
        if event.is_set():
            print("stopped")
            break
        print(x)
        x += 1
        event.wait(timeout=10)


def engine(parser):

    print(parser.interval)
    return
    x = parser.start_time
    interval = ((x + parser.interval) % 60)

    while True and not thread_event.is_set():
        if datetime.datetime.now().minute == x:
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
                x += interval + interval
                x = x % 60
                thread_event.wait(timeout=interval - 1)
            else:
                thread_event.wait(timeout=interval - 1)
        else:
            if x < datetime.datetime.now().minute < interval:
                next_check_time = interval - datetime.datetime.now().minute
                print(f"Time to next check: {next_check_time} minutes")
            else:
                if x < datetime.datetime.now().minute < 60:
                    next_check_time = x + (60 - datetime.datetime.now().minute)
                    print(f"Time to next check: {next_check_time} minutes")
                else:
                    next_check_time = x - datetime.datetime.now().minute
                    print(f"Time to next check: {next_check_time} minutes")
            thread_event.wait(timeout=60)
