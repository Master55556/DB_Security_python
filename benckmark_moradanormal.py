import sqlite3
import time

conn = sqlite3.connect("Dados.db")
cursor = conn.cursor()

start_time = time.time()

cursor.execute("SELECT name, address FROM users")
utilizadores = cursor.fetchall()

for nome, morada in utilizadores:
    _ = morada  
    

end_time = time.time()
tempo_total = end_time - start_time

print(f"Total de utilizadores: {len(utilizadores)}")
print(f"Tempo total da morada sem tar encriptada: {tempo_total:.4f} segundos")

conn.close()
