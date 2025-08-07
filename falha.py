import sqlite3
import random
import string
import time

def gerar_nome_falso():
    return "FakeUser_" + ''.join(random.choices(string.ascii_letters + string.digits, k=8))


conn = sqlite3.connect("Dados.db")
cursor = conn.cursor()

tentativas = 100000
falhas = 0

start_time = time.time()

for _ in range(tentativas):
    nome_falso = gerar_nome_falso()
    cursor.execute("SELECT password FROM users WHERE name = ?", (nome_falso,))
    resultado = cursor.fetchone()
    
    if resultado is None:
        falhas += 1  

end_time = time.time()
tempo_total = end_time - start_time

print(f"Simulação terminada.")
print(f"Tentativas de login: {tentativas}")
print(f"Falhas (utilizadores não encontrados): {falhas}")
print(f"Tempo total: {tempo_total:.4f} segundos")

conn.close()
