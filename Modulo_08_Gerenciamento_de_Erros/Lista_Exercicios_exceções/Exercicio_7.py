
# 7. Uma colega tentou executar o seguinte programa:

#file = open("file.txt", "r")
# file_lines = file.readline()
# file.close()

#Traceback (most recent call last):
 # File "c:/Users/Usuario/Documents/LuizaCode/Luiza_Code_Git/luiza-code-python/Modulo_08_Gerenciamento_de_Erros/Lista_Exercicios/Exercicio_8.py", line 4, in <module>
    #file = open("file.txt", "r")
#FileNotFoundError: [Errno 2] No such file or directory: 'file.txt'

# Reescreva o código para que esse erro seja exibido de forma mais clara e migável.

import logging

logging.basicConfig(level=logging.ERROR, filename="logging_users.log")
    
def file():
    try:
        file = open("file.txt" "r")
        file_lines = file.readline()
        file.close()
    except FileNotFoundError:
        print("Arquivo não encontrado no diretório")
file()