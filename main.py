from sender import Snd
import json

chat = Snd('192.168.56.1')

msgF ={   
    "type": "file",     
    "from": "",
    "content": {
        "text": ""
    },
    
}

msgT ={    
    "type": "text",       
    "text": ""    
}

msgC ={   
    "type": "command",  

    "posx": 0,
    "posy": 0,
    "click": False,
    "key": ""
    
}

def init():
    
    while True:
        text = input()

        msgT["content"]["text"] = text

        chat.send(msgT)
if __name__=="__main__":
    msgT["content"]["text"] = "Вы подключены!"