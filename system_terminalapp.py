import os
import mainscreen
import keyboard
def systerminal():
    os.system("cls")
    print("System Terminal")
    while True:
        command = input("sys.terminal >> ")
        os.system(command)
        if command == "exit":
            exit
        else:
            os.system(command)