import random


def drawBase():
    print(base0)
    print(base1)
    print(base2)
    print(base3)
    print(base4)
    print(base5)
    print(base6)

base0 = '_____'
base1 = '|    |'
base2 = '|    '
base3 = '|   '
base4 = '|    '
base5 = '|   '
base6 = '---'
erros = 0
palvara = 'estas serão as palavras de teste execforca felipe'.split()[random.randrange(7)]

print('*' * len(palvara))
#print(palvara) #ajudar no debug
lst, lstFinal = [], []
[lst.append(i) for i in palvara]
[lstFinal.append('*') for i in palvara]
#print(lst) #ajudar no debug
print(lstFinal)
char = input('digite um caracter para formar a palavra : ').lower()

while lstFinal.count('*') > 0:
    if lst.count(char) > 0:
        for i in range(lst.count(char)):
            indicie = lst.index(char)
            lstFinal[indicie] = char
            lst[indicie] = '*'
        if lstFinal.count('*') == 0:
            print('You Win!')
            break
    else:
        #drawErro(erros)
        if erros == 0:
            base2 += 'O'
        elif erros == 1:
            base3 += '|'
        elif erros == 2:
            base3 += '|'
        elif erros == 3:
            base3 += '|'
        elif erros == 4:
            base4 += '|'
        elif erros == 5:
            base5 += '|'
        elif erros == 6:
            base5 += ' |'
        elif erros > 6:
            print('Game Over!')
            break
        erros += 1
    drawBase()
    print(lstFinal)
    print('erros : ',erros)
    char = input('digite um caracter para formar a palavra : ').lower()