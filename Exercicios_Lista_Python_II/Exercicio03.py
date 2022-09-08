# Escreva uma classe “PessoaJurica” e herde Pessoa(classe do exercício01), agora modificando 
# o comportamento, retorne o cnpj, crie uma instância e acesse os dados.

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

class PessoaJuridica(Pessoa):
    def __init__(self, nome, idade, cpf, tipo, cnpj):
      self.cnpj = cnpj
      
      super().__init__(nome, idade, cpf, tipo)
    
    def Mostrar_cnpj(self):
        print(f' O CNPJ é {self.cnpj}')
    
pessoajuridica = PessoaJuridica('João', '30', '123456789', 'N', '1987654321/0001').Mostrar_cnpj()