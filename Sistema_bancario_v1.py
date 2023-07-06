menu = """
========= Menu =========

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

========================\n
"""

saldo = 0 
deposito = 0
extrato = ""
quantidade_de_saque = 0 # variavel para contar quantidade de saques realizados no programa

while True:
    
      opcao = int(input(menu)) # Menu para selecionar as operações

      if opcao == 1:

            deposito_palavra = "Deposito"
            print(deposito_palavra.center(51, "="))

            deposito = float(input("\nInforme o valor desejado para depósito:     ")) # Solicita o valor do deposito ao usuario e adiciona na variavel deposito
            saldo += deposito # Adiciona o valor depositado ao saldo da conta
            extrato += f"\nDepósito realizado no valor de:     R$ {deposito:.2f}\n" # Registra as informações sobre os depositos realizados na variavel string

      elif opcao == 2:

            saque_palavra = "Saque"
            print(saque_palavra.center(51, "="))

            saque = float(input("\nInforme a quantia até R$ 500 que deseja sacar: ")) # Solicita o valor do saqueao usuario e adiciona na variavel saque

            if saque > 500: 
                  print("Não foi possível realizar o saque. O limite máximo para saque é de R$ 500") # Se o saque solicitado for maior que 500 aparecerá esta mensagem
            elif saque > saldo:
                  print("Não será possível sacar o dinheiro por falta de saldo.") # Se o saque solicitado for maior que o saldo aparecerá esta mensagem
            elif quantidade_de_saque < 3:

                  quantidade_de_saque += 1 # Será adicionado +1 à variavel quantidade_de_saque toda vez que uma saque for realizado
                  saldo -= saque # Será descontado do saldo atual o saque solicitado 
                  extrato += f"\nSaque realizado no valor de:     R$ {saque:.2f}\n" # Registra as informações sobre os saques realizados na variavel string

            else:
                  print("\nNão é possível realizar mais do que 3 saques no dia!") # Caso ultrapasse a quantidade de saques permitidos será mostrado essa frase

      elif opcao == 3:

            extrato_palavra = "Extrato" # Variavel com palavra extrato para usar a função center

            if extrato == "" :

                  print(extrato_palavra.center(51, "=")) # Uso da função center para criar um menu para o extrato
                  print("\nNão foram realizadas movimentações.\n") # Caso a variavel esteja vazia mostrará esta mensagem
                  print("===================================================\n")

            else:

                  print(extrato_palavra.center(51, "=")) # Uso da função center para criar um menu para o extrato
                  print()
                  print(extrato) # Mostra o extrato atual da conta
                  print(f"Saldo total: R$ {saldo:.2f}\n") # Mostra o saldo atual da conta
                  print("===================================================\n")

      elif opcao == 0:
            break # Caso o usuario escolha a opção sair(0) o programa acaba

      else:
             print("Opção inválida, por favor selecione novamente a operação desejada")


