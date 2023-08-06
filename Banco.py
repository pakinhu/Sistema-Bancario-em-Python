
menu = """

[a] Depositar
[b] Sacar
[c] Extrato
[d] Sair

>= """
saldo = 0
limite = 500
extrato = ""
numero_saques = 1
LIMITE_SAQUES = 3

while True:

    opcao = input(menu).lower()

    if opcao == "a":
        try:
            valor = float(input("Informe o valor do depósito: "))

            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
            else:
                print("Valor informado é inválido")
        except ValueError:
            print("Erro: Valor do depósito inválido. Certifique-se de digitar um número válido.")

    
    elif opcao == "b" :
        try:
            valor = float(input("Informe o valor de saque: "))

            if saldo >= valor and numero_saques <= LIMITE_SAQUES  and valor <= limite and valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
                        
            elif saldo < valor:
                print("==================\nSaldo insuficiente\n==================")
            
            elif numero_saques > 3:
                print("=======================\nNúmero de saques excedidos\n=======================")

            elif valor > limite:
                print("=========Valor inválido========\nValor máximo por saque R$500.00")
                
            elif valor < 0:
                print("============Valor inválido==============.")
         
      
        except ValueError:
            print("Erro: Valor de saque inválido. Certifique-se de digitar um número válido.")
        
    
    elif opcao == "c" :
        print("=============EXTRATO==============")
        print("NÃO FORAM REALIZADAS MOVIMENTAÇÕES" if not extrato else extrato)
        print(f"" if saldo <= 0 else f"Saldo: {saldo:.2f}")
        print("==================================")

    elif opcao == "d":
        print("VOLTE SEMPRE!")
        break

    else:
        print("Opção inválida")
