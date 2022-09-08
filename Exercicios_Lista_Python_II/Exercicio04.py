# Crie um professor de classe com atributos nome, idade e salário, onde o salário deve 
# ter um método privado que não pode ser acessado fora da classe. Crie um método para acessar 
# o método privado, onde é passada a identificação do usuário se ele pode ou não acessar.

class Professor:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def __salario(self):
        return f'O salário é R$2000,00'
    
    def busca_salario_se_esponsavel(self, nome):
        if nome == 'Pedro':
            return self.__salario()
            
professor1 = Professor('Pedro', '40').busca_salario_se_esponsavel('Pedro')
print(professor1)

professor2 = Professor('João', '32').__salario()
print(professor2)