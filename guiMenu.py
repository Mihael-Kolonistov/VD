from tkinter import Tk, ttk, LabelFrame, Button, StringVar
import json
import threading

from dialog import Info, Error
class main:
    
    

    def thermeChange(self):
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
        self.thermeInit()

    def thermeInit(self):
        with open('gui/config.json', 'r', encoding='utf-8') as cfg:    
            cfgj = json.loads(cfg.read())
            if cfgj["therme"] == "night":
                self.root["bg"]="#242424"
                self.win["bg"]="#242424"
                self.win["fg"]="#f0f0f0"
                self.actions["bg"]="#242424"
                self.actions["fg"]="#f0f0f0"
                self.prarm["bg"]="#242424"
                self.prarm["fg"]="#f0f0f0"
                self.type["bg"]="#242424"
                self.type["fg"]="#f0f0f0"
                self.ip["bg"]="#242424"
                self.ip["fg"]="#f0f0f0"
                self.port["bg"]="#242424"
                self.port["fg"]="#f0f0f0"

            elif cfgj["therme"] == "day":
                self.root["bg"]="#f0f0f0"
                self.win["bg"]="#f0f0f0"
                self.win["fg"]="#242424"
                self.actions["bg"]="#f0f0f0"
                self.actions["fg"]="#242424"
                self.prarm["fg"]="#242424"
                self.prarm["bg"]="#f0f0f0"
                self.type["fg"]="#242424"
                self.type["bg"]="#f0f0f0"
                self.ip["fg"]="#242424"
                self.ip["bg"]="#f0f0f0"
                self.port["fg"]="#242424"
                self.port["bg"]="#f0f0f0"
                
        self.ipE["values"] = cfgj["ips"]
        self.portE["values"] = cfgj["ports"]


    def __init__(self):
        self.go = False
        self.root = Tk()
        self.root.minsize(width = 310, height=390)

        self.root.geometry("310x390")
        self.root.title("Старотвые настройки")

        for c in range(1): self.root.columnconfigure(index=c, weight=1)
        self.root.rowconfigure(index=0, weight=1)

        self.win=LabelFrame(self.root, text="Старотвые настройки")
        self.win.rowconfigure(index=0, weight=1)
        self.win.columnconfigure(index=0, weight=1)
        #окно инф-ии
        self.prarm=LabelFrame(self.win, text="Параметр")

        self.type=LabelFrame(self.prarm, text="Тип подключения")
        self.ip=LabelFrame(self.prarm, text="ip(обязательно при подключении первым)")
        self.port=LabelFrame(self.prarm, text="Порт подключения")

        self.types = ["Desktop", "User"]#user = sender, desktop = client
        self.typeSt = StringVar()
        self.tps= ttk.Combobox(self.type, values=self.types, textvariable=self.typeSt, state="readonly").grid(sticky="ns", padx=10, pady=5)
        
        
        self.ipSt = StringVar()
        self.ipE = ttk.Combobox(self.ip, values=[], textvariable=self.ipSt)
        self.ipE.grid(sticky="ns", padx=10, pady=5)
        
        self.portSt = StringVar()
        self.portE = ttk.Combobox(self.port, values=[], textvariable=self.portSt)
        self.portE.grid(sticky="ns", padx=10, pady=5)

        #панель снизу, запуск и т.д.
        self.actions = LabelFrame(self.root, text="Инструменты")
        self.actions.rowconfigure(index=0, weight=1)
        self.actions.columnconfigure(index=1, weight=1)

        def req(ip = self.ipE, type = self.typeSt, port = self.portE):
            global go
            ip = ip.get()
            type = type.get()
            port = port.get()
            if ip != "" and port != "" and (type == "Desktop" or type=="User"):
                if not self.go:
                    try:
                        port = int(port)
                        with open('gui/config.json', 'r', encoding='utf-8') as cfg:    
                            cfgj = json.loads(cfg.read())
                            if not port in cfgj["ports"]:
                                cfgj["ports"].append(port)
                            if not ip in cfgj["ips"]:            
                                cfgj["ips"].append(ip)
                        with open('gui/config.json', 'w', encoding='utf-8') as cfg: 
                            json.dump(cfgj, cfg, ensure_ascii=False, indent=4)
                                
                        if type=="Desktop":
                            from initSND import ini
                            from lib import main as ml
                            ml()
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
        self.podkl = Button(self.actions, text="Подключиться", relief='groove', command=req)
        self.therme = Button(self.actions, text="сменить тему", relief='groove', command=self.thermeChange)
        #grid

        self.win.grid(sticky="nswe", padx=5, pady=5 , ipadx=5, ipady=5, column=0, row=0)

        self.prarm.grid(column=0, row=0, padx=5, pady=5, sticky="nswe")
        self.type.grid(column=0, row=0, padx=5, pady=5, sticky="nswe")
        self.port.grid(column=0, row=1, padx=5, pady=5, sticky="nswe")
        self.ip.grid(column=0, row=2,padx=5, pady=5, sticky="nswe")

        self.podkl.grid(column=0, row=0, ipadx=5, padx=5, pady=5)
        self.therme.grid(column=3, row=0, ipadx=5, padx=5, pady=5)
        self.actions.grid(sticky="nswe", padx=5, pady=5 , ipadx=5, ipady=5, column=0, row=1)

        #настройки темы


        self.thermeInit()
        self.root.mainloop()
main()