import socket
import threading

ip = '0.0.0.0'
port = 12345

s = socket.socket()
s.bind((ip, port))
s.listen()
conn, addr = s.accept()

def listen():
    while True:
        data = conn.recv(1024).decode()
        print(f"Received: {data}")

threading.Thread(target=listen, daemon=True).start()

def sendText(text):
    print(f"snd: "+text)
    s.send(text.encode())
while True:
    
    sendText(input("text"))