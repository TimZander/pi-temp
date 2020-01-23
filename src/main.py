from devices import get_devices
from temperature_read import read_temp
import sys
import time

base_dir = '/sys/bus/w1/devices/'
slave_path = '/w1_slave'
matching_string = '28*'
sleep_time = 1
if len(sys.argv) > 1:
    sleep_time = float(sys.argv[1])

print("Starting pi-temp with interval of " + sleep_time)
initial_devices = get_devices(base_dir, slave_path, matching_string)
print("Reading from " + len(initial_devices) + " devices:")
for device in initial_devices:
    print(device)

while True:
    for device in get_devices(base_dir, slave_path, matching_string):
        print(read_temp(device))
    time.sleep(sleep_time)
