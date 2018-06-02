from tkinter import *
import sys
from PIL import Image, ImageTk
import json
import sys
import os

class Window(object):

    def __init__(self, master):
        self.master = master
        self.master.title("Setup | Suggestion Bot")
        self.master.geometry("1500x600")
        self.master.config(bg="#000")
        self.master.resizable(0, 0)
        self.AddWidgets()

    def AddWidgets(self):
        load = Image.open("banner.png")
        render = ImageTk.PhotoImage(load)
        img = Label(self.master, image=render, bd=0, relief=FLAT)
        img.image = render
        img.place(x=0, y=0)

        self.token = StringVar(self.master, value="ENTER YOUR TOKEN HERE")
        self.EnterToken = Entry(self.master, textvariable=self.token, bd=0, width=100)
        self.EnterToken.place(x=450, y=500)
        self.SubmitToken = Button(self.master, text="SUBMIT TOKEN", width=25, height=2, bd=0, font="Impact", bg="#42f498", fg="#000", command=self.SaveToken)
        self.SubmitToken.place(x=650, y=525)

    def SaveToken(self):
        token = self.token.get()
        with open('settings.json', 'r') as f:
            config = json.load(f)
            config["GLOBAL"]["TOKEN"] = token
            with open('settings.json', 'w') as f:
                json.dump(config, f, indent=2)
        self.SubmitToken.destroy()
        self.EnterToken.destroy()
        self.NoAutoButton = Button(self.master, text="NO AUTORESTART", width=25, height=2, bd=0, font="Impact", bg="#42f498", fg="#000", command=self.noauto)
        self.NoAutoButton.place(x=500, y=525)
        self.AutoButton = Button(self.master, text="AUTORESTART", width=25, height=2, bd=0, font="Impact", bg="#42f498", fg="#000", command=self.auto)
        self.AutoButton.place(x=800, y=525)

    def noauto(self):
        os.remove("setup.py")
        os.remove("setup.bat")
        with open("startbot.bat", "w+") as f:
            f.write("@echo off\n")
            f.write("TITLE Suggestion Bot\n")
            f.write("COLOR F4\n")
            f.write("cls \n")
            f.write("python main.py\n")
            f.write("echo Bot stopped. Press any key to close the cmd prompt!\n")
            f.write("pause >nul\n")
        sys.exit()
        return

    def auto(self):
        os.remove("setup.py")
        os.remove("setup.bat")
        os.remove("banner.png")
        with open("startbot.bat", "w+") as f:
            f.write("TITLE Suggestion Bot\n")
            f.write("COLOR F4\n")
            f.write("cls \n")
            f.write(":begin\n")
            f.write("python main.py\n")
            f.write("cls\n")
            f.write("goto begin\n")
        sys.exit()
        return

app = Tk()
Window = Window(app)
app.mainloop()
