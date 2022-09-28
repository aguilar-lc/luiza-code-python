
# 6. Observe o seguinte programa:

try:
    number_1 = float(input("Insira um número: "))
    number_2 = float(input("Insira outro número: "))
    result = number_1 / number_2
    
    print("Resultado: {:.f}".format(resultado))
except ValueError:
    print("Isso não é um número")
except ZeroDivisionError:
    print("Divisão por 0 indeterminada.")
except:
    print("Algo deu errado.")
    
# Escreva o que será impresso na tela caso o mesmo seja executado com as seguintes entradas (5, 3):
# Insira um número: 5
# Insira outro número: 3

# Resposta: Será impresso na tela "Algo deu errado", pois o nome correto da variável no 
# primeiro print deveria ser "result" e não "resultado."
    