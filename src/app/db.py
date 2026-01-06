import logging
import os
import urllib.parse
from sqlalchemy import create_engine

def get_engine(db_type, params):
    params = params or {}
    if not isinstance(params, dict):
        raise TypeError("params deve ser um dict.")

    password = urllib.parse.quote_plus(str(params.get("password", "") or ""))
    user = str(params.get("user", "") or "")
    host = str(params.get("host", "") or "")
    database = str(params.get("database", "") or "")
    port_raw = str(params.get("port", "") or "").strip()

    if db_type == "SQLite":
        if not os.path.isabs(host):
            base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            host = os.path.join(base_dir, "data", host)
        return create_engine(f"sqlite:///{host}")

    default_ports = {"PostgreSQL": "5432", "MySQL": "3306", "Oracle": "1521"}
    port = port_raw or default_ports.get(db_type, "")

    if db_type == "PostgreSQL":
        url = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"
    elif db_type == "MySQL":
        url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
    elif db_type in ("SQL Server", "Microsoft Azure"):
        url = f"mssql+pyodbc://{user}:{password}@{host}/{database}?driver=ODBC+Driver+17+for+SQL+Server"
    elif db_type == "Oracle":
        url = f"oracle+oracledb://{user}:{password}@{host}:{port}/?service_name={database}"
    else:
        raise ValueError(f"Motor não suportado: {db_type}")

    return create_engine(url, pool_pre_ping=True)
