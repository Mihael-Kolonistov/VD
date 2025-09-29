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
        try:
            self.s = socket.socket()
            self.s.connect((self.ip, self.port))
            self.tp = "client"
        except:
            self.s.close()
            self.s = socket.socket()
            self.s.bind(('0.0.0.0', self.port))
            self.tp = "server"
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

    def send(self, msg):
        self.s.send(str(msg).encode())