
# Exercício 1. Faça um programa que calcule a raiz quadrada de um número n e trate os casos 
# em que n < 0.
# OBS: Utilize o módulo math para calcular a raiz quadrada.

import logging
from typing import Type
import math

logging.basicConfig(level=logging.ERROR, filename="logging_users.log")

def numero_validate(numero):
    if numero < 0 or numero == 0:
        raise ValueError("O número deve ser maior que zero")
    
def add_numero():
    while True:
        try: 
            numero = int(input("Digite um número: "))
            numero_validate(numero)
        except ValueError:
            print("O número deve ser maior que zero")
            logging.error("O número deve ser maior que zero")
            return    
        print(f'A raiz quadrada de {numero} é {math.sqrt(numero)}')
add_numero()
