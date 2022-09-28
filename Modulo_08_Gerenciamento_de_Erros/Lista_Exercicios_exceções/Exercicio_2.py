
# 2. Faça um programa que calcule a divisão de dois números m e n e trate os casos em
# que n = 0.

import logging
from typing import Type

logging.basicConfig(level=logging.ERROR, filename="logging_users.log")

def numero_validate(n):
    if n == 0:
        raise ValueError("O denominador não deve ser igual a zero.")
    
def add_numero():
    while True:
        try: 
            m = int(input("Digite um número: "))
            n = int(input("Digite outro número: "))
            numero_validate(n)
        except ValueError:
            print("O denominador não deve ser igual a zero.")
            logging.error("O denominador não deve ser igual a zero.")
            return    
        print(f'A divisao entre {m} e {n} é igual a {m/n}')
add_numero()