from flask import Flask
from psycopg2 import connect

#conectar base de datos
app = Flask(__name__)

#Definir valores para la conexion

host = "localhost"
port = 5432
dbname = "mi_tienda"
username = "postgres"
password = "admin"

#construir la cadenas para la conexion

def get_connection():
    conn = connect(host=host,port=port,dbname=dbname,user=username,password=password)
    return conn

#get simple
@app.get("/")
def home():
         #probando una cadena de conexion
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT version()")
    print(cursor.fetchall())
    return "prueba de base de datos exitosa"    

#Habilitar Debug
if __name__ == "__main__":
    app.run(debug=True)


