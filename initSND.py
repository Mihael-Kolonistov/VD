from sender import Snd
import json

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
    "click": "False"
}

msgF={
    "type": "file",
    "from": "",
    "to": "",
    "file": ""
}



def ini(ip, port):
    global msgC, msgF, msgT
    
    snd = Snd(ip, port)
    while True:
        msgC["type"]=random.randint(0,1000)
        time.sleep(wait)
        snd.send(msgC)