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

chk_mouse_pos = (0, 0)

while True:
    mouse_pos = win32api.GetCursorPos()
    exit = win32api.GetKeyState(0x1B)
    if mouse_pos != chk_mouse_pos:
        playsound(str(boom), 0)
        chk_mouse_pos = mouse_pos
        time.sleep(0.1)
    
    if exit < 0:
        break