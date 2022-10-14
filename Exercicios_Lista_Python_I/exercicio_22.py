
###22). Crie um script que leia 10 números inteiros positivos e que irá apresentar:
#● A lista dos valores lidos de forma ordenada.
#● Uma saída identificando o número, se o número é par e se é primo. Isto será feito
#separando por vírgulas: Por exemplo, se informou [1,2,3,6]. Iremos apresentar aqui:
#○ 1,ímpar,não é primo
#○ 2,par,é primo
#○ 3,ímpar,é primo
#○ 6,par,não é primo

numeros = [1,2,3,4,5,6,7,8,9,10]

def num_primo(num):
    if num == 2:
        return True

    for i in range(2, num):
        if num % 2 == 0:
            return False

    return True

def num_par(num):
    return True if num % 2 == 0 or num == 0 else False

def identificador_numero(numeros):
    for num in numeros:
        primo = num_primo(num)
        par = num_par(num)
        print(f"{num}, {'par' if par else 'não é par'}, {'é primo' if primo else 'não é primo'}")

identificador_numero(numeros)