from exporter import exportar_dados

def main():
    caminho = exportar_dados()
    print(f"Arquivo CSV gerado com sucesso em: {caminho}")

if __name__ == "__main__":
    main()
