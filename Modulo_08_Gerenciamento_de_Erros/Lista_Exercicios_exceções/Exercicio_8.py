
# 8. Observe o seguinte programa:

#try:
#  file = open("file.txt", "r")
#  file.write("Exemplo de texto.")
#except IOError:
#    print("Não foi possível escrever o arquivo")

# Um dos problemas do código acima é que o mesmo além de possuir um erro lógico 
# execução de um comando de escrita em um arquivo em modo de leitura), abre um
# arquivo e tem a sua execução encerrada sem realizar o close.
# Incremente o código apresentado liberando da memória a referência do arquivo
# tanto nos casos de erro, quanto em execuções bem sucedidas (caso o mesmo fosse
# aberto em modo de escrita).
 
def file():
    try:
        file = open("file.txt", "r")
        file.write("Exemplo de texto.")
        print("Arquivo escrito.")
    except IOError:
         print("Não foi possível escrever o arquivo, abra-o em modo de escrita -> 'w'.")
    finally: 
        file.close()
        print("Arquivo fechado.")
        return 
file()

