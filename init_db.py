import psycopg2
from dotenv import load_dotenv
load_dotenv()

import os

conn = psycopg2.connect(host='localhost',
                        database='mpharma-dev',
                        user=os.environ['DB_USERNAME'],
                        # password=os.environ['DB_PASSWORD']
                        )
# apetsiampiah
# Apetsi@1990
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS diagnosis_codes;')
cur.execute('CREATE TABLE diagnosis_codes (id serial PRIMARY KEY,'
            'category_code VARCHAR NOT NULL,'
            'diagnosis_code VARCHAR NOT NULL,'
            'full_code VARCHAR NOT NULL,'
            'abbreviated_description VARCHAR NOT NULL,'
            'full_description VARCHAR NOT NULL,'
            'category_title VARCHAR NOT NULL);')

conn.commit()

cur.close()
conn.close()
