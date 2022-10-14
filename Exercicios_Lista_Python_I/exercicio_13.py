
#### 13). Crie o seguinte programa Python: Colete a idade de 3 pessoas e
# mostre a média de suas idades.

soma = cont = 0
for i in range(0,3):
    idade = int(input('Digite sua idade: '))
    cont = cont + 1
    soma = soma + idade
media = soma/cont
print(f'A média das idades é {media}')
