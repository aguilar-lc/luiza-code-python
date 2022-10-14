
### 5) Resolva estes problemas em Python, guardando os valores e seus resultados em
# variáveis diferentes.

## a. Calcule a área de um quadrado cujo lado seja 2 cm.
lado = 2
x = lado * 4
print (f'A área o quadrado é: {x}') 
#Resposta -> área do quadrado = 8


## b. Uma mala custa R$120,00. Esta recebeu 5% de desconto. Quanto você irá pagar por ela.
preco_mala = 120
desconto = 120 * 5 / 100
preco_final = preco_mala - desconto
print(f'O preço com desconto é: R${preco_final}')
#Resposta -> o valor pago será R$ 114,00.


# c. Um carro está viajando a uma velocidade média de 100 Km/h, o trecho de viagem
#será 200 Km. Quantas horas irá demorar a viagem.
velocidade = 100
trecho = 200
tempo = trecho / velocidade
print(f'O tempo gasto será de {tempo} horas') 
#Resposta -> A viagem irá demorar 2 horas.


# d. João tem 2 pirulitos, Maria 3 pirulitos e Sofia 1 pirulito. Calcule o total de pirulitos e
#sua média.
joao = 2
maria = 3
sofia = 1
total_pirulitos = joao + maria + sofia
media_pirulitos = total_pirulitos / 3
print(f'O total de pirulitos é {total_pirulitos} e a média é {media_pirulitos}') 
#Resposta -> o total de pirulitos é 6 a média dos pirulitos é 2


# e. Davi tem 13 anos e sua irmã tem 7 anos. Guarde na variável eh_mais_velho a
#verificação se a idade de Davi é maior que a idade de sua irmã.
idade_Davi = 7
idade_irma_Davi = 13
eh_mais_velho = idade_Davi > idade_irma_Davi
print(eh_mais_velho)
#Resposta = False, a idade de Davi não é maior que a idade de sua irmã.
