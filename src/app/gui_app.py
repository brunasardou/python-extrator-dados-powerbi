import tkinter as tk
from tkinter import messagebox, scrolledtext, filedialog, ttk
from app.db import get_engine
from app.exporter import processar_e_exportar


class DataExtractorApp:
    def __init__(self, master: tk.Tk):
        self.master = master
        self.master.title("Data Intelligence Engine")
        self.master.geometry("1000x800")
        self.master.configure(bg="#F5F7FB")
        self.engine = None
        self._setup_ui()

    def _setup_ui(self):
        content = tk.Frame(self.master, bg="#F5F7FB", padx=60, pady=30)
        content.pack(fill="both", expand=True)

        # ================= HEADER =================
        tk.Label(
            content,
            text="Extrator de Dados",
            bg="#F5F7FB",
            fg="#111827",
            font=("Segoe UI", 28, "bold"),
        ).pack(anchor="w")

        tk.Label(
            content,
            text="Conecte sua fonte de dados e inicie a análise estatística avançada.",
            bg="#F5F7FB",
            fg="#6B7280",
            font=("Segoe UI", 11),
        ).pack(anchor="w", pady=(5, 40))

        # ================= MOTOR SQL =================
        motor_frame = tk.Frame(content, bg="#F5F7FB")
        motor_frame.pack(fill="x", pady=(10, 20))

        tk.Label(
            motor_frame,
            text="BANCO DE DADOS:",
            bg="#F5F7FB",
            fg="#9CA3AF",
            font=("Segoe UI", 8, "bold"),
        ).pack(side="left")

        self.db_combobox = ttk.Combobox(
            motor_frame,
            values=["PostgreSQL", "MySQL", "SQL Server", "Oracle", "SQLite"],
            state="readonly",
            width=20,
        )
        self.db_combobox.set("PostgreSQL")
        self.db_combobox.pack(side="left", padx=15)

        # ================= INPUT GRID =================
        input_grid = tk.Frame(content, bg="#F5F7FB")
        input_grid.pack(fill="x", pady=10)

        # a coluna 2 precisa esticar (Database + botão)
        input_grid.grid_columnconfigure(2, weight=1)

        self.entries = {}

        def create_modern_input(parent, label, row, col, width=25, show=None):
            frame = tk.Frame(parent, bg="#F5F7FB")

            sticky = "ew" if col == 2 else "w"
            frame.grid(row=row, column=col, sticky=sticky, padx=(0, 25), pady=8)

            tk.Label(
                frame,
                text=label.upper(),
                bg="#F5F7FB",
                fg="#9CA3AA",
                font=("Segoe UI", 7, "bold"),
            ).pack(anchor="w")

            ent = tk.Entry(
                frame,
                width=width,
                font=("Segoe UI", 10),
                show=show,
                relief="flat",
                bg="#DEE9F0",
                highlightthickness=0,
            )

            fillx = "x" if col == 2 else None
            ent.pack(pady=(5, 0), ipady=6, ipadx=8, fill=fillx)

            line = tk.Frame(frame, height=1, bg="#E5E7EB")
            line.pack(fill="x")

            ent.bind("<FocusIn>", lambda e: line.configure(bg="#1E40AF"))
            ent.bind("<FocusOut>", lambda e: line.configure(bg="#E5E7EB"))

            self.entries[label] = ent

        # -------- Linha 0
        create_modern_input(input_grid, "Host", 0, 0, 30)
        create_modern_input(input_grid, "Porta", 0, 1, 10)
        create_modern_input(input_grid, "Database", 0, 2, 30)

        # -------- Linha 1
        create_modern_input(input_grid, "Usuário", 1, 0, 30)
        create_modern_input(input_grid, "Senha", 1, 1, 30, show="*")

        # ================= BOTÃO TESTAR CONEXÃO =================
        btn_slot = tk.Frame(input_grid, bg="#F5F7FB")
        btn_slot.grid(row=1, column=2, sticky="ew", padx=(0, 25), pady=8)

        # ocupa espaço do label para alinhar como campo
        tk.Label(
            btn_slot,
            text="",
            bg="#F5F7FB",
            font=("Segoe UI", 7, "bold"),
        ).pack(anchor="w")

        self.btn_test = tk.Button(
            btn_slot,
            text="TESTAR CONEXÃO",
            command=self.test_connection,
            bg="#395EDA",
            fg="white",
            font=("Segoe UI", 9, "bold"),
            relief="flat",
            padx=28,
            pady=10,
            cursor="hand2",
        )
        self.btn_test.pack(anchor="e", pady=(6, 0))

        # ================= SQL =================
        tk.Label(
            content,
            text="INSTRUÇÃO SQL",
            bg="#F5F7FB",
            fg="#9CA3AF",
            font=("Segoe UI", 8, "bold"),
        ).pack(anchor="w", pady=(25, 8))

        self.sql_text = scrolledtext.ScrolledText(
            content,
            height=12,
            font=("Consolas", 11),
            relief="flat",
            bg="#0F172A",
            fg="#F8FAFC",
            padx=15,
            pady=15,
        )
        self.sql_text.pack(fill="both", expand=True)
        self.sql_text.insert("1.0", "SELECT * FROM vendas_big")

        # ================= FOOTER =================
        footer = tk.Frame(content, bg="#F5F7FB", pady=30)
        footer.pack(fill="x")

        self.btn_run = tk.Button(
            footer,
            text="PROCESSAR E EXPORTAR",
            command=self.run_process,
            bg="#395EDA",
            fg="white",
            font=("Segoe UI", 9, "bold"),
            relief="flat",
            padx=35,
            pady=12,
            cursor="hand2",
        )
        self.btn_run.pack(side="right")

    # ================= FUNÇÕES =================
    def test_connection(self):
        try:
            params = {
                "host": self.entries["Host"].get().strip(),
                "port": (self.entries["Porta"].get().strip() or "5432"),
                "database": self.entries["Database"].get().strip(),
                "user": self.entries["Usuário"].get().strip(),
                "password": self.entries["Senha"].get().strip(),
            }

            if not params["host"] or not params["database"] or not params["user"]:
                return messagebox.showwarning("Aviso", "Preencha Host, Database e Usuário.")
            if not params["password"]:
                return messagebox.showwarning("Aviso", "Preencha a Senha.")

            self.engine = get_engine(self.db_combobox.get(), params)

            from sqlalchemy import text
            with self.engine.connect() as conn:
                conn.execute(text("SELECT 1"))

            messagebox.showinfo("Sucesso", "Conectado com sucesso!")

        except Exception as e:
            messagebox.showerror("Falha na ligação", str(e))

    def run_process(self):
        import pandas as pd

        if not self.engine:
            return messagebox.showwarning("Aviso", "Por favor, valide a conexão primeiro.")

        try:
            query = self.sql_text.get("1.0", tk.END).strip()
            if not query:
                return messagebox.showwarning("Aviso", "Informe uma instrução SQL.")

            df = pd.read_sql_query(query, self.engine)

            if df.empty:
                return messagebox.showinfo("Vazio", "Nenhum dado retornado.")

            cols_num = df.select_dtypes(include=["number"]).columns.tolist()
            col_alvo = self._abrir_seletor(cols_num) if cols_num else None

            filepath = filedialog.asksaveasfilename(
                title="Local de Saída",
                defaultextension=".parquet",
                filetypes=[
                    ("Parquet (Performance)", "*.parquet"),
                    ("CSV (Excel)", "*.csv"),
                    ("JSON (API/Data Lake)", "*.json"),
                ],
            )

            if filepath:
                processar_e_exportar(df, filepath, col_alvo)
                messagebox.showinfo("Sucesso", "Dados exportados com sucesso!")

        except Exception as e:
            messagebox.showerror("Erro SQL", str(e))

    def _abrir_seletor(self, colunas):
        if not messagebox.askyesno("Análise", "Aplicar análise de Z-Score?"):
            return None

        win = tk.Toplevel(self.master)
        win.title("Seleção")
        win.geometry("350x180")
        win.configure(bg="#F5F7FB")
        win.grab_set()

        tk.Label(
            win,
            text="Selecione a coluna:",
            bg="#F5F7FB",
            font=("Segoe UI", 10),
        ).pack(pady=15)

        selecionada = tk.StringVar(value=colunas[0])

        combo = ttk.Combobox(
            win,
            values=colunas,
            state="readonly",
            width=25,
            textvariable=selecionada,
        )
        combo.pack()

        tk.Button(
            win,
            text="Confirmar",
            command=win.destroy,
            bg="#395EDA",
            fg="white",
            relief="flat",
            padx=20,
            pady=8,
            font=("Segoe UI", 9, "bold"),
        ).pack(pady=20)

        win.wait_window()
        return selecionada.get()


if __name__ == "__main__":
    root = tk.Tk()
    app = DataExtractorApp(root)
    root.mainloop()
