from sender import Snd
import json
import threading
import time
import random

wait = 0.5

msgT={
    "type": "text",
    "text": ""
}
msgC={
    "type": "cmd",
    "pos": "hhh",
    "btn": "",
    "clickAt": "", 
    "scroll": ""
}

msgF={
    "type": "file",
    "from": "",
    "to": "",
    "file": ""
}




def ini(ip, port):
    threading.Thread(target=init, daemon=True, kwargs={"ip": ip, "port": port}).start()
        
def init(ip, port):
    global msgC, msgF, msgT
    
    snd = Snd(ip, port)
    while True:
        time.sleep(wait)
        snd.send(msgC)