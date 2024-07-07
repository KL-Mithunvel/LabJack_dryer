import time
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import threading
from enum import IntEnum
from enum import auto as enum_auto

import Main
import config


class Commands(IntEnum):
    StartCycle = enum_auto()


class MainWindow:
    def __init__(self,guic,cmd:list,live_data):
        self.guic=guic
        self.live_data = None
        self.components= dict()
        self.root = None
        self.command_pipe = cmd
        self.live_data=live_data
    def createtk(self):
        root = tk.Tk()
        root.geometry("800x600")
        root.title('LabJack_dryer')
        root.tk.call("tk", "scaling", 2)

        self.components["l1"] = tk.Label(root, text='LabJack_dryer')
        self.components["l1"] .grid(row=0, column=0)
        self.components["l2"]=(tk.Label(root, text="Test Setup"))
        self.components["l2"].grid(row=1, column=0)
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

class report_window:
    def __init__(self,test_no,command):
        self.root = None
        self.components = dict()
        self.test_no=test_no
        self.cmd=command
        self.live_data = None

    def on_select(self):
        selected_item = self.report_ch.get()
        self.label.config(text="Selected Item: " + selected_item)


    def createtk(self):
        self.root = tk.Tk()
        self.root.geometry("800x600")
        self.root.title('Report')
        self.root.tk.call("tk", "scaling", 2)
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)
        filemenu = tk.Menu(menu)
        menu.add_cascade(label='File', menu=filemenu)
        filemenu.add_command(label='New', command=Main.main)
        filemenu.add_separator()
        filemenu.add_command(label='Exit', command=self.root.quit)
        self.components["l1"] = tk.Label(self.root, text='Report:')
        self.components["l1"].grid(row=0, column=1)
        self.report_ch =ttk.Combobox(self.root, values=self.test_no)
        self.report_ch.set(self.test_no[0])
        self.label = tk.Label(self.root, text="Selected test: ")
        self.label.grid(column=0, row=1)
        self.report_ch.grid(column=2, row=1)
        self.components["plot_button"] = tk.Button(master=self.root,command=self.plt, text="Plot")
        self.components["plot_button"].grid(column=3, row=2)

    def plt(self):
        self.cmd.append("plot")

    def main_loop(self):
        self.createtk()
        self.update()
        self.root.mainloop()


    def update(self):
        self.report_ch.bind(self.on_select())
        if self.live_data:
            self.live_data = None
        self.root.after(1000,self.update)

    def update_data(self, data):
        self.live_data = data


