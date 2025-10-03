import msvcrt
from pynput.mouse import Listener
from initSND import msgC
import threading
class main:
    def press(self):  
        
        global pressed          
        char = msvcrt.getch() 
        pressed = char.decode('utf-8')  
        msgC["btn"] = pressed
        print(pressed)

    def pos(self, x, y):
        msgC["pos"] = ((x, y))

    def cl(self, x, y, pressed):
        msgC["click"] =  True if pressed else False
        msgC["clickAt"] = ((x, y))
        if not pressed:
            pass
        
    def sc(self, dy):  
        msgC["scroll"] = dy
    def ini(self):    
        listener = Listener(
            on_move=self.pos,
            on_click=self.cl,
            on_scroll=self.sc)
        listener.start()
            
    def __init__(self):
        threading.Thread(target=self.ini, daemon=True).start()
        
if __name__=="__main__":
    main()  