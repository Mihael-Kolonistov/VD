from tkinter import Tk, ttk, LabelFrame, Button
import json

def thermeChange():
    with open('gui/config.json', 'r', encoding='utf-8') as cfg:    
        cfgj = json.loads(cfg.read())
        if cfgj["therme"] == "night":
            cfgj["therme"] = "day"
            
        elif cfgj["therme"] == "day":
            cfgj["therme"] = "night"
            
        else:
            cfgj["therme"] = "night"
    with open('gui/config.json', 'w', encoding='utf-8') as cfg:    
        json.dump(cfgj, cfg, ensure_ascii=False, indent=4)
    thermeInit()
def thermeInit():
    with open('gui/config.json', 'r', encoding='utf-8') as cfg:    
        cfgj = json.loads(cfg.read())
        if cfgj["therme"] == "night":
            root["bg"]="#242424"
            win["bg"]="#242424"
            win["fg"]="#E0E0E0"
            actions["bg"]="#242424"
            actions["fg"]="#E0E0E0"
            prarm["bg"]="#242424"
            prarm["fg"]="#E0E0E0"
            
        elif cfgj["therme"] == "day":
            root["bg"]="#E0E0E0"
            win["bg"]="#E0E0E0"
            win["fg"]="#242424"
            actions["bg"]="#E0E0E0"
            actions["fg"]="#242424"
            prarm["fg"]="#242424"
            prarm["bg"]="#E0E0E0"
    
root = Tk()

root.geometry("660x320")
root.title("Старотвые настройки")

for c in range(1): root.columnconfigure(index=c, weight=1)
root.rowconfigure(index=0, weight=1)

win=LabelFrame(root, text="Старотвые настройки")
win.rowconfigure(index=0, weight=1)
win.columnconfigure(index=0, weight=1)
win.columnconfigure(index=1, weight=1)
#окно инф-ии
prarm=LabelFrame(win, text="Параметр")

#панель снизу, запуск и т.д.
actions = LabelFrame(root, text="Инструменты")
actions.rowconfigure(index=0, weight=1)
actions.columnconfigure(index=1, weight=1)

podkl = Button(actions, text="Подключиться", relief='groove')
therme = Button(actions, text="сменить тему", relief='groove', command=thermeChange)

#grid

win.grid(sticky="nswe", padx=5, pady=5 , ipadx=5, ipady=5)

prarm.grid(column=0, row=0, ipadx=5, padx=5, pady=5, sticky="nswe")

podkl.grid(column=0, row=0, ipadx=5, padx=5, pady=5)
therme.grid(column=3, row=0, ipadx=5, padx=5, pady=5)
actions.grid(sticky="nswe", padx=5, pady=5 , ipadx=5, ipady=5, column=0, row=1)

#настройки темы
thermeInit()
root.mainloop()
