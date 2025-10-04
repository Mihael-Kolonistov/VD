import pyautogui as pg
import plyer
import threading
class mainn:
    def do(self, mgs):
        match mgs["type"]:
            case "text":                    
                plyer.notification.notify(message=mgs["text"], app_name='VDS', title='Получено текстовое сообщение:', )
            case "cmd":                                  
                x, y = mgs["pos"][0], mgs["pos"][1]
                print(x, y)
                pg.moveTo(x, y)
                if mgs["clickAt"]!="":
                    pg.click()
                if mgs["scroll"]!="":
                    pg.scroll(int(mgs["scroll"]))                
        
    def __init__(self, mgs):
        threading.Thread(target=self.do, kwargs={"mgs": mgs}, daemon=True).start()
        
if __name__=="__main__":
    mainn({"type": "cmd", "pos": [500, 500], "clickAt": "fg", "scroll": -500})
                    
                
 