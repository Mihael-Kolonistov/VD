import socket
import threading

ip = input("Enter target IP: ")
port = 12345

sock = socket.socket()

try:
    sock.connect((ip, port))
    print("Connected as client")
except:
    sock.close()
    sock = socket.socket()
    sock.bind(('0.0.0.0', port))
    sock.listen()
    print("Waiting for connection...")
    sock, addr = sock.accept()
    print("Connected as server")

def listen():
    while True:
        data = sock.recv(1024).decode()
        print(f"\nReceived: {data}\nYou: ", end='')

threading.Thread(target=listen, daemon=True).start()

while True:
    msg = input("You: ")
    sock.send(msg.encode())