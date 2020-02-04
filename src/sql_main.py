#from devices import get_devices
#from temperature_read import read_temp
from temperature_read import TemperatureReading
import sys
import time
from datetime import datetime
import getopt
from data_storage import save_to_sql

def main(argv):
    connection_string = ""

    try:
        opts, args = getopt.getopt(argv,"hc:",["connection_string="])
    except getopt.GetoptError:
        print('sql_main.py -c <connection_string>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('sql_main.py -c <connection_string>')
            sys.exit()
        elif opt in ("-c", "--connection_string"):
            connection_string = arg
    while True:
        save_to_sql(connection_string, TemperatureReading("TEST_SERIAL", 123, datetime.now()))



if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except KeyboardInterrupt:
        pass
