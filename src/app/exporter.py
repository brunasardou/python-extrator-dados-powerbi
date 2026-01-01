import pandas as pd
import os
from db import get_connection

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

def exportar_dados():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    query = """
        SELECT
            id,
            data_abertura,
            status,
            tipo,
            tempo_resolucao,
            responsavel
        FROM demandas
    """

    conn = get_connection()
    df = pd.read_sql_query(query, conn)
    conn.close()

    # Conversão de data
    df["data_abertura"] = pd.to_datetime(df["data_abertura"])

    # Coluna de SLA
    def calcular_sla(row):
        if row["status"] != "Concluído":
            return "Em andamento"
        elif row["tempo_resolucao"] <= 120:
            return "Dentro do SLA"
        else:
            return "Fora do SLA"

    df["sla_status"] = df.apply(calcular_sla, axis=1)

    # Ordenação
    df = df.sort_values(by="data_abertura")

    output_path = os.path.join(OUTPUT_DIR, "dados_operacionais.csv")
    df.to_csv(
        output_path,
        index=False,
        sep=";",
        encoding="utf-8-sig"
)

    return output_path
