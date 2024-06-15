import LJ_Acquire, LJ_Config
import CalcScale
import sqlDB


def start_daq_run(interval_sec, duration_min, lj_config:LJ_Config.LJ_Config, db_cursor, run_sl):
    # lj_config - > dict containing LJ info
    lj = LJ_Acquire.open_device(lj_config.DevType, lj_config.ConType)
    while lp:
        v = LJ_Acquire.read_ai_chl(lj_config.MM1011_chl)
        mm = CalcScale.scale_ai_to_mm_MM1011(v, lj_config.POT_Zero_V, lj_config.POT_Max_V)
        sqlDB.add_data(db_cursor, run_sl)