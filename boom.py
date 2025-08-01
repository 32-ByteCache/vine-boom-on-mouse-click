from playsound import playsound
import win32api
import ctypes
from pathlib import Path
import time


SCRIPT_DIR = Path(__file__).parent
boom = SCRIPT_DIR / 'boom.wav'

kernel32 = ctypes.WinDLL('kernel32')
user32 = ctypes.WinDLL('user32')

SW_HIDE = 0
hWnd = kernel32.GetConsoleWindow()
user32.ShowWindow(hWnd, SW_HIDE)

while True:
    click = win32api.GetKeyState(0x01)
    exit = win32api.GetKeyState(0x1B)
    if click < 0:
        playsound(str(boom), 0)
        time.sleep(0.15)
    if exit < 0:
        break