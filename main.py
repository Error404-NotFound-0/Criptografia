def main():
    while True:
        print('-'*10, 'CRIPTOGRAFADOR', '-'*10)
        e = input(' Opções; \n\n a) Criptografar uma mensagem \n b) Descriptografar uma mensagem \n\n Escolha (a, b): ')
        if e.lower() == 'a':
            criptografar()
        elif e.lower() == 'b':
            descriptografar()
        else:
            print('Escolha inválida!')


def criptografar():
    while True:
        try:
            print('\n', '-'*10, 'CRIPTOGRAFAR', '-'*10)
            m = input('\n Insira a mensagem que será criptografada: ')
            c = ''
            break
        except:
            print('Algo deu errado, tente novamente.')
            return
    for i in m:
        if i.isalpha():
            c += f"<{ord(i)}>"
        else:
            c += f"<{i}>"
    print('\n', '-'*10, 'MENSAGEM CRIPTOGRAFADA', '-'*10)
    print('\n', c, '\n')


def descriptografar():
    while True:
        try:
            print('\n', '-'*10, 'DESCRIPTOGRAFAR', '-'*10)
            m = input('\n Insira a mensagem que será descriptografada: ')
            d = ''
            na_lista = False
            lista = ''
            break
        except:
            print('Algo deu errado, tente novamente.')
            return
    for i in m:
        if i == '<':
            na_lista = True
            lista = ''
        elif i == '>':
            if lista.isdigit():
                num = int(lista)
                if (90 >= num >= 65) or (122 >= num >= 97):
                    d += chr(num)
                else:
                    d += str(num)
            else:
                d += lista
        elif na_lista:
            lista += i

    print('\n', '-'*10, 'MENSAGEM DESCRIPTOGRAFADA', '-'*10)
    print('Mensagem Original: ', ''.join(d))

main()