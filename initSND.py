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



def ini():
    global msgC, msgF, msgT
    
    snd = Snd()
    while True:
        time.sleep(wait)
        snd.send(msgC)
        
        
        
def send():    
    threading.Thread(target=ini, daemon=True).start()