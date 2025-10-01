from recerver import Rec
import threading

def ini():
    rec = Rec()        
        
def start():    
    threading.Thread(target=ini).start()