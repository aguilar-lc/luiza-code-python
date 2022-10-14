class Big_Bang_Theory:
    def __init__(self, nome, profissao, frase):
        self.nome = nome
        self.profissao = profissao
        self.frase = frase
        
    def descricao(self):
        print(f'Sou {self.nome} e sou {self.profissao}.')
        
    def exibir_caracteristica(self):
        print(f'    -> {self.frase}')
        print()
        
personagem1 = Big_Bang_Theory('Sheldon Cooper', 'Físico Teórico',
                              'toc toc toc, Penny! toc toc toc, Penny! toc toc toc, Penny!')
personagem1.descricao()
personagem1.exibir_caracteristica()

personagem2 = Big_Bang_Theory('Leonard Hofstadter', 'Físico Experimental', 
                              'Não posso beber leite, sou intolerante a lactose.')
personagem2.descricao()
personagem2.exibir_caracteristica()

personagem3 = Big_Bang_Theory('Penny Hofstadter', 'Garçonete', 'Preciso de uma taça de vinho.')
personagem3.descricao()
personagem3.exibir_caracteristica()

personagem4 = Big_Bang_Theory('Howard Wolowitz', 'Engenheiro Espacial', 
                              'Não sei se ja disse.. Mas, já fui pro Espaço.')
personagem4.descricao()
personagem4.exibir_caracteristica()

personagem5 = Big_Bang_Theory('Rajesh Koothrappali', 'Astrofísico', 
                              'Como os vampiros se barbeiam, se não podem se ver no espelho?')
personagem5.descricao()
personagem5.exibir_caracteristica()

personagem6= Big_Bang_Theory('Bernadette Wolowitz', 'Microbiologista', 'Sou um doce...Hooowaard!!!')
personagem6.descricao()
personagem6.exibir_caracteristica()

personagem7 = Big_Bang_Theory('Amy Farrah Fowler ', 'Neurocientista', 
                              'Oh, é uma tiara! Eu tenho uma tiara!')
personagem7.descricao()
personagem7.exibir_caracteristica()