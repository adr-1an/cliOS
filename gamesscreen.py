def games():
    import os
    import keyboard
    import mainscreen
    import Play
    os.system("cls")
    print("""
-------------------------
|       CLI OS - Games  |
|s - SNAKE              |
|2 - R.P.S              |
|                       |
|Press 0 to GO BACK     |
-------------------------
    """)
    if keyboard.is_pressed("0"):
        mainscreen.home()
    elif keyboard.is_pressed("s"):
        Play.playsnake()