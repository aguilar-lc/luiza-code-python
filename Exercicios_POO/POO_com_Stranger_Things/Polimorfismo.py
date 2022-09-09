import time

class Vecna:
    def __init__(self, nome):
        self.nome = nome
            
    def descricao_001(self):
        return 'Antes de se tranformar no Vecna, era o {self.nome} do laboratório de Hawkins'

class transformacao(Vecna):
    def __init__(self,nome, novo_nome):
        self.novo_nome = novo_nome
        super().__init__(nome)
        
    def transformacao_vecna(self):
        print(f'{self.nome} provoca um massacre no laboratório...')
        time.sleep(2)
        print(f'{self.nome} é detido por Eleven, que acaba abrindo o portal para o Mundo Invertido e o empurra para lá...')
        time.sleep(4)
        print(f'Ao cair, {self.nome} é queimado por um raio e se transforma em {self.novo_nome}.')

vecna = transformacao('001', 'Vecna').transformacao_vecna()