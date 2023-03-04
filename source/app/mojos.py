from .defines import MOJOS_COORDINATES
import pyautogui
import time


class MojosChecker:

    def __init__(self):
        # list of pointers to check functions
        self.__quality_checks = [self.p480_check, self.p720_check, self.p1080_check]

    @staticmethod
    def open_menu():
        pyautogui.moveTo(*MOJOS_COORDINATES['Menu'])
        time.sleep(MOJOS_COORDINATES['Short_sleep'])
        pyautogui.click()
        time.sleep(MOJOS_COORDINATES['Short_sleep'])

    @staticmethod
    def open_audio_video():
        pyautogui.moveTo(*MOJOS_COORDINATES['Audio_Video'])
        time.sleep(MOJOS_COORDINATES['Short_sleep'])
        pyautogui.click()
        time.sleep(MOJOS_COORDINATES['Short_sleep'])

    @staticmethod
    def p480_check():
        pyautogui.moveTo(*MOJOS_COORDINATES["480"])
        time.sleep(MOJOS_COORDINATES['Short_sleep'])
        pyautogui.click()
        time.sleep(MOJOS_COORDINATES['Short_sleep'])
        pyautogui.moveTo(*MOJOS_COORDINATES["Blank_click"])
        pyautogui.click()
        time.sleep(MOJOS_COORDINATES['Long_sleep'])

    @staticmethod
    def p720_check():
        pyautogui.moveTo(*MOJOS_COORDINATES["720"])
        time.sleep(MOJOS_COORDINATES['Short_sleep'])
        pyautogui.click()
        time.sleep(MOJOS_COORDINATES['Short_sleep'])
        pyautogui.moveTo(*MOJOS_COORDINATES["Blank_click"])
        pyautogui.click()
        time.sleep(MOJOS_COORDINATES['Long_sleep'])

    @staticmethod
    def p1080_check():
        pyautogui.moveTo(*MOJOS_COORDINATES["1080"])
        time.sleep(MOJOS_COORDINATES['Short_sleep'])
        pyautogui.click()
        time.sleep(MOJOS_COORDINATES['Short_sleep'])
        pyautogui.moveTo(*MOJOS_COORDINATES["Blank_click"])
        pyautogui.click()
        time.sleep(MOJOS_COORDINATES['Long_sleep'])

    def run(self):
        time.sleep(6)
        for check_func in self.__quality_checks:
            self.open_menu()
            self.open_audio_video()
            check_func()
        pyautogui.hotkey('ctrl', 'w')
