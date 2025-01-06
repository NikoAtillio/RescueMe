import psycopg2
import os
from datetime import date

def connect_db():
    """Connect to the PostgreSQL database"""
    try:
        conn = psycopg2.connect(os.environ.get('DATABASE_URL'))
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return None

def create_tables():
    commands = (
        """
        CREATE TYPE animal_status AS ENUM ('Available', 'Adopted', 'Fostered', 'Pending')
        """,
        """
        CREATE TABLE IF NOT EXISTS animals (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            species VARCHAR(50) NOT NULL,
            breed VARCHAR(50),
            age INTEGER,
            gender VARCHAR(10),
            size VARCHAR(20),
            status animal_status DEFAULT 'Available',
            arrival_date DATE DEFAULT CURRENT_DATE,
            description VARCHAR(500)
        )
        """
    )
    
    conn = None
    try:
        conn = connect_db()
        cur = conn.cursor()
        for command in commands:
            cur.execute(command)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    create_tables()