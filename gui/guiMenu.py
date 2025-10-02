from tkinter import Tk, ttk, LabelFrame

root = Tk()

root.geometry("660x320")
root.title("Старотвые настройки")

for c in range(1): root.columnconfigure(index=c, weight=1)
root.rowconfigure(index=0, weight=1)

win=LabelFrame(root, text="Старотвые настройки")
win.rowconfigure(index=0, weight=1)

actions = LabelFrame(win, text="Инструменты")
actions.rowconfigure(index=0, weight=1)

asRoot = ttk.Button(actions)
asRoot = ttk.Button(actions)

win.grid(sticky="nswe", padx=5, pady=5 , ipadx=5, ipady=5)
actions.grid(sticky="nswe", padx=5, pady=5 , ipadx=5, ipady=5, column=0, row=1)

asRoot.grid(column=0, row=0)

root.mainloop()
