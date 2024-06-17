import CalcScale
from labjack import ljm


def open_device(deviceType, connType):
    try:
        handle = ljm.openS(deviceType, connType, "ANY")
    except ljm.ljm.LJMError:
        return None
    else:
        return handle


def read_ai_chl(handle, chl):
    value = ljm.eReadName(handle, chl)
    return value


def close_device(handle):
    ljm.close(handle)
    pass
