# import pyperclip
import pyautogui
from keytype import Shortcut


def key_press(shortcut: Shortcut):
    for key in shortcut["key"]:
        print("keyDonwn : " + key)
        pyautogui.keyDown(key)
    for key in reversed(shortcut["key"]): #逆順
        print("keyUp : " + key)
        pyautogui.keyUp(key)    