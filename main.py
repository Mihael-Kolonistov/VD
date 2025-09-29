from sender import Snd
import json
from mgs import *

chat = Snd('192.168.56.1')

if __name__=="__main__":
    msgT["text"] = "Вы подключены!"
    chat.send(msgT)