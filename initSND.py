from sender import Snd
import json
import threading
import time

wait = 0.5

msgT={
    "type": "text",
    "text": ""
}
msgC={
    "type": "cmd",
    "pos": "",
    "btn": "",
    "click": "False"
}

msgF={
    "type": "file",
    "from": "",
    "to": "",
    "file": ""
}



def upd():
    snd = Snd()
    while True:
        time.sleep(wait)
        
        
        
def send():    
    threading.Thread(target=upd).start()