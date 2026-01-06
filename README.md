🚀 Extrator de Dados Universal Pro (BI & Analytics)

📌 Visão Geral

O Extrator de Dados Universal Pro é uma aplicação desenvolvida em Python para automatizar a extração de dados de múltiplos bancos de dados, com foco em Business Intelligence, Analytics e Performance.

A ferramenta permite conectar-se a diferentes motores SQL, executar consultas personalizadas, aplicar análises estatísticas opcionais e exportar os dados em formatos otimizados para ferramentas como Power BI, Tableau e Excel.

🛠️ Solução & Diferenciais

✔ Motor Universal
Conexão nativa com:

- PostgreSQL
- MySQL
- SQL Server
- Oracle
- SQLite

Utilizando SQLAlchemy, garantindo compatibilidade entre dialetos SQL.

✔ Extração Inteligente para BI
Execução direta de queries SQL definidas pelo usuário, mantendo total controle sobre filtros, joins e regras de negócio.

✔ Análise Estatística (Opcional)
Aplicação de Z-Score para identificação automática de anomalias (outliers) em colunas numéricas, auxiliando análises exploratórias e de qualidade de dados.

✔ Exportação Otimizada para Big Data
Suporte aos formatos:

- Parquet (alto desempenho e menor volume)
- CSV (Excel e análises rápidas)
- JSON (integrações e APIs)

✔ Interface Gráfica Intuitiva
- Interface desenvolvida em Tkinter, com:
- Layout limpo e orientado à produtividade
- Tratamento automático de portas padrão
- Validações de conexão e feedback visual

<img width="578" height="241" alt="image" src="https://github.com/user-attachments/assets/39a115a8-1851-48ad-8f54-e8138ef575e6" />

*Arquitetura modular, facilitando manutenção, evolução e adição de novos recursos.*

## 🖥️ Execução via Terminal

Além da interface gráfica, a aplicação pode ser iniciada diretamente via terminal utilizando o módulo principal do projeto.

1️⃣ Instalar Dependências
pip install -r requirements.txt

⚠️ Para alguns bancos (ex: SQL Server, Oracle), é necessário instalar o driver específico no sistema operacional.


2️⃣ (Opcional) Preparar Base de Testes

Caso queira testar com dados fictícios:

python data/seed_database.py

3️⃣ Iniciar a Aplicação
python -m app.main

📊 Recomendações de Exportação

- CSV - Ideal para volumes menores ou análises rápidas no Excel.
- Parquet - Recomendado para grandes volumes de dados e uso em Power BI, oferecendo melhor performance de leitura e atualização.
- JSON - Indicado para integrações com APIs ou pipelines de dados.

📝 Observações Técnicas

- O projeto utiliza SQLAlchemy para abstração de conexões e compatibilidade entre bancos.
- A análise de anomalias via Z-Score considera valores com desvio padrão absoluto superior a 2 como potenciais outliers.
- A filtragem de dados é feita diretamente via SQL, garantindo flexibilidade total ao usuário.

🎯 Quando usar esta ferramenta?

- Extração de dados para Power BI / Tableau
- Consolidação de dados de múltiplos bancos
- Análises exploratórias e validação de qualidade
- Pipelines simples de dados sem necessidade de ETL pesado
