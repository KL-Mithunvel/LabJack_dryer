import time

import DAQ_Run
import GUI
import LJ_Acquire
import config
import plot
import sqlDB
import tkinter as tk
import threading


#set up
ljc = config.LJ_Config()
# read config from config.ini to ljc
lj: LJ_Acquire = LJ_Acquire.LJAq(ljc)
if not lj.open_device(ljc.DevType, ljc.ConType):
    GUI.MessageWindow("unable to open LJ."+str(lj.error))
    exit(1)
guic = config.config()
command = []
main_w = GUI.MainWindow(guic=guic, cmd=command)
t1 = threading.Thread(target=main_w.main_loop, args=[])
t1.start()
while True:
    if len(command):
        c = command.pop()
        if c == GUI.Commands.StartCycle:
            print("Start Cycle Requested")
    else:
        time.sleep(0.01)

main_w.update_data(x)
#db ,con = sqlDB.get_cursor("sample.db")
#run_sl = sqlDB.test_testno(con, sno)



#
# DAQ_Run.start_daq_run(1, 0.5, ljc, db,con , run_sl)
# LJ_Acquire.close_device(lj)
# data = sqlDB.get_data(db, run_sl)
# sqlDB.flush(con)
# sqlDB.close(db)

#plot.plotGraph(data)

