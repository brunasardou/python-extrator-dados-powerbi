import sys
import os
import tkinter as tk
from tkinter import messagebox
from app.gui_app import DataExtractorApp


def main():
    root = tk.Tk()
    root.withdraw() # Esconde a janela principal até carregar tudo
    
    try:
                     
        # Se funcionar, mostra a janela
        root.deiconify()
        app = DataExtractorApp(root)
        root.mainloop()
        
    except ImportError as e:
        # Em alguns casos e.name vem None, então extraímos do texto do erro
        missing = getattr(e, "name", None)

        if not missing:
            msg = str(e)
            # padrões comuns:
            # "No module named 'xyz'"
            if "No module named" in msg:
                try:
                    missing = msg.split("No module named", 1)[1].strip()
                    missing = missing.strip(": ").strip("'").strip('"')
                except Exception:
                    missing = None

        if missing:
            messagebox.showerror(
                "Erro de Dependência",
                f"Faltando biblioteca: {missing}\n\nExecute no terminal:\npip install {missing}"
            )
        else:
            messagebox.showerror(
                "Erro de Dependência",
                f"Falha ao importar dependências.\n\nDetalhes:\n{e}"
            )

        root.destroy()

if __name__ == "__main__":
    main()