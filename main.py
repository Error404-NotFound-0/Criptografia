import random
import time
def main():
    random.seed(time.time())
    while True:
        print('\n\n\n', '-'*10, 'CRIPTOGRAFADOR', '-'*10)
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
            chave1 = random.randint(1, 1000)
            chave2 = random.choice(['a', 'b'])
            

            break
        except:
            print('Algo deu errado, tente novamente.')
            return
    for i in m:
        if i.isalpha():
            if chave2.lower() == 'a':
                c += f"<{(ord(i)+chave1)*chave1}>"
            if chave2.lower() == 'b':
                c += f"<{(ord(i)*chave1)+chave1}>"
        else:
            while True:
                try:
                    if chave2.lower() == 'a':
                        c += f"<{(int(i)+chave1)*chave1}>"
                        break
                    elif chave2.lower() == 'b':
                        c += f"<{(int(i)*chave1)+chave1}>"
                        break
                except:
                    c += f"<{i}>"
                    break
    print('\n', '-'*10, 'MENSAGEM CRIPTOGRAFADA', '-'*10)
    print('\n', c, '\n')
    print('\n A chave da mensagem é: ', f'{chave1}'+f'{chave2}')
    recomecar()


def descriptografar():
    while True:
        try:
            print('\n', '-'*10, 'DESCRIPTOGRAFAR', '-'*10)
            m = input('\n Insira a mensagem que será descriptografada: ')
            chave = input('\n Insira a chave da mensagem: ')
            d = ''
            na_lista = False
            lista = ''
            chave1 = int(chave[:-1])
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
                if chave[-1].lower() == 'b':
                    num = (int(lista) - chave1) // chave1
                
                elif chave[-1].lower() == 'a':
                    num = (int(lista) // chave1) - chave1

                if (90 >= num >= 65) or (122 >= num >= 97) or num > 122:
                    d += chr(num)
                else:
                    d += str(num)
            else:
                d += lista
            na_lista = False
        elif na_lista:
            lista += i

    print('\n', '-'*10, 'MENSAGEM DESCRIPTOGRAFADA', '-'*10)
    print('Mensagem Original: ', ''.join(d))
    recomecar()

def recomecar():
    while True:
        e = input("\n Você deseja fazer novamente? (S/N)")
        if e.lower() == 's':
            break
        if e.lower() == 'n':
            quit()
        else:
            print('Escolha inválida.')

main()
