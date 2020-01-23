import glob
import time
from datetime import datetime
import sys

base_dir = '/sys/bus/w1/devices/'
slave_path = '/w1_slave'
sleep_time = 1
if len(sys.argv) > 1:
    sleep_time = float(sys.argv[1])


def get_devices():
    device_folder = glob.glob(base_dir + '28*')
    devices = []
    for folder in device_folder:
        devices.append(folder + slave_path)
    return devices


def read_temp_raw(device):
    f = open(device, 'r')
    lines = f.readlines()
    f.close()
    return lines


def read_temp(device):
    lines = read_temp_raw(device)
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return get_device_serial(device), temp_c, str(datetime.now())


def get_device_serial(device):
    return device.replace(base_dir, '').replace(slave_path, '')


while True:
    for device in get_devices():
        print(read_temp(device))
    time.sleep(sleep_time)