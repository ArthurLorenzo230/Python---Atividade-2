try:
    preco = float(input("Preço do produto: "))
    imposto = 1.1
    print("Preço com imposto:", preco * imposto)
except ValueError:
    print("Erro: Digite um valor numérico válido para o preço.")
except KeyboardInterrupt:
    print("\nOperação cancelada pelo usuário.")
except Exception as e:
    print(f"Erro inesperado: {e}")