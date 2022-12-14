import os
import mainscreen
import terminalroot
from getpass import getpass
def terminal():
    os.system("cls")
    passwd = "null"
    passfile = "password.txt"
    passwordfile = open(passfile, mode="r")
    passwd = passwordfile.read()
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
            elif passwd != "null":
                currentpassword = getpass("Current password >> ")
                if currentpassword == passwd:
                    passwd = getpass("Set a password >> ")
                    passwdverify = getpass("Confirm your password >> ")
                    if passwdverify == passwd:
                        print("Successfully set password.")
                        file = open("password.txt", "w")
                        file.write(passwd)
                        file.close()
                    elif passwdverify != passwd:
                        print("Incorrect password.")
                elif currentpassword != passwd:
                    print("Incorrect password.")
        elif command == "help":
            print("Help!")
        elif command == "exit":
            mainscreen.home()
            break
        elif command == "su":
            if passwd == "null":
                terminalroot.terminalroot()
            else:
                currentpassword = getpass("Password for root >> ")
                if currentpassword == passwd:
                    terminalroot.terminalroot()
                else:
                    print("Incorrect password.")
        elif command == "poweroff":
            print("Poweroff: Permission denied.")
        elif command == "sudo poweroff":
            if passwd == "null":
                print("Logout")
                exit()
            else:
                currentpassword = getpass("sudo: Password for root >> ")
                if currentpassword == passwd:
                    exit()
                else:
                    print("Incorrect password.")
        elif command == "":
            pass
        elif command == "sudo getpass":
            currentpassword = getpass("sudo: Password for root >> ")
            if currentpassword == passwd:
                passfile = "password.txt"
                passwordfile = open(passfile, mode="r")
                print(passwordfile.read())
            else:
                print("Incorrect password.")
        elif command == "getpass":
            print("getpass: Permission denied.")
        elif command == "ssh":
            sshcommand = input("Enter the full SSH command >> ")
            if "ssh" in sshcommand:
                os.system(sshcommand)
            else:
                print("Incorrect SSH command usage.")
        elif command == "nano":
            os.system("nano")
        if command == "mkdir":
            print("mkdir")
        else:
            print("Error: Unrecognized command.")