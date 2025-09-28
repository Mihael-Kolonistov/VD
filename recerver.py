import socket
import threading

#ip = '127.0.0.1'
ip = '168.0.0.1'
port = 12345

s = socket.socket()
s.connect((ip, port))

def listen():
    
    while True:
        data = s.recv(1024).decode()
        print(f"Received: {data}")

threading.Thread(target=listen, daemon=True).start()

def sendText(text):
    print(f"snd: "+text)
    s.send(text.encode())
while True:    
    sendText(input("text"))