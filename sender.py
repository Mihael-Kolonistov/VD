import socket
import json
from dialog import Info, Error
class Snd:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.s = None
        self.tp = None
        try:            
            self.podkl()
        except:
            Error("Ошибка подключения")

    def podkl(self):
        Info("Ожидание подключения...")
                
        self.s = socket.socket()
        self.s.settimeout(None)
        self.s.connect((self.ip, self.port))
        self.tp = "sender"
        Info("Подключено!")

    def send(self, msg):
        self.s.send(json.dumps(msg).encode())




