import psycopg2
import os

def create_japanese():
    conn = psycopg2.connect(
                host= os.getenv('POSTGRES_HOST'),
                database= "postgres",
                user= "postgres",
                password= "postgres"
                )
    cur = conn.cursor()
    
    cur.execute("commit")
    cur.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = 'japanese'")
    exists = cur.fetchone()
    if not exists:
        cur.execute('CREATE DATABASE japanese')
    else:
        print(f"Database 'japanese' alredy exist")
    cur.execute("commit")
    cur.close()
    conn.close()