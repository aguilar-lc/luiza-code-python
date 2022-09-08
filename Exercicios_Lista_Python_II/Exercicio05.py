# Escreva uma classe “Quadrado”, crie dois métodos que retornem a área do quadrado e o perímetro, 
# não crie a instância nesse exercício.

class Quadrado():

    def __init__(self, lado):
        self.__lado = lado

    def mostra_area(self):
        return self.__lado ** 2

    def mostra_perimetro(self):
        return self.__lado * 4