from tecateca import soma, divisao, subtracao, multiplicacao

mensagem = '''OPERAÇÕES BÁSIAS
    1- SOMA
    2- SUBTRAÇÃO
    3- DIVISÃO
    4- MULTIPLICAÇÃO
    
    "s" para sair
    
    OPÇÃO: '''
while True:
    opcao = input(mensagem)
    if opcao == 's':
        print('FINALIZADO')
        break

    num1 = int(input("Digite um número: "))
    num2 = int(input('Digite outro número: '))



    if opcao == '1':
        soma(num1, num2)
    elif opcao == '2':
        subtracao(num1, num2)
    elif opcao == '3':
        divisao(num1, num2)
    elif opcao == '4':
        multiplicacao(num1, num2)
    else:
        print("Opção invalida")
