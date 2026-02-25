nome_arquivo = input("Arquivo: ")
try:
    f = open(nome_arquivo, "r", encoding="utf-8")
    print(f.read())
except FileNotFoundError:
    print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
except PermissionError:
    print(f"Erro: Sem permissão para ler o arquivo '{nome_arquivo}'.")
except Exception as e:
    print(f"Erro inesperado: {e}")
finally:
    try:
        f.close()
    except:
        pass