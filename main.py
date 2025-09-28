import threading
import lib
from sender import send as sendS, tp as tpS
import json
msg={        
        "from": "",
        "content": {
            "text": ""
        },
        "command":{
            "posx": 0,
            "posy": 0,
            "click": False,
            "key": ""
        }
    }
def updateMsg():
    global msg  
    msg["content"]["text"] = ""
    msg["from"] = tpS
    x,y = lib.posc
    msg["command"]["posx"] = x
    msg["command"]["posy"] = y
    msg["command"]["key"] = lib.pressed
    msg["content"]["text"]="gg!"
    
    

def send(msg=msg): 
    sendS(json.dumps(msg))
if __name__=="__main__":
    send()
    
