#Classe

class Amigos_Hawkins:
    def __init__(self, personagem, apelido, interprete):
        self.personagem = personagem
        self.apelido = apelido
        self.interprete = interprete
        
    def mostrar_descricao(self):
        print(f'O nome do personagem é {self.personagem}, também conhecido(a) como: {self.apelido}')
        print(f'Interpretado(a) por... -> {self.interprete}')
        print()

amigo1 = Amigos_Hawkins('Onze', 'On','Millie Bobby Brown').mostrar_descricao()
amigo2 = Amigos_Hawkins('Michael Wheeler', 'Mike','Finn Wolfhard').mostrar_descricao()
amigo3 = Amigos_Hawkins('Dustin Henderson', 'Nerd','Gaten Matarazzo').mostrar_descricao()
amigo4 = Amigos_Hawkins('William Byers', 'Will',' Noah Schnapp').mostrar_descricao()
amigo5 = Amigos_Hawkins('Lucas Sinclair', 'Ranger','Caleb McLaughlin').mostrar_descricao()
amigo6 = Amigos_Hawkins('Maxine Mayfield', 'Max','Sadie Sink').mostrar_descricao()

#O nome do personagem é Michael Wheeler, também conhecido(a) como: Mike
#Interpretado(a) por... -> Finn Wolfhard

#O nome do personagem é Dustin Henderson, também conhecido(a) como: Nerd
#Interpretado(a) por... -> Gaten Matarazzo

#O nome do personagem é William Byers, também conhecido(a) como: Will
#Interpretado(a) por... ->  Noah Schnapp

#O nome do personagem é Lucas Sinclair, também conhecido(a) como: Ranger
#Interpretado(a) por... -> Caleb McLaughlin

#O nome do personagem é Maxine Mayfield, também conhecido(a) como: Max
#Interpretado(a) por... -> Sadie Sink