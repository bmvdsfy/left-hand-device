import pyautogui
import pyperclip
import time

class KeyStroke:
    def __init__(self) -> None:
        None
    def undo() -> None:
        pyautogui.keyDown("command")
        pyautogui.press("z")
        pyautogui.keyUp("command")
    
    def redo() -> None:
        pyautogui.keyDown("command")
        pyautogui.hotkey("shiftleft", "z")
        pyautogui.keyUp("command")

    def save() -> None:
        pyautogui.keyDown("command")
        pyautogui.press("s")
        pyautogui.keyUp("command")

    
    def nextPage() -> None:
        pyautogui.keyDown("command")
        pyautogui.keyDown("option")

        pyautogui.press("right")
        pyautogui.keyUp("option")
        pyautogui.keyUp("command")

    def prevPage() -> None:
        pyautogui.keyDown("command")
        pyautogui.keyDown("option")

        pyautogui.press("left")
        pyautogui.keyUp("option")
        pyautogui.keyUp("command")

    

if __name__ == "__main__" :
    # pyautogui.typewrite("hello")
    time.sleep(5)
    KeyStroke.nextPage()
    time.sleep(1)
    KeyStroke.nextPage()
    time.sleep(1)
    KeyStroke.nextPage()
    time.sleep(1)
    KeyStroke.prevPage()
    time.sleep(1)
    KeyStroke.prevPage()
