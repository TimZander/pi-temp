#from devices import get_devices
#from temperature_read import read_temp
from temperature_read import TemperatureReading
import sys
import time
from datetime import datetime
import getopt
from data_storage import save_to_sql_pymssql

def main(argv):
    server = ""
    user = ""
    password = ""
    database = ""

    try:
        opts, args = getopt.getopt(argv,"hs:u:p:d:",["server="])
    except getopt.GetoptError:
        print('sql_main.py -c <server>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('sql_main.py -c <server>')
            sys.exit()
        elif opt in ("-s", "--server"):
            server = arg
        elif opt in ("-u", "--user"):
            user = arg
        elif opt in ("-p", "--password"):
            password = arg
        elif opt in ("-d", "--database"):
            database = arg
    while True:
        save_to_sql_pymssql(server, user, password, database, TemperatureReading("TEST_SERIAL", 123, datetime.now()))


if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except KeyboardInterrupt:
        pass
