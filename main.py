import threading
import lib

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

def sendCur(pos = lib.posc, msg=msg):    
    import sender
    msg["content"]["text"] = ""
    msg["from"] = sender.tp
    x,y = lib.posc
    msg["command"]["posx"] = x
    msg["command"]["posy"] = y
    msg = json.dumps(msg)
    sender.send(msg)

threading.Thread(target=lib.pos, daemon=True).start()
sendCur()