import os
import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

load_dotenv()

POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_PATH_SQL = os.getenv("POSTGRES_PATH_SQL")


conn = psycopg2.connect(
    dbname="postgres",  
    user=POSTGRES_USER,
    password=POSTGRES_PASSWORD,
    host=POSTGRES_HOST,
    port=POSTGRES_PORT
)
conn.autocommit = True
cur = conn.cursor()


try:
    cur.execute(sql.SQL("SELECT 1 FROM pg_database WHERE datname = %s"), [POSTGRES_DB])
    exists = cur.fetchone()
    if not exists:
        cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(POSTGRES_DB)))
        logging.info(f"Banco de dados `{POSTGRES_DB}` criado.")
    else:
        logging.info(f"Banco de dados `{POSTGRES_DB}` já existe.")
except Exception as e:
    logging.error(f"Erro ao criar banco: {e}")
finally:
    cur.close()
    conn.close()


conn = psycopg2.connect(
    dbname=POSTGRES_DB,
    user=POSTGRES_USER,
    password=POSTGRES_PASSWORD,
    host=POSTGRES_HOST,
    port=POSTGRES_PORT
)
cur = conn.cursor()


try:
    with open(POSTGRES_PATH_SQL, "r", encoding="utf-8") as f:
        sql_script = f.read()

    for statement in sql_script.strip().split(";"):
        stmt = statement.strip()
        if stmt:
            cur.execute(stmt + ";")
            logging.info("Executado com sucesso: %s", stmt.splitlines()[0][:60])
    conn.commit()
    logging.info("Todas as tabelas foram criadas com sucesso.")
except Exception as e:
    logging.error(f"Erro ao executar script SQL: {e}")
    conn.rollback()
finally:
    cur.close()
    conn.close()