def dobro(x):
    try:
        return float(x) * 2
    except (TypeError, ValueError):
        print(f"Erro: Não foi possível converter '{x}' para número.")
        return None

def main():
    valor = input("Digite um número: ")
    
    if valor.strip() == "":
        print("Erro: Entrada vazia não é permitida.")
        return
    
    resultado = dobro(valor)
    
    if resultado is not None:
        print(f"O dobro de {valor} é: {resultado}")

if __name__ == "__main__":
    main()