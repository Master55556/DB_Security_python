import sqlite3
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


conn = sqlite3.connect("Dados.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS Users_Dup(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    address TEXT,
    password TEXT NOT NULL
)
""")

cursor.execute("SELECT name, address, password FROM users")
dados_originais = cursor.fetchall()
inseridos = 0

for nome, morada, password in dados_originais:
    inseridos+=1
    cursor.execute("""
        INSERT INTO Users_Dup(name, address, password)
        VALUES (?, ?, ?)
    """, (nome, morada,password))
    if inseridos%1000 == 0:
        print(inseridos)


conn.commit()
conn.close()

print("Dados migrados com sucesso com SHA-256")
