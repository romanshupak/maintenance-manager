import sqlite3
import json

# Підключення до бази даних
conn = sqlite3.connect("db.sqlite3")
cursor = conn.cursor()

# Отримуємо список таблиць
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

database_dict = {}

for table in tables:
    table_name = table[0]
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()

    # Отримуємо назви колонок
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = [column[1] for column in cursor.fetchall()]

    table_data = []
    for row in rows:
        row_data = {}
        for idx, value in enumerate(row):
            row_data[columns[idx]] = value
        table_data.append(row_data)

    database_dict[table_name] = table_data

# Записуємо у файл JSON
with open("output.json", "w", encoding="utf-8") as f:
    json.dump(database_dict, f, ensure_ascii=False, indent=4)

# Закриваємо з'єднання з базою даних
conn.close()
