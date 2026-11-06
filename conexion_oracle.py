import oracledb
from dotenv import load_dotenv
import os

load_dotenv()

def get_db_connection():
    connection = oracledb.connect(
        user=os.getenv("DB_USER"),
        password= os.getenv("DB_PASSWORD"),
        dsn=os.getenv("DB_DSN")
    )
    return connection


def query_to_dict(sql, params=None):
    """ Ejecuta una consulta SQL y devuelve los resultados como una lista de diccionarios"""
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute(sql, params or [])
             # mapea las columnas a minusculas y construye el diccionario
            columns = [col[0].lower() for col in cursor.description]
            results = [dict(zip(columns, row)) for row in cursor]
            return results
    except Exception as ex:
        print(ex)
    finally:
        connection.close()
        print("Conexion finalizada")