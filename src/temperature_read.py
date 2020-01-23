from datetime import datetime
import time

def read_temp_raw(device_path):
    f = open(device_path, 'r')
    lines = f.readlines()
    f.close()
    return lines


def read_temp(device):
    lines = read_temp_raw(device.path)
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        # temp_f = temp_c * 9.0 / 5.0 + 32.0
        return device.serial, temp_c, str(datetime.now())
