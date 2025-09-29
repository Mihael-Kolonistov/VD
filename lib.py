import msvcrt
from pynput import mouse
from mgs import msgF, msgT, msgC
class main:
    def press(self):  
        
        global pressed          
        char = msvcrt.getch() 
        pressed = char.decode('utf-8')  
        msgC["key"] = pressed

    def pos(self, x, y):
        msgC["posx"] = x
        msgC["posy"] = y

    def cl(self, button, pressed):
        msgC["click"] =  True if pressed else False
    def __init__(self):
        with mouse.Listener(on_move=self.pos, on_click=self.cl) as ls:
            ls.join()
if __name__=="__main__":
    main.__init__(self = main)
    
