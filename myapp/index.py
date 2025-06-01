import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("myapp.db")

# Execute the SQL query
conn.execute("""
CREATE TABLE IF NOT EXISTS persons (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    dob TIMESTAMP NOT NULL,
    phone TEXT,
    CONSTRAINT person_name_IDX UNIQUE (name),
    CONSTRAINT person_phone_IDX UNIQUE (phone)
);
""")

# Close the connection
conn.close()
