pessoa = {"nome": "João", "idade": 20}
try:
    chave = input("Qual campo quer ver? ")
    print(pessoa[chave])
except KeyError:
    print(f"Erro: O campo '{chave}' não existe. Campos disponíveis: {list(pessoa.keys())}")
except KeyboardInterrupt:
    print("\nOperação cancelada pelo usuário.")
except Exception as e:
    print(f"Erro inesperado: {e}")