
#15). Para o programa Python: Em uma casa, uma família decidiu dividir
#o valor da conta de energia entre os moradores da casa. No programa eles informam o
#valor da conta de energia e quantos que irão pagar a conta no mês. O programa calculará
#quanto cada um deverá contribuir com a conta de energia.

conta = int(float("Digite o valor da conta: R$"))
quant_pessoas = int(input("Digite a quantidade de pessoas: "))
valor_por_pessoa = conta/quant_pessoas
print(f' Cada pessoa deverá para RS {valor_por_pessoa}')