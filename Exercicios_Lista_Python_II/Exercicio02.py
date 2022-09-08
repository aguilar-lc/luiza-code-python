# Escreva uma classe “PessoaFisica” e herde Pessoa(classe do exercicio 01),
# crie um método exclusivo para a classe e acesse-o.

class Pessoa:
    def __init__(self, nome, idade, cpf, tipo):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.tipo = tipo
    
    def descricao(self):
        if self.tipo == 'F':
            print(f'{self.nome} tem {self.idade} anos, seu cpf é {self.cpf} e é fumante.')
        else:
            print(f'{self.nome} tem {self.idade} anos, seu cpf é {self.cpf} e é não é fumante.')

class PessoaFisica(Pessoa):
    def __init__(self, nome, idade, cpf, tipo, cidade):
      self.cidade = cidade
      
      super().__init__(nome, idade, cpf, tipo)
    
    def Mostrar_cidade(self):
        print(f' {self.nome} mora em {self.cidade}')
    
pessoafisica = PessoaFisica('João', '30', '123456789', 'N', 'Marília').Mostrar_cidade()