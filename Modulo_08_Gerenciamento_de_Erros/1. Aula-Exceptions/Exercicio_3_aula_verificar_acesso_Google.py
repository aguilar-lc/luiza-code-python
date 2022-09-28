
# Exercício 3 - Crie um script que acesse o site da Google e retorne se o mesmo está acessível

import requests

try:
    result = requests.get("https://www.google.com.br/")
    result.raise_for_status()
    print("Google acessado!")
except requests.exceptions as error:
    print(f"Não foi possível acessar o Google. Erro {error._cause__}")