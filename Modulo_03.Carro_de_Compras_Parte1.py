cart = []
for i in range(3):
    id_user = input("Insira o ID do usuário: ")
    id_product = input("Insira o ID do produto: ")
    price_product = float(input("Insira o preço do produto: R$ "))
    quantity_product = int(input("Insira a quantidade do produto: "))

    item = [id_user, id_product, price_product, quantity_product]

    def add_item_cart():
        cart.append(item)
        print(f'Item inserido no carrinho: {item}')
        print('-'*60)
    add_item_cart()

def get_all_item_cart():
    print(f'Todos os itens do carrinho: {cart}')
    print('-'*60)
get_all_item_cart()

def get_item_cart_by_id(id_product):
    for i in cart:
        if i[1] == id_product:
            print(f'O id_product -> {i[1]} <- corresponde ao item -> {i} <- do carrinho.')
            print('-'*60)        
get_item_cart_by_id(id_product)

def get_item_cart_by_product_id(id_product):
    new_list = [item for item in cart if item[1] == id_product]
    return new_list[0]
get_item_cart_by_product_id(id_product)
print(item)