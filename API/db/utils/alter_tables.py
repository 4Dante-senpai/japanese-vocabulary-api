import psycopg2
import os

def set_pk(tables):
        conn = psycopg2.connect(
                host=os.getenv('POSTGRES_HOST'),
                database=os.getenv('POSTGRES_DB'),
                user=os.getenv('POSTGRES_USER'),
                password=os.getenv('POSTGRES_PASSWORD'))

        cur = conn.cursor()
        for table in tables.keys():
                cur.execute(f'ALTER TABLE {table} ADD PRIMARY KEY ("{tables[table]}");')
                conn.commit()
        cur.close()