import msvcrt
from pynput import mouse
from initSND import msgC

class main:
    def press(self):  
        
        global pressed          
        char = msvcrt.getch() 
        pressed = char.decode('utf-8')  
        msgC["btn"] = pressed

    def pos(self, x, y):
        msgC["pos"] = (x, y)

    def cl(self, button, pressed):
        msgC["click"] =  True if pressed else False
        
    def __init__(self):
        with mouse.Listener(on_move=self.pos, on_click=self.cl) as ls:
            ls.join()

