import duckdb
import os
from pathlib import Path

DB_Path = os.getenv("MOTHERCARE_DB_PATH", str(Path(__file__).resolve().parent / "data" / "mothercare.duckdb"))

def get_connection(): # returns a duckdb connection to the file
    return duckdb.connect(DB_Path)

def init_db():
    con = get_connection()

    # basic tables

    # users table
    con.execute("""
    CREATE TABLE IF NOT EXISTS users (
                email TEXT PRIMARY KEY,
                name TEXT,
                age INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
    """)

    # mood_sleep_logs table
    con.execute("""
                CREATE SEQUENCE IF NOT EXISTS mood_sleep_logs_seq START 1;


    CREATE TABLE IF NOT EXISTS mood_sleep_logs (
        log_id INTEGER DEFAULT nextval('mood_sleep_logs_seq') PRIMARY KEY,
        email TEXT,
        date DATE,
        mood_score INTEGER CHECK(mood_score BETWEEN 1 AND 10),
        sleep_hours INTEGER,
        notes TEXT
    );
    """)

    # EDPS test results table
    con.execute("""
    CREATE SEQUENCE IF NOT EXISTS edps_seq START 1;
        
    CREATE TABLE IF NOT EXISTS edps_results (
        result_id INTEGER DEFAULT nextval('edps_seq') PRIMARY KEY,
        email TEXT,
        date DATE,
        q1 INTEGER, q2 INTEGER, q3 INTEGER, q4 INTEGER, q5 INTEGER,
        q6 INTEGER, q7 INTEGER, q8 INTEGER, q9 INTEGER, q10 INTEGER,
        total_score INTEGER,
        interpretation TEXT
        );
    """)

    # # PBQ TEST RESULTS TABLE
    con.execute("""
        CREATE SEQUENCE IF NOT EXISTS pbq_seq START 1;
        
        CREATE TABLE IF NOT EXISTS pbq_results (
            result_id INTEGER DEFAULT nextval ('pbq_seq') PRIMARY KEY,
            email TEXT,
            date DATE,
            q1 INTEGER, q2 INTEGER, q3 INTEGER, q4 INTEGER, q5 INTEGER,
            q6 INTEGER, q7 INTEGER, q8 INTEGER, q9 INTEGER, q10 INTEGER,
            q11 INTEGER, q12 INTEGER, q13 INTEGER, q14 INTEGER, q15 INTEGER,
            q16 INTEGER, q17 INTEGER, q18 INTEGER, q19 INTEGER, q20 INTEGER,
            q21 INTEGER, q22 INTEGER, q23 INTEGER, q24 INTEGER, q25 INTEGER,
            total_score INTEGER,
            interpretation TEXT
        );
    """)

    # coping assesment table
    con.execute("""
    CREATE SEQUENCE IF NOT EXISTS coping_assessment_seq START 1;

        CREATE TABLE IF NOT EXISTS coping_assessments (
            assessment_id INTEGER DEFAULT nextval ('coping_assessment_seq') PRIMARY KEY,
            email TEXT,
            date DATE,
            q1 INTEGER, q2 INTEGER, q3 INTEGER, q4 INTEGER, q5 INTEGER,
            q6 INTEGER, q7 INTEGER, q8 INTEGER, q9 INTEGER, q10 INTEGER,
            q11 INTEGER, q12 INTEGER, q13 INTEGER, q14 INTEGER, q15 INTEGER,
            q16 INTEGER, q17 INTEGER, q18 INTEGER, q19 INTEGER, q20 INTEGER,
            q21 INTEGER, q22 INTEGER, q23 INTEGER, q24 INTEGER, q25 INTEGER,
            q26 INTEGER, q27 INTEGER, q28 INTEGER,
            score INTEGER,
            interpretation TEXT
                );
    """)

    # coping cards table
    con.execute("""
    CREATE SEQUENCE IF NOT EXISTS coping_cards_seq START 1;

    CREATE TABLE IF NOT EXISTS coping_cards (
        card_id INTEGER DEFAULT nextval('coping_cards_seq') PRIMARY KEY,
        category TEXT,
        title TEXT,
        description TEXT
    );
    """)

    # Information hub table
    con.execute("""
    CREATE TABLE IF NOT EXISTS information_hub (
        info_id INTEGER PRIMARY KEY,
        category TEXT,
        content TEXT
   );
    """)

    # Admin table
    con.execute("""
    CREATE TABLE IF NOT EXISTS admin (
        username TEXT PRIMARY KEY,
        password_hash TEXT,
        role TEXT
    );
    """)

    con.close() # close the connection after table creation

if __name__ == "__main__":
    # Ensure data directory exists
    os.makedirs("data", exist_ok=True)
    init_db()
    print("Database initialized successfully!")
