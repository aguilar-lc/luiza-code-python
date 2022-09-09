#Encapsulamento

class Clube_Hellfire:
    def __init__(self, fundador):
        self.fundador = fundador
    
    def mostrar_fundador(self):
        return 'Eddie Munson'
    
    def __mostrar_acesso_clube(self):
        return "Você é um membro, pode entrar!"

    def acessar_clube(self, membro):
        if membro == "Dustin":
            return self.__mostrar_acesso_clube()
        
        return "Voce não é um membro e não tem acesso!"
    
membro = Clube_Hellfire(['Eddie Munson'])

acesso = membro.acessar_clube("Dustin")
print(acesso)

acesso = membro.acessar_clube("Max")
print(acesso)