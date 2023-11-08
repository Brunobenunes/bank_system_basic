from copy import deepcopy

menu_login = '''
########## Bank DIO ##########
     #### Bem Vindo(a) ####
     
     [e] Entrar
     [c] Cadastrar Usuário
     [q] Sair

'''

options_menu_display = '''
    ## Bank DIO System ##

    [c] Criar Conta-Corrente
    [a] Acessar Contas
    [q] Sair

    
'''

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

users = [
    {
        '02133622608': {
            'name': 'Bruno Benunes',
            'birth_year': 199,
            'adress': '',
            'accounts': ['1', '2'],
            'password': '123abc'
        }
    },
    {
        '123': {
            'name': 'Bruno Henrique',
            'birth_year': 1999,
            'adress': '',
            'accounts': ['3'],
            'password': '123'
        }
    }

]

accounts = [
    {
        '1': {
            'branch': 0o1,
            'user': '0213362608',
            'balance': 1000,
            'count_withdraws': 0,
            'MAX_WITHDRAW': 500,
            'extract': [],
            'DAILY_WITHDRAW': 3,
        },
    },
    {
        '2': {
            'branch': 0o1,
            'user': '0213362608',
            'balance': 5000,
            'count_withdraws': 0,
            'MAX_WITHDRAW': 500,
            'extract': [],
            'DAILY_WITHDRAW': 3,
        },
    },
    {
        '3': {
            'branch': 0o1,
            'user': '123',
            'balance': 50,
            'count_withdraws': 0,
            'MAX_WITHDRAW': 500,
            'extract': [],
            'DAILY_WITHDRAW': 3,
        }
    }
]

BASE_ACCOUNT = {
    'branch': 0o1,
    'balance': 50,
    'count_withdraws': 0,
    'MAX_WITHDRAW': 500,
    'extract': [],
    'DAILY_WITHDRAW': 3,
}

def create_user():
    cpf = input('Digite seu CPF: ')
    name = input('Digite seu NOME: *Nome e Sobrenome*: ')
    birth_year = int(input('Digite seu ano de Nascimento: '))
    street = input('Digite Seu endereço: *RUA e NUMERO e COMPLEMENTO*: ')
    district = input('Digite Seu Bairro: ')
    state = input('Digite Seu Estado: ')
    password = input('Digite sua SENHA: ')
    cpf_format = ''.join(cpf.split('.'))
    cpf = ''.join(cpf_format.split('-'))

    new_user = {
        cpf: {
            'name': name,
            'birth_year': birth_year,
            'adress': f'{street} - {district}/{state}',
            'password': password
        }
    }
    return new_user

def extract_system(balance, / , *, list_extract):
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

def transfer_operations(account_number):
        account = find_account_with_number(account_number)
        DAILY_WITHDRAW = account['DAILY_WITHDRAW']
        count_withdraws = account['count_withdraws']
        MAX_WITHDRAW = account['MAX_WITHDRAW']
        balance = account['balance']
        extract = account['extract']
        
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
                    print(balance)
                    continue

            elif(command == 'd'):
                balance = deposit_system(balance, extract)
                continue

            if (command == 'e'):
                extract_system(balance, list_extract=extract)
                continue

            if (command == 'q'):
                print('Saindo...')
                print()
                print('Tenha um ótimo Dia')
                break

            else:
                print('Insira um comando válido')
                continue

def find_account_with_number(account_number):
    for acc in accounts :
        if (list(acc.keys())[0] == account_number):
            return acc[account_number]

def check_user_login(user, password):
    for user_ in users:
        if (list(user_.keys())[0] == user):
            if (user_[user]['password'] == password):
                return True, user_[user]
            else:
                return False

def input_account_choice(user):
    account_options = []
    for index, acc in enumerate(user['accounts']):
        account_options.append(f'[{index + 1}]: {acc}')
    print('## Bank DIO System ##'.center(10, ' '))
    print(*account_options, sep='\n')
    print()
    return 'Sua Opção: '

def account_choice(user, account):
    return user['accounts'][int(account) - 1]

def options_menu(user):
    while True:
        command = input(options_menu_display)
        if (command == 'a'):
            account = input(input_account_choice(user))
            if (int(account) > len(user['accounts'])):
                print('Conta não encontrada')
                continue
            transfer_operations(account_choice(user, account))
        elif (command == 'c'):
            accounts.append(create_accounts(user, BASE_ACCOUNT))
        elif (command == 'q'):
            break

def create_accounts(user, BASE_ACCOUNT: dict):
    new_account = deepcopy(BASE_ACCOUNT)
    user_id = ''
    for user_ in users:
        if (user_[list(user_.keys())[0]]['name'] == user['name']):
            user_id = list(user_.keys())[0]
    
    new_account['user'] = user_id
    account_id = str(int(list(accounts[-1].keys())[0]) + 1)
    user['accounts'].append(account_id)
    return {
        account_id : new_account
    }



while True:
    command = input(menu_login)

    if (command == 'c'):
        create_user()
        continue
    elif (command == 'e'):
        user = input('Digite seu usuario: *CPF*: ')
        password = input('Digite sua senha: ')
        if (check_user_login(user, password)):
            _, user_loged = check_user_login(user, password)
            print('Bem vindo!')
            options_menu(user_loged)
        else:
            print('SENHA ou USUARIO INCORRETO')
    elif (command == 'q'):
        break