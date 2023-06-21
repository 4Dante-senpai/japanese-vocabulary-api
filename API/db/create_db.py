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
    #cur.execute("create database japanese")
    cur.execute("SELECT 'CREATE DATABASE japanese' WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'japanese')")
    cur.close()
    conn.close()