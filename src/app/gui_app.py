import tkinter as tk
from tkinter import messagebox, scrolledtext, filedialog

from app.db import connect_postgres, fetch_all
from app.exporter import rows_to_dicts, save_json


class DataExtractorApp:
    def __init__(self, master: tk.Tk):
        self.master = master
        self.master.title("Extrator de Dados → JSON (Power BI)")
        self.master.geometry("820x720")

        self.conn = None

        # --- conexão ---
        self.frame_conn = tk.LabelFrame(master, text="Conexão PostgreSQL", padx=10, pady=10)
        self.frame_conn.pack(fill="x", padx=16, pady=10)

        self._build_conn_fields()

        # --- query ---
        self.frame_sql = tk.LabelFrame(master, text="Query SQL", padx=10, pady=10)
        self.frame_sql.pack(fill="both", expand=True, padx=16, pady=10)

        self.sql_text = scrolledtext.ScrolledText(self.frame_sql, wrap=tk.WORD, height=14)
        self.sql_text.pack(fill="both", expand=True)
        self.sql_text.insert(tk.END, "SELECT 1 AS exemplo;")

        # --- ações ---
        self.frame_actions = tk.Frame(master, padx=10, pady=10)
        self.frame_actions.pack(fill="x", padx=16, pady=10)

        tk.Button(self.frame_actions, text="Testar conexão", command=self.test_connection).pack(side="left", padx=6)
        tk.Button(self.frame_actions, text="Executar query e salvar JSON", command=self.run_and_export).pack(side="left", padx=6)
        tk.Button(self.frame_actions, text="Fechar", command=self.on_close).pack(side="right", padx=6)

        self.status = tk.Label(master, text="Status: pronto", anchor="w")
        self.status.pack(fill="x", padx=16, pady=(0, 10))

    def _build_conn_fields(self):
        labels = ["Host", "Porta", "Database", "Usuário", "Senha"]
        defaults = {"Host": "localhost", "Porta": "5432", "Database": "postgres", "Usuário": "postgres", "Senha": ""}

        self.entries = {}
        for i, lab in enumerate(labels):
            tk.Label(self.frame_conn, text=f"{lab}:").grid(row=i, column=0, sticky="w", pady=3)
            ent = tk.Entry(self.frame_conn, width=42, show="*" if lab == "Senha" else None)
            ent.grid(row=i, column=1, sticky="ew", pady=3)
            ent.insert(0, defaults[lab])
            self.entries[lab] = ent

        self.frame_conn.grid_columnconfigure(1, weight=1)

    def _set_status(self, msg: str):
        self.status.config(text=f"Status: {msg}")

    def _get_conn_params(self):
        host = self.entries["Host"].get().strip()
        port = self.entries["Porta"].get().strip()
        dbname = self.entries["Database"].get().strip()
        user = self.entries["Usuário"].get().strip()
        password = self.entries["Senha"].get()  # não strip em senha
        if not all([host, port, dbname, user]):
            raise ValueError("Preencha Host, Porta, Database e Usuário.")
        return host, port, dbname, user, password

    def test_connection(self):
        try:
            host, port, dbname, user, password = self._get_conn_params()
            if self.conn:
                try:
                    self.conn.close()
                except Exception:
                    pass
                self.conn = None

            self._set_status("conectando...")
            self.conn = connect_postgres(host, port, dbname, user, password)
            self._set_status("conectado ✅")
            messagebox.showinfo("Conexão", "Conexão estabelecida com sucesso!")
        except Exception as e:
            self._set_status("erro na conexão ❌")
            messagebox.showerror("Erro de Conexão", str(e))

    def run_and_export(self):
        try:
            if not self.conn:
                messagebox.showwarning("Atenção", "Conecte no banco primeiro (Testar conexão).")
                return

            query = self.sql_text.get("1.0", tk.END).strip()
            if not query:
                messagebox.showwarning("Atenção", "Digite uma query SQL.")
                return

            self._set_status("executando query...")
            columns, rows = fetch_all(self.conn, query)

            if not columns or not rows:
                self._set_status("query sem resultados")
                messagebox.showinfo("Resultado", "A query não retornou dados.")
                return

            data = rows_to_dicts(columns, rows)

            filepath = filedialog.asksaveasfilename(
                title="Salvar JSON",
                defaultextension=".json",
                filetypes=[("JSON", "*.json")],
                initialfile="dados_extraidos.json",
            )
            if not filepath:
                self._set_status("exportação cancelada")
                return

            save_json(filepath, data)
            self._set_status("exportado ✅")
            messagebox.showinfo("Sucesso", f"JSON salvo em:\n{filepath}")

        except Exception as e:
            self._set_status("erro ❌")
            messagebox.showerror("Erro", str(e))

    def on_close(self):
        try:
            if self.conn:
                self.conn.close()
        except Exception:
            pass
        self.master.destroy()
