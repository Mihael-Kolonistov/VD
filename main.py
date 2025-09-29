from sender import Snd
import threading
import time

sender = Snd()


threading.Thread(target=sender.recv, daemon=True).start()
sender.send({'hi': "again"})
