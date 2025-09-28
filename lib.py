import pyautogui
import msvcrt
import threading
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
    
def press():  
    global pressed          
    char = msvcrt.getch() 
    pressed = char.decode('utf-8')  
    
    pressed = ""
    