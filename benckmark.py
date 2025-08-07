import sqlite3
import time
from cryptography.fernet import Fernet

with open("chave.key", "rb") as f:
    key = f.read()
fernet = Fernet(key)

conn = sqlite3.connect("Dados.db")
cursor = conn.cursor()

cursor.execute("SELECT name, address FROM Users_Morada_Encrypted")
registos = cursor.fetchall()

start_time = time.time()

desencriptadas = 0
for nome, morada_enc in registos:
    try:
        morada = fernet.decrypt(morada_enc.encode()).decode()
        desencriptadas += 1
        print(f"{nome}: {morada}")#COMENTA OU DESCOMENTA ESTA LINHA E VE A DIFERENÇA DE PROCESSAMENTO
    except Exception as e:
        print(f"Erro ao desencriptar morada de {nome}: {e}")

end_time = time.time()
total_time = end_time - start_time

print(f"\nTotal de moradas desencriptadas: {desencriptadas}")
print(f"Tempo desencriptação: {total_time:.4f} segundos")
