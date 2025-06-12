# LOOP INFINITO PARA EXIBIR O MENU ATÉ O USUÁRIO ESCOLHER SAIR
while True: 
    # EXIBE O MENU DE OPÇÕES
    print("======= MENU DE OPÇÕES ======")
    print("[1] Somar dois numeros: ")
    print("[2] Subtrair dois numeros: ")
    print("[3] Sair: ") 

    # RECEBE A OPÇÃO DO USUÁRIO
    opcao = input("Escolha uma opção: ") 

    # SE A OPÇÃO FOR 1, FAZ A SOMA
    if opcao == "1" : 
        number1 = int(input("Escreva o primeiro numero: "))  # RECEBE O PRIMEIRO NÚMERO
        number2 = int(input("Escreva o segundo numero: "))   # RECEBE O SEGUNDO NÚMERO
        print(f"{number1} + {number2} = {number1 + number2}") # MOSTRA O RESULTADO

    # SE A OPÇÃO FOR 2, FAZ A SUBTRAÇÃO
    elif opcao == "2" : 
        number1 = int(input("Escreva o primeiro numero: "))
        number2 = int(input("Escreva o segundo numero: ")) 
        print(f"{number1} - {number2} = {number1 - number2}") 

    # SE A OPÇÃO FOR 3, ENCERRA O PROGRAMA
    elif opcao == "3" : 
        print("Programa finalizado!") 
        break 

    # CASO A OPÇÃO SEJA INVÁLIDA
    else : 
        print("Opção Invalida!") 

       