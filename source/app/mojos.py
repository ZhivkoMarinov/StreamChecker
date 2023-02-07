from . defines import MOJOS_COORDINATES
import pyautogui
import time


def open_menu():
    pyautogui.moveTo(*MOJOS_COORDINATES['Menu'])
    time.sleep(MOJOS_COORDINATES['Short_sleep'])
    pyautogui.click()
    time.sleep(MOJOS_COORDINATES['Short_sleep'])


def open_audio_video():
    pyautogui.moveTo(*MOJOS_COORDINATES['Audio_Video'])
    time.sleep(MOJOS_COORDINATES['Short_sleep'])
    pyautogui.click()
    time.sleep(MOJOS_COORDINATES['Short_sleep'])


def p480_check():
    pyautogui.moveTo(*MOJOS_COORDINATES["480"])
    time.sleep(MOJOS_COORDINATES['Short_sleep'])
    pyautogui.click()
    time.sleep(MOJOS_COORDINATES['Short_sleep'])
    pyautogui.moveTo(*MOJOS_COORDINATES["Blank_click"])
    pyautogui.click()
    time.sleep(MOJOS_COORDINATES['Long_sleep'])


def p720_check():
    pyautogui.moveTo(*MOJOS_COORDINATES["720"])
    time.sleep(MOJOS_COORDINATES['Short_sleep'])
    pyautogui.click()
    time.sleep(MOJOS_COORDINATES['Short_sleep'])
    pyautogui.moveTo(*MOJOS_COORDINATES["Blank_click"])
    pyautogui.click()
    time.sleep(MOJOS_COORDINATES['Long_sleep'])


def p1080_check():
    pyautogui.moveTo(*MOJOS_COORDINATES["1080"])
    time.sleep(MOJOS_COORDINATES['Short_sleep'])
    pyautogui.click()
    time.sleep(MOJOS_COORDINATES['Short_sleep'])
    pyautogui.moveTo(*MOJOS_COORDINATES["Blank_click"])
    pyautogui.click()
    time.sleep(MOJOS_COORDINATES['Long_sleep'])


# list of pointers to check functions
QUALITY_CHECKS = [p480_check, p720_check, p1080_check]


def run():
    time.sleep(6)
    for check_func in QUALITY_CHECKS:
        open_menu()
        open_audio_video()
        check_func()
    pyautogui.hotkey('ctrl', 'w')

