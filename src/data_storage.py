import pyodbc
import pymssql

def connect(connection_string):
    conn = pyodbc.connect(connection_string)
    return conn


def connect_pymssql(server, user, password, database):
    conn = pymssql.connect(server, user, password, database)
    return conn


def save_to_sql(connection_string, temperature_reading):
    connection = connect(connection_string)
    cursor = connection.cursor()
    cursor.execute('INSERT INTO temperature.dbo.readings (probe_serial, reading_date, temperature_value) VALUES (%s, %s, %s)', [(temperature_reading.serial, temperature_reading.datetime, temperature_reading.temperature_celcius)])
    cursor.commit()
    connection.close()
    
def save_to_sql_pymssql(server, user, password, database, temperature_reading):
    connection = connect_pymssql(server, user, password, database)
    cursor = connection.cursor()
    cursor.execute('INSERT INTO temperature.dbo.readings (probe_serial, reading_date, temperature_value) VALUES (%s, %s, %s)', (temperature_reading.serial, temperature_reading.datetime, temperature_reading.temperature_celcius))
    connection.commit()
    connection.close()
