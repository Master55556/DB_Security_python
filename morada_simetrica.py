import sqlite3
from cryptography.fernet import Fernet

with open("chave.key", "rb") as f:
    key = f.read()

fernet = Fernet(key)

conn = sqlite3.connect("Dados.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Users_Morada_Encrypted (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    address TEXT,
    password TEXT NOT NULL
)
""")

cursor.execute("SELECT name, address, password FROM users")
utilizadores = cursor.fetchall()

for nome, morada, password in utilizadores:
    morada_encriptada = fernet.encrypt(morada.encode()).decode()
    cursor.execute("INSERT INTO Users_Morada_Encrypted (name, address, password) VALUES (?, ?, ?)",
                   (nome, morada_encriptada, password))

conn.commit()
conn.close()
print("Dados migrados com morada encriptada.")
