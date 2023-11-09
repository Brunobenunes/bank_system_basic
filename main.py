from abc import ABC, abstractclassmethod, abstractproperty

CLIENTS = [

]
ACCOUNTS = [

]
class Transaction(ABC):

    @property
    @abstractproperty
    def value(self):
        pass

    @abstractclassmethod
    def register(self, account):
        pass


class Client:
    def __init__(self, address) -> None:
        self._address = address
        self._accounts = []

    def run_transaction(self, account, transaction: Transaction):
        transaction.register(account)
    
    def add_account(self, account):
        self._accounts.append(account)

class Person(Client):
    def __init__(self, address, cpf, name, birth, password= '') -> None:
        super().__init__(address)
        self._cpf = cpf
        self._name = name
        self._birth = birth
        self._password = password


    @property
    def name(self):
        return self._name
    
    @property
    def accounts(self):
        return self._accounts
    
    def login_check(self, login, password):
        print(login, password, '///// SELF: ', self._cpf, self._password)
        return (login == self._cpf and password == self._password), self


    
    @classmethod
    def create(cls):
        name = input('Digite seu Nome e Sobrenome: ')
        cpf = input('Digite seu CPF: ')
        birth = input('Digite sua Data de Nascimento: dd/mm/aaaa ')
        street = input('Digite Seu endereço: * Rua/Av, numero* ')
        district = input('Digite Seu Bairro: ')
        city = input('Digite sua Cidade: ')
        state = input('Digite o UF: *MG* ')
        password = input('Digite sua Senha: ')
        address = f'{street} - {district}, {city}/{state}'
        return CLIENTS.append(cls(name=name, cpf=cpf, birth=birth, address=address, password=password))

class AccountClient:
    def __init__(self, number, client) -> None:
        self._balance = 0
        self._number = number
        self._branch = '0001'
        self._client = client
        self._history = History()

    @property
    def number(self):
        return self._number
    
    @property
    def checking_account(self):
        return self._checking_account
    
    @property
    def history(self):
        return self._history
    
    @property
    def client(self):
        return self._client

    @property
    def balance(self):
        return self._balance

    def withdraw(self, value):
        if (value < 0):
            print('@@@@ Falha no Saque. Insira um valor Positivo! @@@')
            return False
        if (value > self.balance):
            print(self.balance)
            print('@@@@ Falha no Saque. Saldo Inválido! @@@')
            return False
        if (value <= self.balance):
            print('&&&& Saque Realizado com SUCESSO! &&&')
            self._balance -= value
            return True
        
    def deposit(self, value):
        if (value < 0):
            print('@@@@ Falha no Depósito. Insira Valores Positivos! @@@')
            return False
        self._balance += value
        return True
    
    @classmethod
    def create_account(cls, client, number):
        ACCOUNTS.append(cls(number=number, client=client))
        return client.accounts.append(number)
    
class ChekingAccount(AccountClient):
    def __init__(self, number, client) -> None:
        super().__init__(number, client)
        self._max_withdraw = 500
        self._daily_withdraw = 3
        self._count_withdraw = 0
    
    def withdraw(self, value):
        if (self._count_withdraw == self._daily_withdraw):
            print('@@@@ Falha no Saque. Você já atingiu o limite máximo de saques diários! @@@@')
            return False
        if (value > self._max_withdraw):
            print(f'@@@@ Falha no Saque. Limite máximo para saque: R$ {self._max_withdraw} @@@@')
            return False
        return super().withdraw(value)


class Deposit(Transaction):
    def __init__(self, value) -> None:
        self._value = value

    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, value):
        self._value = value

    def register(self, account: ChekingAccount):
        if (account.deposit(self.value)):
            new_Transaction = f'{self.__class__.__name__}: R$ {self._value}'
            account.history.add_transaction(new_Transaction)
        
class Withdraw(Transaction):
    def __init__(self, value) -> None:
        self._value = value

    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, value):
        self._value = value
    
    def register(self, account: ChekingAccount):
        if (account.withdraw(self.value)):
            new_Transaction = f'{self.__class__.__name__}: R$ -{self._value}'
            account.history.add_transaction(new_Transaction)

class History:
    def __init__(self) -> None:
        self._history = []
    
    def add_transaction(self, transaction):
        self._history.append(transaction)

    def list_transactions(self, account: ChekingAccount):
        print(f'''
=======================================================
            Extrato da conta: {account.number}
''')
        for transaction in self._history:
            print(transaction)
        print(f'''
========================== Saldo Atual: {account.balance}
=======================================================
''')


def menu_login():
    while True:
        command = input('''
    =======================================================
                    ## Bank System DiO ##
                        
        [e] Entrar
        [c] Criar Usuario
        [q] Sair
                        
    =======================================================
    ''')
        if (command == 'e'):
            login = input('Digite seu CPF: ')
            client = ''
            status = ''
            password = input('Digite sua SENHA: ')
            for user in CLIENTS:
                status, client_login = user.login_check(login, password)
                if (status):
                    client = client_login
            if (status):
                print(f'Bem vindo {client.name}')
                client_menu(client)
            else:
                print('@@@@   Usuario ou Senha Inválida!   @@@@')
        elif (command == 'c'):
            Person.create()
            continue
        elif (command == 'q'):
            print(' Tenha um Otimo Dia!')
            break
        else :
            print('@@@@ Comando Inválido. Tente Novamente! @@@@')
            continue

def client_menu(client):
    while True:
        command = input(f'''
    =======================================================
                    ## Bank System DiO ##
                        Bem Vindo {client.name}
                        
        [a] Acessar Contas
        [c] Criar Conta
        [q] Sair
                        
    =======================================================
    ''')
        
        if (command == 'a'):
            print(f'''
    =======================================================
                    ## Bank System DiO ##
                        Bem Vindo {client.name}
                        

''')
            for index, account in enumerate(client.accounts):
                print(f'[{index}]: Acc: {account}')
            account_choice = int(input('\n'))
            account = [acc for acc in ACCOUNTS if acc.number == client.accounts[account_choice]][0]
            account_menu(client, account)
        if (command == 'c'):
            ChekingAccount.create_account(client, len(ACCOUNTS))
        if (command == 'q'):
            break
        else:
            print('@@@@ Comando Inválido. Tente Novamente! @@@@')
            continue

def account_menu(client : Client, account : AccountClient):
    while True:
        command = input(f'''
        =======================================================
                        ## Bank System DiO ##
                        Bem vindo {client.name}
                        Acc: {account.number}
                            
            [s] Sacar
            [d] Depositar
            [e] Extrato
            [q] Sair
                            
        =======================================================
        ''')
        if (command == 's'):
            operation = Withdraw(float(input('Quanto deseja Sacar?:')))
            client.run_transaction(account, operation)

        if (command == 'd'):
            operation = Deposit(float(input('Quanto deseja Depositar?: ')))
            client.run_transaction(account, operation)
        
        if (command == 'e'):
            account.history.list_transactions(account)

        if (command == 'q'):
            break
        
            
menu_login()