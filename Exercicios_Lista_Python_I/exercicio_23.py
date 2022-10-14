
#23) Neste script você irá ler o nome de 4 alunos e suas notas e determinar qual
#aluno possui a maior nota.

menor = maior = 0
aluno = []
for i in range(0,4):
    aluno.append(input("Nome do aluno: "))
    aluno.append(input("Nota do aluno: "))
    if i == 0:
        maior = menor = aluno[i]
    else:
        if aluno[i] > maior:
            maior = aluno[i]
        if aluno[i] < menor:
            menor = aluno[i]
print(f'Os nomes e notas informados foram: {aluno}')
print(f'O aluno(a) com maior nota foi: {maior}')