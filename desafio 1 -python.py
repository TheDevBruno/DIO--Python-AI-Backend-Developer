
menu = """
    ====== DIGITE SUA OPÇÃO ======

            [d] Depositar
            [s] Sacar
            [e] Extrato
            [q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("""
            
                    Operação falhou! Você não tem saldo suficiente.

                    Por favor, verifique seu saldo e refaça a operação.
            
            """)

        elif excedeu_limite:
            print("""   
            
                    Operação falhou! O valor do saque excede o limite.
                    O Valor limite por saque é de R$500,00.
                     
                """)

        elif excedeu_saques:
            print("""   
            
                    Operação falhou! Número máximo de saques excedido.
            
                    Você tem um limite de 3 saques diários.

                """)

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":

        print("""
                Obrigado por ter utilizado nosso terminal.
                
                Volte sempre!
        """)
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")