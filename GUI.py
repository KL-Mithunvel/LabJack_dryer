import time
import tkinter as tk
from tkinter import messagebox
import threading
from enum import IntEnum
from enum import auto as enum_auto
import config


class Commands(IntEnum):
    StartCycle = enum_auto()


class MainWindow:
    def __init__(self,guic,cmd:list):
        self.guic=guic
        self.live_data = None
        self.components= dict()
        self.root = None
        self.command_pipe = cmd
    def createtk(self):
        root = tk.Tk()
        root.geometry("800x600")
        root.title('LabJack_dryer')
        root.tk.call("tk", "scaling", 2)

        x = tk.Label(root, text='LabJack_dryer')
        x.grid(row=0, column=0)
        self.components["l1"] = x
        self.components["l2"]=tk.Label(root, text="Test Setup").grid(row=1, column=0)
        self.components["l3"]=tk.Label(root, text="Sno:").grid(row=2, column=0)
        self.components["ltemp"]=tk.Label(root, text="default temp:" )
        self.components["ltemp"].grid(row=3, column=0)
        self.components["lmass"]=tk.Label(root, text="default mass:" ).grid(row=4, column=0)
        self.components["lHome"]=tk.Label(root, text="default home point:").grid(row=5, column=0)
        self.components["sno"] = tk.Entry(root).grid(row=2, column=1)

        # t1 = threading.Thread(target=, args=[guic,root,sno])
        self.components["note"] = tk.Label(root, text=self.guic.note, fg="red")
        self.components["note"].grid(row=7, column=4)
        START = tk.Button(root, text='Start cycle', width=25, command=self.start_cycle).grid(row = 5, column = 5)


        self.root = root


    def main_loop(self):
        self.createtk()
        self.update()
        self.root.mainloop()

    def update(self):
        self.components["note"]["text"]=time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(time.time()))
        if self.live_data:
            self.components["ltemp"]["text"]=self.live_data
            self.live_data = None
        self.root.after(1000,self.update)

    def update_data(self, data):
        self.live_data = data


    def start_cycle(self):
        self.command_pipe.append(Commands.StartCycle)

#GUI


class MessageWindow:
    def __init__(self, msg: str, title="Message"):
        tk.messagebox.showinfo(title, msg)

