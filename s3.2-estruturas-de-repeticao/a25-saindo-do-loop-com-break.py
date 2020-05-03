"""
utilização do BREAK em loops
"""
for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)
print('Saiu do loop')


#--------------------------------
while True:
    comando = input('Digite "sair" para finalizar: ')
    if comando == 'sair':
        break
