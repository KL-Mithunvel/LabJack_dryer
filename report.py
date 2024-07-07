import GUI
import config
import sqlDB
import threading
import tkinter as tk
import time


cur, con = sqlDB.get_cursor("sample.db")
past_test = sqlDB.get_testno(cur)
command =[]
report = GUI.report_window(test_no=past_test,command=command)
t1 = threading.Thread(target=report.main_loop, args=[])
t1.start()
while True:
    if len(command):
        c = command.pop()
        if c == "plot":
            print("plot")
    else:
        time.sleep(0.01)
sqlDB.close(con)
