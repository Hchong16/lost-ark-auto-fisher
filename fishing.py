import random
import cv2 as cv2
import mss as mss
import numpy as np
from configparser import ConfigParser
from keyboard import is_pressed
from pyautogui import keyUp, keyDown
from time import sleep
from threading import Timer

config = ConfigParser()
config.read('config.ini')


energy = int(config["DEFAULT"]['energy'])
keybind = config["DEFAULT"]['keybind']
NORMAL_INDICATOR = cv2.imread("./assets/indicator.png", 0)

print("""
██      ██████  ███████ ████████      █████  ██████  ██   ██ 
██     ██    ██ ██         ██        ██   ██ ██   ██ ██  ██  
██     ██    ██ ███████    ██        ███████ ██████  █████   
██     ██    ██      ██    ██        ██   ██ ██   ██ ██  ██  
███████ ██████  ███████    ██        ██   ██ ██   ██ ██   ██                                                                                                                                                
""")
print("Program is starting in 5 secs... move your cursor to an applicable location! Press the '=' key or 'CTRL + C' in the terminal to quit anytime!")

keep_track, catch = False, 0 # Determine whether the program should auto quit or not based on energy amount
if energy > 0:
    keep_track = True
    catch = round(int(config["DEFAULT"]['energy'])/60) # Each catch cost 60 energy
    print('[CATCH LEFT]: ' + str(catch))

def delay() -> float:
    """
    To prevent bot detection, randomnize delay between actions.
    """
    return sleep(random.uniform(0, 1))

def automate_press() -> None:
    keyDown(keybind)
    sleep(0.1)
    keyUp(keybind)

def is_caught() -> bool:
    """
    Search for the "!" indicator to determine when the fishing key should be pressed. 
    """
    indicator_img_rgb = np.array(sct.grab({"left": 940, "top": 459, "width": 40, "height": 50}))
    indicator_img_gray = cv2.cvtColor(indicator_img_rgb, cv2.COLOR_BGR2GRAY)

    # Determine whether a fish has been caught.
    indicator_res = cv2.matchTemplate(indicator_img_gray, NORMAL_INDICATOR, cv2.TM_CCOEFF_NORMED)

    _, confidence, _, max_loc = cv2.minMaxLoc(indicator_res)
    if confidence >= 0.8:
        print("FISH CAUGHT!")
        return True

    return False

# Set a timer to automatically cast the fishing line in the case it failed unexpectedly. 
def fail_safe():
    t = Timer(20, automate_press) # On average, catching one fish from start to finish takes around 17 secs.
    t.start()
    return t

sleep(5)
automate_press()
t = fail_safe()

while is_pressed('=') == False or (keep_track and catch == 0):
    with mss.mss() as sct:
        if is_caught():
            t.cancel()
            delay()
            automate_press() # Reel it back!

            sleep(7) # Wait for catch animation
            delay()
            automate_press() # Start next fish
    
            if keep_track:
                catch -= 1
                print('[CATCH LEFT]: ' + str(catch))

            t = fail_safe()
