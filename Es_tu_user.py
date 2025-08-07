import sqlite3
import time
import random

conn = sqlite3.connect("Dados.db")
cursor = conn.cursor()

cursor.execute("SELECT name, password FROM users")
utilizadores = cursor.fetchall() 


random.shuffle(utilizadores)


inicio = time.time()

comparacoes = 0

for nome, senha_correta in utilizadores:
    cursor.execute("SELECT password FROM Users_Dup WHERE name = ?", (nome,))
    resultado = cursor.fetchone() # fetchone buscar só a primeira linha do resultado retornando uma sequencia unica

    if resultado:
        autenticado = (senha_correta == resultado[0])
        comparacoes += 1
        print(str(comparacoes) + str(autenticado))
    else:
        print(f"Utilizador '{nome}' não encontrado (deu erro).")


fim = time.time()
tempo_total = fim - inicio

print(f"\nComparações realizadas: {comparacoes}")
print(f"Tempo total: {tempo_total:.4f} segundos")

conn.close()
