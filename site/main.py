from fastapi import FastAPI
import psycopg2
import os

app = FastAPI()

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

@app.get("/")
def read_root():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        cur = conn.cursor()
        cur.execute("SELECT version();")
        db_version = cur.fetchone()
        cur.close()
        conn.close()
        return {"message": f"Connected to PostgreSQL {db_version[0]}"}
    except Exception as e:
        return {"error": str(e)}