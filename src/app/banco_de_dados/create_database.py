import os
import mysql.connector
from mysql.connector import errorcode
import logging
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

load_dotenv()

MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PORT = int(os.getenv("MYSQL_PORT"))
MYSQL_DB = os.getenv("MYSQL_DB")
MYSQL_PATH_SQL = os.getenv("MYSQL_PATH_SQL")  


config = {
    "host": MYSQL_HOST,
    "user": MYSQL_USER,
    "password": MYSQL_PASSWORD,
    "port": MYSQL_PORT
}

try:
   
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {MYSQL_DB}")
    logging.info(f"Banco de dados `{MYSQL_DB}` criado ou já existente.")
    conn.database = MYSQL_DB

   
    with open(MYSQL_PATH_SQL, "r", encoding="utf-8") as f:
        sql_script = f.read()

   
    for statement in sql_script.strip().split(";"):
        stmt = statement.strip()
        if stmt:
            cursor.execute(stmt + ";")
            logging.info("Executado com sucesso: %s", stmt.splitlines()[0][:60])

    logging.info("Todas as tabelas foram criadas com sucesso.")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        logging.error("Erro de acesso: usuário ou senha inválido.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        logging.error("Banco de dados não existe.")
    else:
        logging.error("Erro: %s", err)
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()