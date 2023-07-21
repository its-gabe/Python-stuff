#Desafio Sistema bancário da DIO


extrato = []
saldo = 0
LIMITE_SAQUE = 3
saques = 0

while True:
    menu = input("""
         MENU
    ===============

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [0] Sair

    ===============

Qual você deseja executar? 
""")
    
    if menu == '1':
        valor_a_depositar = float(input("Quantia a depositar: "))

        if valor_a_depositar < 0:
            print("Desculpe, não depositamos valor negativo")
        else:
            saldo += valor_a_depositar
            extrato.append(valor_a_depositar)

    elif menu == '2':
        valor_a_sacar = float(input("Quantia a sacar: "))
        
        if valor_a_sacar > saldo:
            print("Você não tem saldo suficiente para realizar esse saque")
        elif valor_a_sacar > 500:
            print("Você não pode realizar um saque maior que R$ 500.00")
        elif saques >= LIMITE_SAQUE:
            print("Atingiu o limite de saques diários!")
        elif valor_a_sacar <= saldo and valor_a_sacar <= 500:
            saldo -= valor_a_sacar
            extrato.append(-valor_a_sacar)
            saques += 1

    elif menu == '3':
        print("Não foram feitas movimentações na conta." if not extrato else extrato)
        print("Extrato:")
        for extratos in extrato:
            print(f"R$ {extratos}")
        print(f"\nSaldo atual: R$ {saldo}")
        break

    elif menu == '0':
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")