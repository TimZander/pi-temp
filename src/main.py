from devices import get_devices
from temperature_read import read_temp
import sys
import time
import getopt
from data_storage import save_to_sql

def main(argv):
    base_dir = '/sys/bus/w1/devices/'
    slave_path = '/w1_slave'
    matching_string = '28*'
    sleep_time = 1
    connection_string = ""

    try:
        opts, args = getopt.getopt(argv,"hi:b:c:",["interval=","base_dir=","connection_string="])
    except getopt.GetoptError:
        print('main.py -i <interval> -c <connection_string> -b <base_dir>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('main.py -i <interval> -c <connection_string> -b <base_dir>')
            sys.exit()
        elif opt in ("-i", "--interval"):
            sleep_time = float(arg)
        elif opt in ("-b", "--base_dir"):
            base_dir = arg
        elif opt in ("-c", "--connection_string"):
            connection_string = arg
    print("Starting pi-temp with interval of " + str(sleep_time) + " seconds")
    initial_devices = get_devices(base_dir, slave_path, matching_string)
    print("Reading from " + str(len(initial_devices)) + " devices:")
    for device in initial_devices:
        print(device)
    while True:
        for device in get_devices(base_dir, slave_path, matching_string):
            temperature_reading = read_temp(device)
            print(temperature_reading)
            # upload to database
            save_to_sql(connection_string, temperature_reading)
        time.sleep(sleep_time)


if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except KeyboardInterrupt:
        pass
