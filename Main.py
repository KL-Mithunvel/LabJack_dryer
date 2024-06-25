import DAQ_Run
import LJ_Acquire, LJ_Config
import plot
import sqlDB


run=False
ljc = LJ_Config.LJ_Config()
# read config from config.ini to ljc
lj = LJ_Acquire.open_device(ljc.DevType, ljc.ConType)
db ,con = sqlDB.get_cursor("sample.db")
run_sl = input("Enter Sl No. of Test:")
run=True
DAQ_Run.start_daq_run(1, 0.5, ljc, db, run_sl)
LJ_Acquire.close_device(lj)
data = sqlDB.get_data(db, run_sl,con)
print(data)
sqlDB.close(db)
run=False
plot.plotGraph(data)
