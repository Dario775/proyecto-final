import pymysql

def connection():
    conn = pymysql.connect(
        host="localhost", port=3306, user="root",
        password="", db="basedatos"
    )
    print('Base de Datos Conectada')
    return conn