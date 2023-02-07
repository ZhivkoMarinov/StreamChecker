from app.defines import CHROME_BROWSER_PATH
from app import validate_data
from . import mojos as mj
import webbrowser
import pyautogui
import datetime
import time

webbrowser.get(CHROME_BROWSER_PATH['ubuntu20-22'])
urls = ['www.google.com']


def engine(parser):

    x = parser.start_time
    interval = ((x + parser.interval) % 60)

    while True:
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
                time.sleep(interval - 1)
            else:
                time.sleep(interval - 1)
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
            time.sleep(60)
