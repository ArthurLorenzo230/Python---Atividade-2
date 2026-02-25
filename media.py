try:
    qtd = int(input("Quantas notas? "))
    if qtd <= 0:
        print("Erro: A quantidade de notas deve ser maior que zero.")
    else:
        soma = 0
        for i in range(qtd):
            try:
                nota = float(input(f"Nota {i+1}: "))
                soma += nota
            except ValueError:
                print("Erro: Digite um valor numérico válido para a nota.")
                break
        else:
            media = soma / qtd
            print("Média:", media)
except ValueError:
    print("Erro: Digite um número inteiro válido para a quantidade.")
except KeyboardInterrupt:
    print("\nOperação cancelada pelo usuário.")
except Exception as e:
    print(f"Erro inesperado: {e}")