import socket
import threading
import json

ip = '127.0.0.1'
port = 12345

s = socket.socket()

try:
    s.connect((ip, port))
    tp = "client"
except:
    s.close()
    s = socket.socket()
    s.bind(('0.0.0.0', port))
    tp = "server"
    s.listen()
    s, _ = s.accept()

def recv():
    while True:
        try:
            msg = s.recv(1024).decode()
            msg = json.loads(msg)
            
            with open('message.json', 'w', encoding='utf-8') as file:
                json.dump(msg, file, ensure_ascii=False, indent=4)    
                pass               
            
        except Exception as e:
            print(e)            
            pass

threading.Thread(target=recv, daemon=True).start()

def send(msg):
    s.send(msg.encode())
while True:
    msg={
        "type": "",
        "from": "",
        "content": {
            "text": ""
        }
    }
    msg["content"]["text"] = input("You: ")
    msg["from"] = tp
    msg = json.dumps(msg)
    send(msg)
    