import sqlite3
import random
import string

def gera_password(tamanho=10):
    chars = string.ascii_letters + string.digits + "!@#$%&*"
    return ''.join(random.choice(chars) for _ in range(tamanho))

conn = sqlite3.connect("Dados.db") 
cursor = conn.cursor()


for i in range(10):
    nome = f"FakeUser_{i+1}"
    morada = f"Rua Falsa, {100 + i}"
    password = gera_password()
    cursor.execute("INSERT INTO users (name, address, password) VALUES (?, ?, ?)", #os ? supostamente é um  placeholder seguro, e que evita SQL injection https://youtu.be/psNYor1FV9c?si=m1DqcdhVRb0OIfNp
                   (nome, morada, password))

conn.commit()
conn.close()

print("Mais utilizadores adicionados com sucesso.")
