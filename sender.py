import socket
import threading
import json

class Snd:
    def __init__(self, ip='192.168.56.1', port=12345):
        self.ip = ip
        self.port = port
        self.s = None
        self.tp = None
        self.podkl()

    def podkl(self):
        print("Ожидание подключения...")
        
        self.s = socket.socket()
        self.s.connect((self.ip, self.port))
        self.tp = "sender"
        print("Подключено!")
        threading.Thread(target=self.recv, daemon=True).start()

    def send(self, msg):
        self.s.send(json.dumps(msg).encode())




