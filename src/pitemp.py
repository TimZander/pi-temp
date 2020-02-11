from devices import get_devices
from temperature_read import read_temp
import sys
import time
import getopt
from data_storage import save_to_sql
from datetime import datetime
import os
import syslog

def main(argv):
    base_dir = '/sys/bus/w1/devices/'
    slave_path = '/w1_slave'
    matching_string = '28*'
    sleep_time = 1
    server = os.getenv('PITEMP_SQLSERVER')
    user = os.getenv('PITEMP_SQLUSER')
    password = os.getenv('PITEMP_SQLPASSWORD')
    database = os.getenv('PITEMP_SQLDB')
    debug = False

    try:
        opts, args = getopt.getopt(argv,"hi:b:s:u:p:d:D",["interval=","base_dir=","server="])
    except getopt.GetoptError:
        print('main.py -i <interval> -s <server> -b <base_dir>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('main.py -i <interval> -s <server> -b <base_dir>')
            sys.exit()
        elif opt in ("-i", "--interval"):
            sleep_time = float(arg)
        elif opt in ("-b", "--base_dir"):
            base_dir = arg
        elif opt in ("-s", "--server"):
            server = arg
        elif opt in ("-u", "--user"):
            user = arg
        elif opt in ("-p", "--password"):
            password = arg
        elif opt in ("-d", "--database"):
            database = arg
        elif opt in ("-D", "--debug"):
            debug = True

    syslog.syslog("Starting pi-temp with interval of " + str(sleep_time) + " seconds")
    initial_devices = get_devices(base_dir, slave_path, matching_string)
    syslog.syslog("Reading from " + str(len(initial_devices)) + " devices:")
    for device in initial_devices:
        syslog.syslog(device.serial)
    while True:
        start_time = datetime.now()
        current_devices = get_devices(base_dir, slave_path, matching_string)
        if current_devices != initial_devices:
            initial_devices = current_devices
            syslog.syslog("devices changed, new devices:")
            for device in current_devices:
                syslog.syslog(device.serial)
            

        for device in current_devices:
            try:
                temperature_reading = read_temp(device)
                syslog.syslog('{0}: {1}'.format(temperature_reading.serial, temperature_reading.temperature_celcius))
                # upload to database
                save_to_sql(server, user, password, database, temperature_reading)
            except:
                pass
            
        true_sleep = sleep_time - (datetime.now() - start_time).total_seconds()
        if true_sleep < 0:
            true_sleep = 0

        time.sleep(true_sleep)


if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except KeyboardInterrupt:
        pass
