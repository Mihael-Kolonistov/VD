import socket
import threading

ip = '127.0.0.1'
port = 12345

s = socket.socket()

try:
    s.connect((ip, port))
except:
    s.close()
    s = socket.socket()
    s.bind(('0.0.0.0', port))
    s.listen()
    s, _ = s.accept()

def recv():
    while True:
        try:
            msg = s.recv(1024).decode()
            return msg
        except:
            break

threading.Thread(target=recv, daemon=True).start()

while True:
    msg = input("You: ")
    s.send(msg.encode())