menu = '''

    ## Bank DIO System ##

    [s] Sacar
    [d] Depositar
    [e] Extrato
    [q] Sair

    #####################

'''

DAILY_WITHDRAW = 3
count_withdraws = 0
MAX_WITHDRAW = 500
balance = 0
extract = []

def extract_system(list_extract):
    print('Extrato'.center(10, '#'))
    for operation in list_extract:
        print(operation)
    print(f'##### Saldo Atual: R$ {balance:.2f}')


while True:
    command = input(menu)

    if (command == 's'):
        if (count_withdraws == DAILY_WITHDRAW):
            print('Você já atingiu o seu limite máximo de saque DIÁRIO')
            continue

        amount_withdraw = float(input('Quanto deseja sacar?: '))

        if (amount_withdraw <= balance):
            print('Sacando....')
            if (amount_withdraw < 0):
                print('Falha no Saque, insira um valor POSITIVO')
                continue
            elif (amount_withdraw > MAX_WITHDRAW):
                print(f'Falha no Saque. O valor máximo para SAQUE é de R${MAX_WITHDRAW:.2f}')
                continue

            balance -= amount_withdraw
            print()
            print(f'Saque realizado com SUCESSO, saldo atual: {balance:.2f}')
            extract.append(f'SAQUE: R$ -{amount_withdraw}')
            count_withdraws += 1
            
        
        else:
            print('Sacando....')
            print()
            print(f'NÂO possível realizar o SAQUE por falta de saldo. Seu saldo Atual : {balance:.2f}')
            continue
    
    elif(command == 'd'):
        amount_depoist = float(input('Qual o valor você deseja DEPOISTAR?: '))
        if (amount_depoist > 0):
            print('Depositando...')
            balance += amount_depoist
            print('DEPOSITO efetuado com SUCESSO!')
            extract.append(f'DEPOSITO: R$ {amount_depoist:.2f}')
            continue
    
    elif(command == 'e'):
        ...
    
    elif(command == 'q'):
        break
    
    else:
        continue