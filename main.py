import threading
import lib
import sender
import json
msg={        
        "from": "",
        "content": {
            "text": ""
        },
        "command":{
            "pos": "",
            "click": False,
            "key": ""
        }
    }

def sendCur(pos = lib.posc, msg=msg):
    
    
    msg["content"]["text"] = ""
    msg["from"] = sender.main.tp
    msg["command"]["pos"] = lib.posc
    msg = json.dumps(msg)
    sender.send(msg)

threading.Thread(target=lib.pos, daemon=True).start()
sendCur()