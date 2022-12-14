import os
import mainscreen
def calculator():
    os.system("cls")
    print("Calculator")
    operation = input("add, sub, mul, div >> ")
    if operation in ("add", "sub", "mul", "div"):
        num1 = int(input("First number >> "))
        num2 = int(input("Second number >> "))
        if operation == "add":
            print(num1 + num2)
            close = input("Press ENTER to exit")
            if (close) == "":
                mainscreen.home()
            else:
                mainscreen.home()
        elif operation == "sub":
            print(num1 - num2)
            close = input("Press ENTER to exit")
            if close:
                mainscreen.home()
        elif operation == "mul":
            print(num1 * num2)
            close = input("Press ENTER to exit")
            if close:
                mainscreen.home()
        elif operation == "div":
            print(num1 / num2)
            close = input("Press ENTER to exit")
            if close:
                mainscreen.home()
    else:
        mainscreen.home()