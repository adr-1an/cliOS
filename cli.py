import time
import os
import keyboard
#importing files
import mainscreen
import appsscreen
import calculatorapp
import helpscreen
import terminalapp
import system_terminalapp
import gamesscreen
#STARTING CODE
os.system("cls")
mainscreen.home()
running = "True"
while running == "True":
    if keyboard.is_pressed("1"):
        appsscreen.apps()
    elif keyboard.is_pressed("2"):
        helpscreen.help()
    elif keyboard.is_pressed("3"):
        terminalapp.terminal()
    elif keyboard.is_pressed("4"):
        gamesscreen.games()