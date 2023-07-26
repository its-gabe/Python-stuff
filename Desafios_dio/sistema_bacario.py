#Desafio Sistema bancário da DIO
import textwrap

extratos = ""
saldo = 0
LIMITE_SAQUE = 3
saques = 0
usuarios = []
contas = []
AGENCIA = "0001"

def menu():
    menu = """
         MENU
    ===============

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Criar usuário
    [5] Criar conta
    [6] Listar contas
    [0] Sair

    ===============

Qual você deseja executar? 
"""
    return input(menu)
    

def depositar(saldo, valor, extrato, /):
    if valor_a_depositar < 0:
            print("Desculpe, não depositamos valor negativo")
    saldo += valor
    extrato += f"\nValor depositado de: R$: {valor:.2f}"

    return saldo, extrato  


def saque(*, saldo, valor, extrato, numero_saques, limite_saques):
    if valor > saldo:
        print("Você não tem saldo suficiente para realizar esse saque")
    elif valor > 500:
        print("Você não pode realizar um saque maior que R$ 500.00")
    elif numero_saques >= limite_saques:
        print("Atingiu o limite de saques diários!")
    elif valor <= saldo and valor <= 500:
        saldo -= valor
        extrato += f"\nValor sacado de R$: -{valor:.2f}"
        numero_saques += 1
    return saldo, extrato, numero_saques


def extrato(saldo, /, *, extrato):
    print("\nExtrato:")
    print("Não foram feitas movimentações na conta." if not extrato else extrato)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    return saldo, extrato


def criar_usuario(usuarios):
    cpf = input("Digite o seu cpf: ")
    usuario = filtrar_usuarios(cpf, usuarios)
    if usuario:
        print("Esse usuário ja existe!")
        return
    
    nome = input("Informe o seu nome completo: ")
    data_nascimento = input("Informe a sua data de nascimento (no formato dd/mm/aaaa): ")
    endereco = input("Informe seu endereço (no formato logradouro, nro - bairro - cidade/estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("\nUsuário criado com sucesso!")


def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe seu cpf de usuario: ")
    usuario = filtrar_usuarios(cpf, usuarios)
    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\nO usuario ainda nao foi criado!")


def listar_contas(contas):
    for conta in contas:
        usuario = conta['usuario']['nome']
        agencia = AGENCIA
        n_conta = conta['numero_conta']
        
        linha = f"""\n========================================================
Usuário: {usuario}
Agencia: {agencia}
Numero da conta: {n_conta}
========================================================"""
        print(textwrap.dedent(linha))
    

while True:
    opcao = menu()
    
    if opcao == '1':
        valor_a_depositar = float(input("Quantia a depositar: "))
        saldo, extratos = depositar(saldo, valor_a_depositar, extratos)
        

    elif opcao == '2':
        valor_a_sacar = float(input("Quantia a sacar: "))
        saldo, extratos, saques = saque(saldo=saldo, valor=valor_a_sacar, extrato=extratos, numero_saques=saques, limite_saques=LIMITE_SAQUE)
        

    elif opcao == '3':
        saldo, extratos = extrato(saldo, extrato=extratos)
        break


    elif opcao == '4':
        criar_usuario(usuarios)


    elif opcao == '5':
        numero_contas = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_contas, usuarios)

        if conta:
            contas.append(conta)


    elif opcao == '6':
        if contas:
            listar_contas(contas)
        else:
            print("Nao ha nenhuma conta criada ainda!")


    elif opcao == '0':
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")