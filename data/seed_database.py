import sqlite3
from datetime import date, timedelta
import random

DB_PATH = "data/database.db"

def criar_banco():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS demandas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data_abertura DATE,
            status TEXT,
            tipo TEXT,
            tempo_resolucao INTEGER,
            responsavel TEXT
        )
    """)

    conn.commit()
    conn.close()

def inserir_dados():
    status_list = ["Aberto", "Em andamento", "Concluído"]
    tipos = ["Incidente", "Solicitação", "Manutenção"]
    responsaveis = ["Ana", "Carlos", "Fernanda", "João"]

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for i in range(120):
        data_abertura = date.today() - timedelta(days=random.randint(0, 90))
        status = random.choice(status_list)
        tipo = random.choice(tipos)

        tempo_resolucao = (
            random.randint(10, 300) if status == "Concluído" else None
        )

        responsavel = random.choice(responsaveis)

        cursor.execute("""
            INSERT INTO demandas (
                data_abertura,
                status,
                tipo,
                tempo_resolucao,
                responsavel
            ) VALUES (?, ?, ?, ?, ?)
        """, (
            data_abertura.isoformat(),
            status,
            tipo,
            tempo_resolucao,
            responsavel
        ))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    criar_banco()
    inserir_dados()
    print("Banco SQLite criado e populado com sucesso.")
