from recerver import Rec
import json
import threading
import time

wait = 0.5



def upd():
    rec = Rec()
    while True:
        time.sleep(wait)
        
def start():    
    threading.Thread(target=upd).start()