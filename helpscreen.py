import os
import keyboard
import mainscreen
def help():
    os.system("cls")
    print("""
-------------------------
|     CLI OS - Help     |
|                       |
|                       |
|                       |
|Press 0 to GO BACK     |
-------------------------
""")
    while True:
        if keyboard.is_pressed("0"):
            mainscreen.home()
            break