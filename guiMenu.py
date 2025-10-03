from tkinter import Tk, ttk, LabelFrame, Button, StringVar
import json
import threading

from dialog import Info, Error

go = False

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
            win["fg"]="#f0f0f0"
            actions["bg"]="#242424"
            actions["fg"]="#f0f0f0"
            prarm["bg"]="#242424"
            prarm["fg"]="#f0f0f0"
            type["bg"]="#242424"
            type["fg"]="#f0f0f0"
            ip["bg"]="#242424"
            ip["fg"]="#f0f0f0"
            port["bg"]="#242424"
            port["fg"]="#f0f0f0"
            
        elif cfgj["therme"] == "day":
            root["bg"]="#f0f0f0"
            win["bg"]="#f0f0f0"
            win["fg"]="#242424"
            actions["bg"]="#f0f0f0"
            actions["fg"]="#242424"
            prarm["fg"]="#242424"
            prarm["bg"]="#f0f0f0"
            type["fg"]="#242424"
            type["bg"]="#f0f0f0"
            ip["fg"]="#242424"
            ip["bg"]="#f0f0f0"
            port["fg"]="#242424"
            port["bg"]="#f0f0f0"


    
root = Tk()
root.minsize(width = 310, height=390)

root.geometry("310x390")
root.title("Старотвые настройки")

for c in range(1): root.columnconfigure(index=c, weight=1)
root.rowconfigure(index=0, weight=1)

win=LabelFrame(root, text="Старотвые настройки")
win.rowconfigure(index=0, weight=1)
win.columnconfigure(index=0, weight=1)
#окно инф-ии
prarm=LabelFrame(win, text="Параметр")

type=LabelFrame(prarm, text="Тип подключения")
ip=LabelFrame(prarm, text="ip(обязательно при подключении первым)")
port=LabelFrame(prarm, text="Порт подключения")

types = ["Desktop", "User"]#user = sender, desktop = client
typeSt = StringVar()
tps= ttk.Combobox(type, values=types, textvariable=typeSt).grid(sticky="ns", padx=10, pady=5)

ipE = ttk.Entry(ip)
ipE.grid(sticky="ns", padx=10, pady=5)
portE = ttk.Entry(port)
portE.grid(sticky="ns", padx=10, pady=5)

#панель снизу, запуск и т.д.
actions = LabelFrame(root, text="Инструменты")
actions.rowconfigure(index=0, weight=1)
actions.columnconfigure(index=1, weight=1)

def req(ip = ipE, type = typeSt, port = portE):
    global go
    ip = ipE.get()
    type = typeSt.get()
    port = portE.get()
    if ip != "" and port != "" and (type == "Desktop" or type=="User"):
        if not go:
            try:
                port = int(port)
                if type=="Desktop":
                    from initSND import ini
                    from lib import main
                    main()
                    threading.Thread(target=ini, kwargs={"ip": ip, "port": port}, daemon= True).start()
                elif type=="User":
                    from initREC import ini
                    threading.Thread(target=ini, kwargs={"ip": ip, "port": port}, daemon= True).start()
                go = True
            except Exception as e:
                threading.Thread(target=Error, kwargs={"text": "Порт должен быть числом"}, daemon= True).start()
                print(e)
        else:
            threading.Thread(target=Info, kwargs={"text": "Вы уже подключены. Для перезапуска закройте приложение и запустите заново."}, daemon= True).start()
    else:
        threading.Thread(target=Error, kwargs={"text": "Вы ввлели неверные параметры, пожалуйста, проверьте их и попробуйте снова!"}, daemon= True).start()
podkl = Button(actions, text="Подключиться", relief='groove', command=req)
therme = Button(actions, text="сменить тему", relief='groove', command=thermeChange)
#grid

win.grid(sticky="nswe", padx=5, pady=5 , ipadx=5, ipady=5, column=0, row=0)

prarm.grid(column=0, row=0, padx=5, pady=5, sticky="nswe")
type.grid(column=0, row=0, padx=5, pady=5, sticky="nswe")
port.grid(column=0, row=1, padx=5, pady=5, sticky="nswe")
ip.grid(column=0, row=2,padx=5, pady=5, sticky="nswe")

podkl.grid(column=0, row=0, ipadx=5, padx=5, pady=5)
therme.grid(column=3, row=0, ipadx=5, padx=5, pady=5)
actions.grid(sticky="nswe", padx=5, pady=5 , ipadx=5, ipady=5, column=0, row=1)

#настройки темы


thermeInit()
root.mainloop()
