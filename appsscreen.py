import os
import system_terminalapp
import keyboard
import calculatorapp
import mainscreen
def appsnocls():
    print("""
-------------------------
|       CLI OS - Apps   |
|c - CALCULATOR         |
|s - SYSTEM TERMINAL    |
|                       |
|Press 0 to GO BACK     |
-------------------------
Abort.
""")
def apps():
    os.system("cls")
    print("""
-------------------------
|       CLI OS - Apps   |
|c - CALCULATOR         |
|s - SYSTEM TERMINAL    |
|                       |
|Press 0 to GO BACK     |
-------------------------
    """)
    while True:
        if keyboard.is_pressed("c"):
            calculatorapp.calculator()
        elif keyboard.is_pressed("s"):
            print("Once you enter the system terminal, you will need to\nrestart the entire CliOS Program in order to exit.")
            yn = input("Do you want to continue? [Y/n] >> ")
            if yn == "Y":
                system_terminalapp.systerminal()
            elif yn == "y":
                system_terminalapp.systerminal()
            elif yn == "n":
                appsnocls()
            elif yn == "N":
                appsnocls()
        elif keyboard.is_pressed("0"):
            mainscreen.home()
            break