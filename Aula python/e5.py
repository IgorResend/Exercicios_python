saldo = 0

while True:
    print("\n1 - Saque")
    print("2 - Depósito")
    print("3 - Transferência")
    print("4 - Saldo")
    print("0 - Sair")
    opcao = int(input("Escolha a operação: "))

    if opcao == 1:
        qsaque = float(input("Insira a quantia do saque: "))
        if qsaque <= saldo:
            saldo -= qsaque
            print(f"Saque de R${qsaque:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente.")
    
    elif opcao == 2:
        qdeposito = float(input("Insira a quantia do depósito: "))
        saldo += qdeposito
        print(f"Depósito de R${qdeposito:.2f} realizado com sucesso.")
    
    elif opcao == 3:
        qtrans = float(input("Insira a quantia da transferência: "))
        if qtrans <= saldo:
            saldo -= qtrans
            print(f"Transferência de R${qtrans:.2f} realizada com sucesso.")
        else:
            print("Saldo insuficiente.")
    
    elif opcao == 4:
        print(f"Seu saldo é: R${saldo:.2f}")
    
    elif opcao == 0:
        print("Saindo...")
        break
    
    else:
        print("Opção inválida. Tente novamente.")
