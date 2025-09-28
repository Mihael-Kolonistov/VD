import pyautogui
posc=()
def pos(): 
    global posc         
    x,y = pyautogui.position()
    posc=(x,y)