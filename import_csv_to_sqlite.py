#!/usr/bin/env python3
"""
Script to import a CSV file into a SQLite database.
Usage: Update DB_FILE and CSV_FILE paths as needed, then run:

    python import_csv_to_sqlite.py
"""
import sqlite3
import csv

# Configuration
DB_FILE   = 'racquets.db'                    # SQLite database file to create or update
CSV_FILE  = 'final_csv_file_racquets.csv'    # CSV file to import
TABLE_NAME = 'racquets'                      # <— Hard‑code the table name here

# Connect to (or create) the SQLite database
conn = sqlite3.connect(DB_FILE)
cur  = conn.cursor()

with open(CSV_FILE, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    headers = next(reader)  # Read header row to get column names

    # Clean column names: strip whitespace and replace spaces with underscores
    columns = [h.strip().replace(' ', '_').lower() for h in headers]

    # Drop any old table so we always start fresh
    cur.execute(f'DROP TABLE IF EXISTS "{TABLE_NAME}";')

    # Create table with all TEXT columns
    col_defs  = ', '.join([f'"{col}" TEXT' for col in columns])
    create_sql = f'CREATE TABLE "{TABLE_NAME}" ({col_defs});'
    cur.execute(create_sql)
    print(f"Created table '{TABLE_NAME}' with columns: {columns}")

    # Prepare INSERT statement
    placeholders   = ', '.join(['?' for _ in columns])
    cols_formatted = ', '.join([f'"{col}"' for col in columns])
    insert_sql     = f'INSERT INTO "{TABLE_NAME}" ({cols_formatted}) VALUES ({placeholders});'

    # Insert each row
    count = 0
    for row in reader:
        cur.execute(insert_sql, row)
        count += 1

# Commit and close
conn.commit()
conn.close()
print(f"Imported {count} rows into '{TABLE_NAME}' in '{DB_FILE}'.")



