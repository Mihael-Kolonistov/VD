from sender import Snd

chat = Snd('192.168.56.1')

while True:
    text = input()
    
    chat.send()