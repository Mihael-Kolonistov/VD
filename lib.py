import pyautogui
import msvcrt
import threading
import main
posc=()
poscBefore=()
click = False
pressed=""
def pos(): 
    global posc, poscBefore      
    if posc != poscBefore and posc != ():   
        x,y = pyautogui.position()
        poscBefore = posc
        posc=(x,y)
        main.send()
    
def press():  
    global pressed          
    char = msvcrt.getch() 
    pressed = char.decode('utf-8')
    main.updateMsg()
    main.send()
    pressed = ""
    main.updateMsg()
    main.send()
    
    
    
threading.Thread(target=pos, daemon=True).start()
threading.Thread(target=press, daemon=True).start()