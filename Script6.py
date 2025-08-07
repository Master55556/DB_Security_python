import sqlite3
import random
import string
from faker import Faker

# fake = Faker()
faker_pt = Faker('pt_PT')
faker_en = Faker('en_US')
conn = sqlite3.connect("Dados.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE,
    address TEXT,
    password TEXT
)
''')


def gera_password(tamanho=15):
    chars = string.ascii_letters + string.digits + "!@#$%&*"
    return ''.join(random.choice(chars) for _ in range(tamanho))


quantos_users = 10000
inseridos = 0
tentativas = 0
max_tentativas = 500

while inseridos < quantos_users:

    faker = random.choice([faker_pt, faker_en])  # alternar entre pt e en
    nome_completo = faker.name()
    morada = faker.address().replace("\n", ", ")
    password = gera_password()
    # nome_completo = fake.name()
    # morada = fake.address().replace("\n", ", ")
    # password = gera_password()

    try:
        cursor.execute("INSERT INTO users (name, address, password) VALUES (?, ?, ?)",
                       (nome_completo, morada, password))
        inseridos += 1
        print(f"{inseridos}Inserido: {nome_completo}")
    except sqlite3.IntegrityError:
        tentativas += 1
        nome_completo = nome_completo+" "+str(tentativas)
        cursor.execute("INSERT INTO users (name, address, password) VALUES (?, ?, ?)",
                       (nome_completo, morada, password))
        pass


conn.commit()
conn.close()

print(f"Total inseridos: {inseridos}")
