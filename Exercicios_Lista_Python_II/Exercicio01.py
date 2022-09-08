# Dada as seguintes informações: pessoa, cpf, nome e idade, crie uma classe onde teremos o retorno
# do documento, o retorno do nome e verificação de tipo de pessoa, onde um método irá receber como
# parâmetro "F" ou "N" para trazer fumante ou não fumente. Feito isso, crie uma instância e retorne 
# esses valores.

class Pessoa:
    def __init__(self, nome, idade, cpf, tipo):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.tipo = tipo
    
    def descricao(self):
        if self.tipo == 'F':
            print(f'{self.nome} tem {self.idade} anos, seu cpf é {self.cpf} e é fumante')
        if self.tipo == 'N':
            print(f'{self.nome} tem {self.idade} anos, seu cpf é {self.cpf} e não é fumante')
        
pessoa1 = Pessoa('João', '30', '123456789', 'N').descricao()