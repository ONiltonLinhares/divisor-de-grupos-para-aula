def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (TypeError, ValueError):
            print('\033[31mERRO:Por favor, digite um numrero inteiro valido\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mDados não informados.\033[m')
        else:
            return n

def leiacpf():
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    num2 = ''
    num3 = ''
    contador = 1
    marcador = True
    while marcador == True:
        num = input('Digite um cpf:')
        for i in num:
            if i in numeros:
                num2 += i
        if len(num2) != 11:
            print('\033[31mDigite um cpf valido(com 11 numeros).\033[m')
        else:
            marcador = False
    for i2 in num2:
        num3 += i2
        if contador == 3 or contador == 6 :
            num3 += '.'
        elif contador == 9:
            num3 += '-'
        contador += 1
    return num3

def leiacelular():
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    num = input('Digite um telefone:')
    num2 = ''
    num3 = ''
    contador = 1
    for i in num:
        if i in numeros:
            num2 += i
    if len(num2) != 11:
        print('\033[31mDigite um telefone valido(com 11 numeros).\033[m')
    else:
        num3 += '('
        for i2 in num2:
            num3 += i2
            if contador == 2:
                num3 += ') '
            elif contador == 7:
                num3 += '-'
            contador += 1
        return num3

def linha(tam = 42):
    return '\033[33m-\033[m' * tam

def cabeçalho(txt, cor = 'vd'):
    if cor == 'vm':
        print(linha())
        print(f'\033[31m{txt.center(42)}\033[m')
        print(linha())
    elif cor == 'az':
        print(linha())
        print(f'\033[34m{txt.center(42)}\033[m')
        print(linha())
    elif cor == 'am':
        print(linha())
        print(f'\033[33m{txt.center(42)}\033[m')
        print(linha())
    elif cor == 'vd':
        print(linha())
        print(f'\033[32m{txt.center(42)}\033[m')
        print(linha())

def menu(lista, str = 'MENU'):
    cabeçalho('MENU PRINCIPAL')
    c = 1 
    for item in lista:
        print((f'\033[33m{c}\033[m - \033[34m{item}\033[m'))
        c += 1
    print(linha())
    opç = leiaint('\033[32mSua Opção: \033[m')
    return opç


