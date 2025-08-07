import sqlite3
import hashlib
import time
import random


def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


conn = sqlite3.connect("Dados.db")
cursor = conn.cursor()

cursor.execute("SELECT name, password FROM users")
utilizadores_originais = cursor.fetchall()

random.shuffle(utilizadores_originais)

start_time = time.time()

total_testes = 0
sucesso = 0
falha = 0

for nome, password in utilizadores_originais:

    cursor.execute("SELECT password FROM User_Sha256 WHERE name = ?", (nome,))
    resultado = cursor.fetchone()

    if resultado:
        autenticado = (hash_password(password) == resultado[0])
        sucesso+= 1
        print(str(sucesso)+ str(autenticado))
    else:
        print(f"Utilizador '{nome}' não encontrado (deu erro).")
        falha+=0

    total_testes += 1


end_time = time.time()
tempo_total = end_time - start_time


print(f"Total de comparações: {total_testes}")
print(f"Autenticações bem-sucedidas: {sucesso}")
print(f"Falhas: {falha}")
print(f"Tempo total: {tempo_total:.4f} segundos")

conn.close()
