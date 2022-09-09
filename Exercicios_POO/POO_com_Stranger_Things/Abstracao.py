#Abstração

class Mundo_Invertido:
    def __init__(self, habilidade, pessoa, local):
        self.habilidade = habilidade
        self.pessoa = pessoa
        self.local = local

    def resgate_do_mundoinvertido(self):
        mensagem = f"Para {self.habilidade}, {self.pessoa}, "
        mensagem +='revela a localização de Onze para Brenner em troca do acesso ao portal. '
        mensagem += 'Juntamente com Joyce, Hopper entra no mundo invertido, ' 
        return mensagem + f"encontra o ninho do monstro na {self.local} onde will está e o resgata."
    
hopper = Mundo_Invertido('entrar no mundo invertido e salvar Will', 'Hopper', 'biblioteca da cidade')

# Voce nao precisa saber o que acontece por debaixo dos panos da função
print(hopper.resgate_do_mundoinvertido())