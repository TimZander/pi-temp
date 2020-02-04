import pymssql

def connect(server, user, password, database):
    conn = pymssql.connect(server, user, password, database)
    return conn

    
def save_to_sql(server, user, password, database, temperature_reading):
    connection = connect(server, user, password, database)
    cursor = connection.cursor()
    cursor.execute('INSERT INTO temperature.dbo.readings (probe_serial, reading_date, temperature_value) VALUES (%s, %s, %s)', (temperature_reading.serial, temperature_reading.datetime, temperature_reading.temperature_celcius))
    connection.commit()
    connection.close()
