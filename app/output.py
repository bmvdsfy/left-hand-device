# import pyperclip
import time

import pyautogui
import pyperclip
from keytype import Shortcut


def proceed_shortcut(shortcut: Shortcut):
    keys = shortcut["key"]
    if keys[0] == "TypewriteWithClipboard":
        pyperclip.copy(keys[1])
        _key_press(["command", "v"])
        print("paste done")

    else:
        _key_press(keys)



def _key_press(keys: list[str]):
    # キー入力ショートカット
    for key in keys:
        print("keyDonwn : " + key)
        pyautogui.keyDown(key)
        time.sleep(0.1)
    for key in reversed(keys): #逆順
        print("keyUp : " + key)
        pyautogui.keyUp(key)    
        time.sleep(0.1)