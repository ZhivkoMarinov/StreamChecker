from .defines import MOJOS_COORDINATES
import threading
import pyautogui
import time


class MojosChecker:

    def __init__(self):
        # list of pointers to check functions
        self.__quality_checks = [self.p480_check, self.p720_check, self.p1080_check]
        self.__thread_event = threading.Event()

    def set_thread_event(self):
        self.__thread_event.set()

    def clear_thread_event(self):
        self.__thread_event.clear()

    def open_menu(self):
        while not self.__thread_event.is_set():
            pyautogui.moveTo(*MOJOS_COORDINATES['Menu'])
            time.sleep(MOJOS_COORDINATES['Short_sleep'])
            # self.__thread_event.wait(MOJOS_COORDINATES['Short_sleep'])
            pyautogui.click()
            time.sleep(MOJOS_COORDINATES['Short_sleep'])
            # self.__thread_event.wait(MOJOS_COORDINATES['Short_sleep'])

    def open_audio_video(self):
        while not self.__thread_event.is_set():
            pyautogui.moveTo(*MOJOS_COORDINATES['Audio_Video'])
            time.sleep(MOJOS_COORDINATES['Short_sleep'])
            # self.__thread_event.wait(MOJOS_COORDINATES['Short_sleep'])
            pyautogui.click()
            time.sleep(MOJOS_COORDINATES['Short_sleep'])
            # self.__thread_event.wait(MOJOS_COORDINATES['Short_sleep'])

    def p480_check(self):
        while not self.__thread_event.is_set():
            pyautogui.moveTo(*MOJOS_COORDINATES["480"])
            time.sleep(MOJOS_COORDINATES['Short_sleep'])
            # self.__thread_event.wait(MOJOS_COORDINATES['Short_sleep'])
            pyautogui.click()
            time.sleep(MOJOS_COORDINATES['Short_sleep'])
            # self.__thread_event.wait(MOJOS_COORDINATES['Short_sleep'])
            pyautogui.moveTo(*MOJOS_COORDINATES["Blank_click"])
            pyautogui.click()
            time.sleep(MOJOS_COORDINATES['Long_sleep'])
            # self.__thread_event.wait(MOJOS_COORDINATES['Long_sleep'])
            break

    def p720_check(self):
        while not self.__thread_event.is_set():
            pyautogui.moveTo(*MOJOS_COORDINATES["720"])
            time.sleep(MOJOS_COORDINATES['Short_sleep'])
            # self.__thread_event.wait(MOJOS_COORDINATES['Short_sleep'])
            pyautogui.click()
            time.sleep(MOJOS_COORDINATES['Short_sleep'])
            # self.__thread_event.wait(MOJOS_COORDINATES['Short_sleep'])
            pyautogui.moveTo(*MOJOS_COORDINATES["Blank_click"])
            pyautogui.click()
            time.sleep(MOJOS_COORDINATES['Long_sleep'])
            # self.__thread_event.wait(MOJOS_COORDINATES['Long_sleep'])
            break

    def p1080_check(self):
        while not self.__thread_event.is_set():
            pyautogui.moveTo(*MOJOS_COORDINATES["1080"])
            time.sleep(MOJOS_COORDINATES['Short_sleep'])
            # self.__thread_event.wait(MOJOS_COORDINATES['Short_sleep'])
            pyautogui.click()
            time.sleep(MOJOS_COORDINATES['Short_sleep'])
            # self.__thread_event.wait(MOJOS_COORDINATES['Short_sleep'])
            pyautogui.moveTo(*MOJOS_COORDINATES["Blank_click"])
            pyautogui.click()
            time.sleep(MOJOS_COORDINATES['Long_sleep'])
            # self.__thread_event.wait(MOJOS_COORDINATES['Long_sleep'])
            break

    def run(self):
        # time.sleep(6)
        while not self.__thread_event.is_set():
            self.__thread_event.wait(6)
            for check_func in self.__quality_checks:
                self.open_menu()
                self.open_audio_video()
                check_func()
            pyautogui.hotkey('ctrl', 'w')
            break
