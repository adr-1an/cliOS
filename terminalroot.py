import os
import keyboard
import mainscreen
from getpass import getpass
def terminalroot():
    os.system("cls")
    print("CLI OS Terminal - Welcome")
    print("Type 'help' for help.")
    print("Warning: This is a root terminal.")
    while True:
        command = input("root@cliOS:~# ")
        print("CLI OS Terminal - Welcome")
        print("Type 'help' for help.")
        while True:
            command = input("user@cliOS:~$ ")
            if command == "passwd":
                if passwd == "null":
                    passwd = getpass("Set a password >> ")
                    passwdverify = getpass("Confirm your password >> ")
                    if passwdverify == passwd:
                        print("Successfully set password.")
                        file = open("password.txt", "w")
                        file.write(passwd)
                        file.close()
            elif command == "help":
                print("Help!")
            elif command == "exit":
                mainscreen.home()
                break
            elif command == "su":
                print("You are already root. Type 'exit' to exit.")
            elif command == "":
                pass
            elif command == "ssh":
                sshcommand = input("Enter the full SSH command >> ")
                if "ssh" in sshcommand:
                    os.system(sshcommand)
                else:
                    print("Incorrect SSH command usage.")
            else:
                print("Error: Unrecognized command.")