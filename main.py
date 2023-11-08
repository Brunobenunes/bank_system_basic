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


def deposit_system(balance, extract: list):
    amount_deposit = float(input('Qual o valor você deseja DEPOISTAR?: '))
    new_balance = 0
    if (amount_deposit > 0):
            print('Depositando...')
            new_balance = balance + amount_deposit
            print('DEPOSITO efetuado com SUCESSO!')
            extract.append(f'DEPOSITO: R$ {amount_deposit:.2f}')
            return new_balance
    else:
        print('Falha no Deposito. Insira valores Positivos')
        return new_balance
    
def withdraw_system(**kwargs):
    extract : list = kwargs['extract']
    balance = kwargs['balance']
    amount_withdraw = kwargs['amount_withdraw']
    new_balance = balance

    if (amount_withdraw <= balance):
        print('Sacando....')
            
        new_balance -= amount_withdraw
        print()
        print(f'Saque realizado com SUCESSO, saldo atual: {new_balance:.2f}')
        extract.append(f'SAQUE: R$ -{amount_withdraw}')
        return new_balance, extract
        
    else:
        print('Sacando....')
        print()
        print(f'NÂO possível realizar o SAQUE por falta de saldo. Seu saldo Atual : {balance:.2f}')
        return new_balance, extract

while True:
    command = input(menu)

    if (command == 's'):
        if (count_withdraws == DAILY_WITHDRAW):
            print('Você já atingiu o seu limite máximo de saque DIÁRIO')
            continue

        amount_withdraw = float(input('Quanto deseja sacar?: '))
        
        if (amount_withdraw < 0):
            print('Falha no Saque, insira um valor POSITIVO')
            continue
        
        elif (amount_withdraw > MAX_WITHDRAW):
            print(f'Falha no Saque. O valor máximo para SAQUE é de R${MAX_WITHDRAW:.2f}')
            continue

        elif (amount_withdraw <= balance):
            balance, extract = withdraw_system(balance=balance, extract=extract, amount_withdraw=amount_withdraw)
            count_withdraws += 1
            print(count_withdraws)
            continue

    elif(command == 'd'):
        balance += deposit_system(balance, extract)
        continue
    
    if (command == 'e'):
        extract_system(extract)
        continue

    if (command == 'q'):
        print('Saindo...')
        print()
        print('Tenha um ótimo Dia')
        break

    else:
        print('Insira um comando válido')
        continue