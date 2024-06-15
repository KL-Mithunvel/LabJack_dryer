import DAQ_Run
import LJ_Acquire, LJ_Config
import plot
import sqlDB



ljc = LJ_Config.LJ_Config()
# read config from config.ini to ljc
lj = LJ_Acquire.open_device(ljc.DevType, ljc.ConType)
db = sqlDB.get_cursor("sample.db")
run_sl = int(input("Enter Sl No. of Test:"))
DAQ_Run.start_daq_run(1,10,ljc,db, run_sl)
data = sqlDB.get_data(db, run_sl)
plot.plotGraph(data)
