
# Exercícios 1 - Crie um sistema de cadastro de pessoas pelo nome e idade. O sistema deve ter as seguintes opções:
# 1 - Cadastrar pessoas
# 2 - Listar pessoas
# 3 - Sair

users = []

def user_add():
    name = input("Digite o nome do usuário: ")
    age = input("Digite a idade do usuário: ")
    
    users.append({"name": name, "age": age})
    
    print("\nUsuário cadastrado com sucesso!")
    
def users_list():
    print("\n")
    for user in users:
        print("{} - {} anos".format(user["name"], user["age"]))

while True:
    option = int(input("\nDigite a opção desejada:\n 1 - Cadastrar pessoas\n 2 - Listar pessoas\n 3 - Sair\n"))
    
    if option == 1:
        user_add()
    elif option == 2:
        users_list()
    elif option == 3:
        exit()
    else:
        print("Opção inválida!")