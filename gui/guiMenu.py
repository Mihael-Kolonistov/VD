from tkinter import Tk, ttk, LabelFrame
import json

root = Tk()

root.geometry("660x320")
root.title("Старотвые настройки")

for c in range(1): root.columnconfigure(index=c, weight=1)
root.rowconfigure(index=0, weight=1)

win=LabelFrame(root, text="Старотвые настройки")
win.rowconfigure(index=0, weight=1)

actions = LabelFrame(root, text="Инструменты")
actions.rowconfigure(index=0, weight=1)

podkl = ttk.Button(actions)

win.grid(sticky="nswe", padx=5, pady=5 , ipadx=5, ipady=5)
actions.grid(sticky="nswe", padx=5, pady=5 , ipadx=5, ipady=5, column=0, row=1)

podkl.grid(column=0, row=0)

with open("config.json", "r") as cfg:
    cfgj = json.dump(cfg)
    if cfgj["therme"] == "night":
        root["backgroud"]="#242424"
        win["backgroud"]="#242424"
        actions["backgroud"]="#242424"
        podkl["backgroud"]="#242424"
    elif cfgj["therme"] == "day":
        root["backgroud"]="#E0E0E0"
        win["backgroud"]="#E0E0E0"
        actions["backgroud"]="#E0E0E0"
        podkl["backgroud"]="#E0E0E0"
root.mainloop()
