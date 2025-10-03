import socket
import threading
import json

class Rec:
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
        
        self.s.bind(("", self.port))
        self.tp = "recv"
        self.s.listen()
        self.s, _ = self.s.accept()
        print("Подключено!")
        threading.Thread(target=self.recv, daemon=True).start()

    def recv(self):
        while True:
            try:
                msg = self.s.recv(1024).decode()
                msg = json.loads(msg)
                with open('message.json', 'w', encoding='utf-8') as file:
                    json.dump(msg, file, ensure_ascii=False, indent=4)
            except Exception as e:
                print(str(e))