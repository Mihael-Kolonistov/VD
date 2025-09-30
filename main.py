from sender import Snd
import json
from mgs import *
import threading

msgCP, msgFP, msgTP = msgC, msgF, msgT

snd = Snd('192.168.56.1')

def upd():
    while True:        
        global msgF, msgT, msgC, msgCP, msgFP, msgTP
        if json.dumps(msgC)!=json.dumps(msgCP):
            snd.send(msgC)

        if json.dumps(msgF)!=json.dumps(msgFP):
            snd.send(msgF)

        if json.dumps(msgT)!=json.dumps(msgTP):
            snd.send(msgT)

        msgCP, msgFP, msgTP = msgC, msgF, msgT
        print(msgC, msgF, msgT)
        print(msgCP, msgFP, msgTP)




threading.Thread(target=upd).start()

msgT["text"] = "Вы подключены!"
snd.send(msgT)
    