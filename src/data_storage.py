import pyodbc

def connect(connection_string):
    conn = pyodbc.connect(connection_string)
    return conn
    