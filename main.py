from sender import Snd
import json

chat = Snd('192.168.56.1')

msg = json.load(open("message.json", "r", encoding="utf-8"))
while True:
    text = input()
    
    msg["content"]["text"] = text
    
    chat.send(msg)