
### 19). Um vendedor ganha uma comissão de uma venda da seguinte forma: Se a venda for …
#● menor que R$1000,00, o vendedor não ganha nenhuma comissão;
#● entre R$1.000,00 e R$5.000,00, o vendedor ganha uma comissão de 10% da venda;
#● entre R$5.000,00 e R$10.000,00, a comissão será de 20% da venda;
#● entre R$10.000,00 e R$50.000,00 a comissão será de 25% da venda;
#● acima de R$50.000,00 a comissão será de 30% da venda.

#Faça um programa que informe o valor da comissão do vendedor para uma venda.

valor_venda = float(input("Digite o valor da venda:R$ "))
if valor_venda < 1000:
    print('O valor da comissão para essa venda será de R$0,00.')
elif valor_venda >= 1000 and valor_venda < 5000:
    comissao = valor_venda * 10/100
    print(f'O valor da comissão para essa venda será de: R${comissao:.2f}')
elif valor_venda >= 5000 and valor_venda < 10000:
    comissao = valor_venda * 20/100
    print(f'O valor da comissão para essa venda será de: R${comissao:.2f}')
elif valor_venda >= 10000 and valor_venda < 50000:
    comissao = valor_venda * 25/100
    print(f'O valor da comissão para essa venda será de: R${comissao:.2f}')
elif valor_venda >= 50000:
    comissao = valor_venda * 30/100
    print(f'O valor da comissão para essa venda será de: R${comissao:.2f}')
    