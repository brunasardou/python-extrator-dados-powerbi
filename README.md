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
```bash
pip install -r requirements.txt
```
⚠️ Para alguns bancos (ex: SQL Server, Oracle), é necessário instalar o driver específico no sistema operacional.


2️⃣ (Opcional) Preparar Base de Testes

Caso queira testar com dados fictícios:
```bash
python data/seed_database.py
```

3️⃣ Iniciar a Aplicação
```bash
cd src
python -m app.main
```

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

## 🖥️ Distribuição Desktop (Opcional)

O projeto também pode ser empacotado como uma aplicação desktop executável, permitindo o uso sem necessidade de Python instalado no ambiente.

Esse modo é indicado para:
- Usuários finais
- Ambientes corporativos restritos
- Demonstrações e provas de conceito

A geração do executável é realizada utilizando ferramentas de empacotamento Python (ex: PyInstaller).

## 🖥️ Geração de Executável Desktop (Avançado)

Opcionalmente, a aplicação pode ser empacotada como um executável desktop para uso sem dependência de Python instalado.

Exemplo de empacotamento utilizando PyInstaller:

```powershell
.\.venv\Scripts\python.exe -m PyInstaller `
  --noconsole `
  --onedir `
  --clean `
  --name Extrator_BI_Pro `
  --paths src `
  --hidden-import pyodbc `
  --hidden-import pymysql `
  --hidden-import oracledb `
  --collect-all pandas `
  src\app\main.py
```

> Nota: o executável não é versionado no repositório e pode ser gerado a partir do código-fonte conforme necessidade.


