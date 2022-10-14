
#21. O pessoal da empresa Caça-Clientes trabalha com ligações para números aleatórios.
#Eles recebem uma lista com vários intervalos de números para eles ligarem. Na lista
#recebida, você tem o prefixo do telefone, o primeiro sufixo e o último sufixo. Crie um script
#que liste todos os números dos telefones, ao serem informados, o prefixo e os sufixos. Por
#exemplo, suponha que o prefixo seja “3232” e que o primeiro prefixo seja “0001” e o último
#sufixo seja “0005”; logo o programa irá imprimir:
#Seus números de telefone são:
#● 3232-0001
#● 3232-0002
#● 3232-0003
#● 3232-0004
#● 3232-0005

def telefones(lista):
    prefixo = lista[0]
    primeiro_sufixo = int(lista[1])
    ultimo_sufixo = int(lista[2])
    lista_sufixos = []
    lista_telefones = []

    for i in range(int(primeiro_sufixo), int(ultimo_sufixo+1)):
        numero = i
        str_numero = str(numero)
        while len(str_numero) < 4:
            str_numero = "0"+str_numero
        lista_sufixos.append(str_numero)
    print(lista_sufixos)

    for i in range(len(lista_sufixos)):
        lista_telefones.append(f"{prefixo}-{lista_sufixos[i]}")

    print(lista_telefones)


telefones(['3232', '0001', '0005'])
telefones(['3232', '0012', '0032'])
telefones(['3232', '0120', '0129'])
telefones(['3232', '1100', '1115'])