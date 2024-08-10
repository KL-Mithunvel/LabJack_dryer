import time
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import threading
from enum import IntEnum
from enum import auto as enum_auto


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


    def on_select(self,label,x):
        selected_item = x.get()
        label.config(text="Selected Item: " + selected_item)


    def createtk(self):
        self.root = tk.Tk()
        self.root.geometry("800x600")
        self.root.title('Report')
        self.root.tk.call("tk", "scaling", 2)
        style = ttk.Style(self.root)
        style.theme_use("clam")



        self.components["l1"] = tk.Label(self.root, text='Report:')
        self.components["l1"].grid(row=0, column=0)
        self.components["l2"] = tk.Label(self.root, text='Test no:')
        self.components["l2"].grid(row=1, column=0)
        self.components["l3"] = tk.Label(self.root, text='plot type:')
        self.components["l3"].grid(row=2, column=0)
        self.report_ch = ttk.Combobox(self.root, values=self.test_no)
        self.report_ch.set(self.test_no[0])
        self.report_ch.grid(column=2, row=1)
        self.plot_ch=["Full plot", "mass vs shrinkage", "mass vs temp" , "temp vs shrinkage"]
        self.plt_ch = ttk.Combobox(self.root, values=self.plot_ch)
        self.plt_ch.set(self.plot_ch[0])
        self.plt_ch.grid(column=2, row=2)
        self.components["l4"] = tk.Label(self.root, text="Selected test: ")
        self.components["l4"].grid(column=1, row=3)
        self.components["l5"] = tk.Label(self.root, text="Selected plot type: ")
        self.components["l5"].grid(column=1, row=4)

        var1 = tk.IntVar()
        var2 = tk.IntVar()
        var3 = tk.IntVar()
        self.components["Mass%"]=tk.Checkbutton(self.root,text="Mass%",variable=var1)
        self.components["Mass%"].grid(column=2, row=5)
        self.components["LS%"] = tk.Checkbutton(self.root, text="LS%", variable=var2)
        self.components["LS%"].grid(column=3, row=5)
        self.components["temp%"] = tk.Checkbutton(self.root, text="temp%", variable=var3)
        self.components["temp%"].grid(column=4, row=5)
        self.components["temp%"]["state"] = "disable"
        self.components["LS%"]["state"] = "disable"
        self.components["Mass%"]["state"] = "disable"
        self.components["plot_button"] = tk.Button(master=self.root, command = self.plt, text="Plot")
        self.components["plot_button"].grid(column=2, row=6)
        self.components["export to csv"] = tk.Button(master=self.root, command= self.csv_export, text="export to csv")
        self.components["export to csv"].grid(column=3, row=6)


    def persent_op(self, E):
        ch = self.plt_ch.get()
        if ch == "Full plot":
            pass
        elif ch == "mass vs shrinkage":
            self.components["Mass%"]["state"] = "normal"
            self.components["LS%"]["state"] = "normal"
            self.components["temp%"]["state"] = "disable"
        elif ch == "mass vs temp":
            self.components["Mass%"]["state"] = "normal"
            self.components["temp%"]["state"] = "normal"
            self.components["LS%"]["state"] = "disable"
        elif ch == "temp vs shrinkage":
            self.components["Mass%"]["state"] = "disable"
            self.components["LS%"]["state"] = "normal"
            self.components["temp%"]["state"] = "normal"

    def MassVsShrinkage(self):
        pass
    def plt(self):
        self.cmd.append("plot")

    def csv_export(self):
        self.cmd.append("csv")

    def main_loop(self):
        self.createtk()
        self.update()
        self.root.mainloop()

    def option_selected(self, component_name: str, set_state: str):
        comp = self.components.get(component_name, None)
        if isinstance(comp, tk.Checkbutton):
            comp["state"] = set_state

    def update(self):
        self.on_select(self.components["l4"], self.report_ch)
        self.on_select(self.components["l5"], self.plt_ch)



        self.plt_ch.bind("<<ComboboxSelected>>", self.persent_op)
        self.persent_op(self.plot_ch)
        if self.live_data:
            self.live_data = None
        self.root.after(1000,self.update)

    def update_data(self, data):
        self.live_data = data


