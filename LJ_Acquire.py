from labjack import ljm
import CalcScale
from config import LJ_Config


class LJAq:
    def __init__(self, lj_config: LJ_Config):
        self.handle = None
        self.lj_config = lj_config
        self.error = None
    def open_device(self, deviceType, connType):
        try:
            handle = ljm.openS(deviceType, connType, "ANY")
        except ljm.ljm.LJMError as e:
            self.handle = None
            self.error = e
            return False
        else:
            self.handle = handle
            self.error = None
            return True

    def read_ai_chl(self, chl):
        value = ljm.eReadName(self.handle, chl)
        return value

    def close_device(self):
        ljm.close(self.handle)
        pass

    def write_ai_chl(self, chl, val):
        ljm.eWriteName(self.handle, chl, val)

    def read_once(self):
        # lj_config - > dict containing LJ info
        v1 = self.read_ai_chl(self.lj_config.MM1011_chl_IOA)
        v2 = self.read_ai_chl(self.lj_config.MM1011_chl_IOB)
        v3 = self.read_ai_chl(self.lj_config.RTD_chl_IOA)
        v4 = self.read_ai_chl(self.lj_config.RTD_chl_IOB)
        v5 = self.read_ai_chl(self.lj_config.Load_chl_IOA)
        mm = CalcScale.scale_ai_to_mm_MM1011(v2, self.lj_config.POT_Zero_V, v1)
        temp = CalcScale.rtd_to_temp(v3, v4)
        weight = CalcScale.loadscale_to_kg(v5)
        data = [mm, temp, weight]
        return data
