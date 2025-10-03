import socket
import threading
import json

class Snd:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.s = None
        self.tp = None
        self.podkl()

    def podkl(self):
        print("Ожидание подключения...")
        
        self.s = socket.socket()
        self.s.settimeout(None)
        self.s.connect((self.ip, self.port))
        self.tp = "sender"
        print("Подключено!")

    def send(self, msg):
        self.s.send(json.dumps(msg).encode())




