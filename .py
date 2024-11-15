def menu():
    print("\nSistema Bancário")
    print("d. Depositar")
    print("s. Sacar")
    print("e. Extrato")
    print("q. Sair")

def sistema_bancario():
    # Variáveis globais
    saldo = 0
    limite = 500
    extrato = ""
    numeros_saques = 0
    LIMITE_SAQUES = 3

    def Depositar(saldo, extrato):
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Valor de R${valor} depositados na conta")
        else:
            print("Valor inválido!")
        return saldo, extrato

    def Sacar(saldo, extrato, numeros_saques, LIMITE_SAQUES, limite):
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numeros_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numeros_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")
        return saldo, extrato, numeros_saques

    def Extrato(saldo, extrato):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    # Loop principal do sistema de gerenciamento
    while True:
        menu()
        opcao = input("Escolha uma opção: ").lower()

        if opcao == "d":
            saldo, extrato = Depositar(saldo, extrato)
        elif opcao == "s":
            saldo, extrato, numeros_saques = Sacar(saldo, extrato, numeros_saques, LIMITE_SAQUES, limite)
        elif opcao == "e":
            Extrato(saldo, extrato)
        elif opcao == "q":
            print("Saindo do sistema")
            break
        else:
            print("Opção Inválida. Tente novamente!")

# Inicializa o sistema
sistema_bancario()

