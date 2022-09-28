
# 3. Observe o programa abaixo

#number = int(input("Digite um número: "))
#print("O número digitado foi:", number)

# Reescreva esse código de uma forma com que ele seja capaz de tratar a inserção 
# de um caractere por parte do usuário

import logging

logging.basicConfig(level=logging.ERROR, filename="logging_users.log")
    
def add_numero():
    while True:
        try: 
            numero = int(input("Digite um número: "))
        except (ValueError, TypeError):
            print("Erro no dado digitado, digite um número válido.")
            logging.error("Erro no dado digitado, digite um número válido.")
            return
        print(numero)  
add_numero()