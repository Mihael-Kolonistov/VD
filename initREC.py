from recerver import Rec
import json
import threading

def upd():
    rec = Rec()
    while True: 
        print()
def start():    
    threading.Thread(target=upd).start()