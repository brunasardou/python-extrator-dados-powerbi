from typing import Tuple, Dict, Any


def _wrap_base_query(base_query: str) -> str:
    q = base_query.strip().rstrip(";")
    return f"SELECT * FROM ({q}) AS base"


def build_incremental_query(
    base_query: str,
    strategy: str,
    column: str,
    last_value
) -> Tuple[str, Dict[str, Any]]:
    """
    Retorna (query, params).

    strategy:
      - "timestamp": incremental por data/timestamp -> WHERE column > :last_value
      - "max": incremental por id/numérico -> WHERE column > :last_value
      - "window": últimos X dias (last_value = int dias) -> WHERE column >= (agora - X dias)
    """
    if not strategy or not column:
        raise ValueError("strategy e column são obrigatórios.")

    wrapped = _wrap_base_query(base_query)
    col = column.strip()

    # incremental por last_value
    if strategy in ("timestamp", "max"):
        if last_value is None or str(last_value).strip() == "":
            raise ValueError("last_value é obrigatório para strategy timestamp/max.")
        query = f"{wrapped} WHERE {col} > :last_value"
        return query, {"last_value": last_value}

    # janela por período (últimos X dias)
    if strategy == "window":
        try:
            days = int(last_value)
        except Exception:
            raise ValueError("Para strategy=window, last_value deve ser um inteiro (dias).")

        # ✅ padrão que funciona muito bem em Postgres/MySQL
        # Se seu SQL Server/Oracle precisar, você pode evoluir isso por "dialect" depois.
        query = f"{wrapped} WHERE {col} >= (CURRENT_TIMESTAMP - INTERVAL '{days} days')"
        return query, {}

    raise ValueError(f"strategy inválida: {strategy}")
