import random
def cadastrar_clientes():
    nome = input("Digite o nome do Cliente: ")
    email = input("Digite seu email: ")
    telefone = input("Digite o telefone:")
    return {"nome": nome, "email": email, "telefone": telefone}


cadastro_clientes = []


while True:
    print("\nCadastro de Clientes PADARIA")
    print("1 - Cadastrar Cliente")
    print("2 - Listar Clientes cadastrados")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        novo_cliente = cadastrar_clientes()
        cadastro_clientes.append(novo_cliente)
        print("Cliente cadastrado com sucesso.")
    elif opcao == "2":
        if cadastro_clientes:
            for i, cliente in enumerate(cadastro_clientes, start=1):
                print(f"\nCliente {i}:")
                print(f"Nome: {cliente['nome']}")
                print(f"Idade: {cliente['email']}")
                print(f"Notas: {cliente['telefone']}")
        else:
            print("Não há clientes cadastrados.")
    elif opcao == "0":
            cliente_sorteado = random.choices(cadastro_clientes)
            print(cadastro_clientes)
            print("O cliente sorteado foi:",cliente_sorteado, "ganhou um pão dormido....")
            break
    else:
        print("Opção inválida. Tente novamente.")

print("\nPrograma finalizado.")