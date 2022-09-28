
# 4. Observe o seguinte programa:

#number = int(input("Digite um número: "))
#print("O número digitado foi:", n)

# Tendo em mente que ao executá-lo a exceção NameError é gerada, reescreve o 
# código de forma com que tal exceção seja tratada.

import logging

logging.basicConfig(level=logging.ERROR, filename="logging_users.log")

def add_numero():
    while True:
        try: 
            number = int(input("Digite um número: "))
            logging.info(number)
            print(f"O número digitado foi: {n}")
        except NameError:
            logging.error("Correção da variável")
        except ValueError:
            print("Erro no tipo de dado: digite um número")
            logging.error("Erro no tipo de dado: digite um número")
add_numero()
    
    