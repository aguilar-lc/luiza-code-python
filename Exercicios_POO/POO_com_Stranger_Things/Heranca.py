#Herança

class Amigos_Hawkins:
    
    def __init__(self, personagem, apelido, interprete):
        self.personagem = personagem
        self.apelido = apelido
        self.interprete = interprete
        
    def mostrar_descricao(self):
        print(f'O nome do personagem é {self.personagem}, também conhecido(a) como: {self.apelido}')
        print(f'Interpretado(a) por... -> {self.interprete}')
        print()
    
class Onze(Amigos_Hawkins):
    
    def __init__(self, personagem, apelido, interprete, pensamento):
      self.pensamento = pensamento
      
      super().__init__(personagem, apelido, interprete)
    
    def mostrar_pensamento(self):
        if self.pensamento == 'Eleven':
            return 'Amigos não mentem.'
    
eleven = Onze('Onze', 'On', 'Millie Bobby Brown','Eleven')
print(eleven.mostrar_pensamento())