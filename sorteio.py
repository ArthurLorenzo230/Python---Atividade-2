nomes = ["Arthur", "Gabriel", "Enzo", "Julia"]
try:
    i = int(input("Indique um número para sortear uma pessoa: "))
    print("Nome:", nomes[i])
except ValueError:
    print("Erro: Digite um número inteiro válido.")
except IndexError:
    print(f"Erro: Digite um número entre 0 e {len(nomes)-1}.")
except KeyboardInterrupt:
    print("\nOperação cancelada pelo usuário.")
except Exception as e:
    print(f"Erro inesperado: {e}")