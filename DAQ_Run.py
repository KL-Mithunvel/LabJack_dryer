import threading
import time

import LJ_Acquire, LJ_Config
import CalcScale
import Live_data
import sqlDB


def start_daq_run(interval_sec, duration_min, lj_config:LJ_Config.LJ_Config, db_cursor, run_sl):
    # lj_config - > dict containing LJ info
    lj = LJ_Acquire.open_device(lj_config.DevType, lj_config.ConType)
    t_end = time.time() + 60 * duration_min
    c = 0
    while time.time() < t_end:
        v1 = LJ_Acquire.read_ai_chl(lj, lj_config.MM1011_chl_IOA)
        v2 = LJ_Acquire.read_ai_chl(lj, lj_config.MM1011_chl_IOB)
        v3 = LJ_Acquire.read_ai_chl(lj, lj_config.MM1011_chl_IOB)
        v4 = LJ_Acquire.read_ai_chl(lj, lj_config.MM1011_chl_IOB)
        mm = CalcScale.scale_ai_to_mm_MM1011(v2, lj_config.POT_Zero_V, v1)
        temp = CalcScale.rtd_to_temp(v3, v4)
        weight = CalcScale.loadscale_to_kg(1, 0)
        sqlDB.add_data(db_cursor, run_sl, [c, mm, temp, weight])
        time.sleep(interval_sec)
        c += interval_sec