import sqlite3

conn = sqlite3.connect("Dados.db")
cursor = conn.cursor()

cursor.execute("SELECT MAX(id) FROM users")
max_id = cursor.fetchone()[0]

if max_id is None:
    print("A tabela está vazia.")
elif max_id < 100:
    print(f"A tabela só tem {max_id} registos. Não é possível apagar 100.")
else:
    limite = max_id - 100

    cursor.execute("DELETE FROM users WHERE id > ?", (limite,))
    conn.commit()
    print("Últimos 100 utilizadores removidos com sucesso.")

conn.close()
