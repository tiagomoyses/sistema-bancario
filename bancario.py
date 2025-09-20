from decimal import Decimal, ROUND_HALF_UP

#Configurações iniciais
SAQUES_DIARIOS = 3
limite_saque_diario = Decimal("500.00")

#Estado da conta
numero_saques = 0
saldo = Decimal("0.00")
extrato = ""

#Menu de opções

while True:
        print(" \nMenu: \n[1]Depositar \n[2]Sacar \n[3]Ver Extrato \n[4]Sair: ")

        try:
            opcao = int(input("\n Digite a opção deseja: "))

        except ValueError:
            print("\n Por favor, digite uma opção válida.")
            continue
        

        if opcao == 1:
             valor = Decimal(input("\n digite o valor do deposito: "))
             if valor > 0:
                saldo+= valor
                extrato += f"\n Depósito: R$ {valor:.2f} "
                print("\n Depósito realizado com sucesso! ")
             else:
                print("\n Operação falhou! O valor informado é inválido. ")

        elif opcao == 2:
                if numero_saques == SAQUES_DIARIOS:
                     print("\n Número máximo de saques diários atingido. ")
                     continue
                
                valor = Decimal(input("\n Digite o valor do saque: "))

                #Por causa do input é necessário iniciar por outro if ao invés de elif

                if valor > limite_saque_diario:
                    print("\n O valor desejado excede o limite diário!")
                    continue
                
                elif valor > saldo:
                    print("\n Saldo insuficiente")
                    continue
        
                elif valor <=0:
                     print("\n Operação falhou! O valor informado é inválido.")
                     continue
                
                else:
                    saldo -= valor
                    limite_saque_diario -= valor
                    numero_saques += 1
                    extrato += f" \n Saque: R$ {valor:.2f}"
                    print("\n Saque realizado com sucesso!")

        elif opcao == 3:
                print("\n**********EXTRATO**********")
                if extrato == "":
                    print("\n Não foram realizadas movimentações.")
                else:
                    print(extrato)
                print(f"\n Saldo: R$ {saldo:.2f}")
                print("***************************")

        elif opcao == 4:
                print("\n Obrigado por usar nosso sistema bancário!\n")
                break
                    
                
        
             

                