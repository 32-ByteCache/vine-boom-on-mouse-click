import winsound
import win32api
from pynput import mouse
import time



while True:
    click = win32api.GetKeyState(0x01)
    exit = win32api.GetKeyState(0x1B)
    if click < 0:
        winsound.PlaySound('Vine_boom_sound_effect', winsound.SND_FILENAME)
        
    if exit < 0:
        break
    #print(click)
    #time.sleep(0.2)

    
#def on_click(x, y, button, pressed):
#    winsound.PlaySound('Vine_boom_sound_effect', winsound.SND_FILENAME)

#with mouse.Listener(
#    on_click=on_click
#) as listner:
#    listner.join()