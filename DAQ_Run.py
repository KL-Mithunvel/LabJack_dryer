import time
import LJ_Acquire, config
import CalcScale
import sqlDB


def start_daq_run(interval_sec, duration_min, lj_config:config.LJ_Config, db_cursor, db_con, run_sl):
    # lj_config - > dict containing LJ info
    lj = LJ_Acquire.open_device(lj_config.DevType, lj_config.ConType)
    t_end = time.time() + 60 * duration_min
    c = 0
    while time.time() < t_end:
        data = [c,].append(LJ_Acquire.read_once(lj_config, lj))
        temp = data [2]

        if temp <=40:
            LJ_Acquire.write_ai_chl(lj,"DAC0",3.3)
        else:
            LJ_Acquire.write_ai_chl(lj, "DAC0", 0)
        sqlDB.add_data(db_cursor, run_sl, data, db_con)
        time.sleep(interval_sec)
        c += interval_sec


