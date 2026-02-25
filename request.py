import requests

try:
    nome = input("Digite um número para descobrir o pokemon: ").strip().lower()
    url = f"https://pokeapi.co/api/v2/pokemon/{nome}"
    
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        dados = resposta.json()
        print("Nome:", dados["name"])
    elif resposta.status_code == 404:
        print(f"Erro: Pokémon '{nome}' não encontrado.")
    else:
        print(f"Erro na requisição: Código {resposta.status_code}")
        
except requests.exceptions.ConnectionError:
    print("Erro: Sem conexão com a internet.")
except requests.exceptions.Timeout:
    print("Erro: Tempo de requisição excedido.")
except requests.exceptions.RequestException as e:
    print(f"Erro na requisição: {e}")
except KeyboardInterrupt:
    print("\nOperação cancelada pelo usuário.")
except Exception as e:
    print(f"Erro inesperado: {e}")