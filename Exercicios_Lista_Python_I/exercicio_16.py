
### 16). Programa: Estou tentando entender os juros do meu banco. Para isto, ele me
# informou esta fórmula:
# valor_final = valor_emprestimo + (valor_emprestimo * taxa * tempo)
# onde:
# ● valor_emprestimo: É o valor que pegarei emprestado.
# ● taxa: É o valor da taxa por mês. Por exemplo: se for 4% ao mês, o valor será 0.04.
# ● tempo: Quantidade de meses que irei pagar o empréstimo.
# Crie um programa que colete cada um destes valores para calcular o valor final que estarei
# pagando ao banco.

valor_emprestimo = float(input("Valor do empréstimo: R$ "))
taxa = float(input("Valor da taxa: "))
tempo = int(input("Quantidade de meses: "))

valor_final = valor_emprestimo + (valor_emprestimo * taxa * tempo)
print(f'O valor a ser pago será: R${valor_final}')