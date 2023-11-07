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

while True:
    command = input(menu)

    if (command == 's'):
        ...
    
    elif(command == 'd'):
        ...
    
    elif(command == 'e'):
        ...
    
    elif(command == 'q'):
        break
    
    else:
        continue