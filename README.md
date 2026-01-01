# Ferramenta de Extração de Dados para BI

## Visão Geral
Este projeto apresenta uma ferramenta desenvolvida em Python para automatizar a extração de dados de um banco relacional e gerar arquivos estruturados para consumo em ferramentas de Business Intelligence, como o Power BI.

O exemplo público utiliza SQLite para facilitar a execução local, mas a lógica de extração é compatível com outros bancos relacionais, como PostgreSQL e MySQL.

---

## Problema
A extração de dados para análises em BI era realizada de forma manual, exigindo consultas recorrentes ao banco de dados e ajustes frequentes nos arquivos, aumentando o risco de inconsistências e retrabalho.

---

## Solução
Foi desenvolvida uma ferramenta em Python que:
- Conecta-se ao banco de dados
- Executa consultas SQL
- Aplica regras simples de tratamento
- Gera arquivos CSV padronizados e prontos para consumo no Power BI

---

## Tecnologias Utilizadas
- Python
- SQL
- SQLite (exemplo público)
- Power BI

---

## Estrutura do Projeto
python-extrator-dados-powerbi/
├─ data/
│ ├─ database.db
│ └─ seed_database.py
├─ output/
│ └─ dados_operacionais.csv
├─ src/
│ └─ app/
│ ├─ db.py
│ ├─ exporter.py
│ └─ main.py
├─ requirements.txt
└─ README.md

---

## Como Executar o Projeto

### 1. Instalar dependências
```bash
pip install -r requirements.txt
python data/seed_database.py
python src/app/main.py
```

## Observacoes

- Após a execução, o arquivo dados_operacionais.csv será gerado na pasta output/, pronto para importação no Power BI.
- O CSV é gerado com separador ; e encoding UTF-8 para compatibilidade com Excel (PT-BR).
- O projeto possui foco demonstrativo e utiliza dados fictícios.

