import msvcrt
import time
import os

def menu():
    print(
    """
    _________________________________________________________________
      ██████    ██████       ██   ███████    ██    ██████    ██   ██  
     ██    ██   ██   ██      ██       ██     ██   ██    ██   ███  ██  
     ██    ██   ██████       ██      ██      ██   ██    ██   ████ ██  
     ██    ██   ██  ██       ██     ██       ██   ██    ██   ██  ███  
      ██████    ██   ██████  ██    ████████  ██    ██████    ██   ██
    _________________________________________________________________""")

    print("    [1] New Game")
    print("    [2] Load Game")
    print("    [3] Settings")
    print("    [4] Quit")

def newGameSelected():
    print(
    """
    _________________________________________________________________
      ██████    ██████       ██   ███████    ██    ██████    ██   ██  
     ██    ██   ██   ██      ██       ██     ██   ██    ██   ███  ██  
     ██    ██   ██████       ██      ██      ██   ██    ██   ████ ██  
     ██    ██   ██  ██       ██     ██       ██   ██    ██   ██  ███  
      ██████    ██   ██████  ██    ████████  ██    ██████    ██   ██
    _________________________________________________________________""")

    print("    [1] > New Game <")
    print("    [2] Load Game")
    print("    [3] Settings")
    print("    [4] Quit")

    print("")
    print("SPACEBAR to confirm")

def loadGameSelected():
    print(
    """
    _________________________________________________________________
      ██████    ██████       ██   ███████    ██    ██████    ██   ██  
     ██    ██   ██   ██      ██       ██     ██   ██    ██   ███  ██  
     ██    ██   ██████       ██      ██      ██   ██    ██   ████ ██  
     ██    ██   ██  ██       ██     ██       ██   ██    ██   ██  ███  
      ██████    ██   ██████  ██    ████████  ██    ██████    ██   ██
    _________________________________________________________________""")

    print("    [1] New Game")
    print("    [2] > Load Game <")
    print("    [3] Settings")
    print("    [4] Quit")
    
    print("")
    print("SPACEBAR to confirm")

def settingsSelected():
    print(
    """
    _________________________________________________________________
      ██████    ██████       ██   ███████    ██    ██████    ██   ██  
     ██    ██   ██   ██      ██       ██     ██   ██    ██   ███  ██  
     ██    ██   ██████       ██      ██      ██   ██    ██   ████ ██  
     ██    ██   ██  ██       ██     ██       ██   ██    ██   ██  ███  
      ██████    ██   ██████  ██    ████████  ██    ██████    ██   ██
    _________________________________________________________________""")

    print("    [1] New Game")
    print("    [2] Load Game")
    print("    [3] > Settings <")
    print("    [4] Quit")
    
    print("")
    print("SPACEBAR to confirm")

def quitSelected():
    print(
    """
    _________________________________________________________________
      ██████    ██████       ██   ███████    ██    ██████    ██   ██  
     ██    ██   ██   ██      ██       ██     ██   ██    ██   ███  ██  
     ██    ██   ██████       ██      ██      ██   ██    ██   ████ ██  
     ██    ██   ██  ██       ██     ██       ██   ██    ██   ██  ███  
      ██████    ██   ██████  ██    ████████  ██    ██████    ██   ██
    _________________________________________________________________""")
    print("    [1] New Game")
    print("    [2] Load Game")
    print("    [3] Settings")
    print("    [4] > Quit <")
    
    print("")
    print("SPACEBAR to confirm")

def generalSettingsSelected():
    print("")
    print("[1] General Settings")
    print("[2] Video Settings")
    print("[3] Audio Settings")
    print("")
    print("[4] Save & Exit")
    print("")
    y=input()

def kbfunc():
    x = msvcrt.kbhit()
    if x:
        ret = msvcrt.getch()
    else:
        ret = False
    return ret

menu()

selected = 0
number = 1

while True:
    
    x = kbfunc()
    
    if x != False and x.decode() == '1':
        choice = x.decode()
        selected = 1
        os.system("cls")
        newGameSelected()
    else:
        number += 1
        time.sleep(0.0001)
        
    if x != False and x.decode() == '2':
        choice = x.decode()
        selected = 1
        os.system("cls")
        loadGameSelected()       
    else:
        number += 1
        time.sleep(0.0001)

    if x != False and x.decode() == '3':
        choice = x.decode()
        selected = 1
        os.system("cls")
        settingsSelected()
    else:
        number += 1
        time.sleep(0.0001)

    if x != False and x.decode() == '4':
        choice = x.decode()
        selected = 1
        os.system("cls")
        quitSelected()
    else:
        number += 1
        time.sleep(0.0001)

    if x != False and x.decode() == ' ' and selected == 1:
        if choice == '1':
            print("")
            print("Creating New Game...")
            print("")
            x=input("[Press Enter]")
        elif choice == '2':
            print("")
            print("Loading Save Data...")
            print("")
            x=input("[Press Enter]")
        elif choice == '3':
            print("Delete Save Data?")
            y=input("[Y/N]: ")
        elif choice == '4':
            quit
        break

