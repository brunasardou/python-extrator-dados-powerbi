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

🏗️ Estrutura do Projeto
Projeto/
├── requirements.txt      # Dependências (Pandas, SQLAlchemy, drivers SQL)
├── extrator.log          # Registro de operações e erros
├── README.md             # Documentação do projeto
├── data/                 # Arquivos locais (.db SQLite, se aplicável)
└── src/app/              # Código-fonte
    ├── main.py           # Inicialização da aplicação
    ├── gui_app.py        # Interface gráfica (Tkinter)
    ├── db.py             # Motor de conexão universal
    └── exporter.py       # Lógica de análise estatística e exportação

*Arquitetura modular, facilitando manutenção, evolução e adição de novos recursos.*

🚀 Como Executar o Projeto
1️⃣ Instalar Dependências
pip install -r requirements.txt

⚠️ Para alguns bancos (ex: SQL Server, Oracle), é necessário instalar o driver específico no sistema operacional.


2️⃣ (Opcional) Preparar Base de Testes

Caso queira testar com dados fictícios:

python data/seed_database.py

3️⃣ Iniciar a Aplicação
python src/app/main.py

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