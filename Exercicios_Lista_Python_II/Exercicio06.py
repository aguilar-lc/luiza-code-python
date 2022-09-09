# Crie um arquivo main.py, importe a classe “Quadrado”, crie uma nova instância e acesse seus métodos

from Exercicio05 import Quadrado


def main():
    quadrado = Quadrado(5)

    print(f"A área do quadrado é: {quadrado.mostra_area()}m²")
    print(f"O perímetro do quadrado é: {quadrado.mostra_perimetro()}m")


if __name__ == "__main__":
    main()