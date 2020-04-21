"""
Loop -> estrutura de repetição / laço de repetição
for ->  para tal condição - irá executar

ex:
for item in interavel:
IMPORTANTE -> tipows interáveis suportados no for são:
    - string
    - lista (será estudado em outra aula) - ex: lista = [1, 2, 3, 4]
    - range (será estudado em outra aula) - ex: numeros = range(1, 10)
"""
numeros = range(1, 10)
count = 1


for count in numeros:
    print(f'{count} - dentro do for')
    count += 1

# descobrir o indice(posição) de uma string -> utilizar enumerate
nome = 'Felipe Savaris'
"""
for indice, valor in enumerate(nome):
    print(nome[indice], [valor])
"""
for i in enumerate(nome):
    print(i)
# desta maneira imprime indice e valor

for _, i in enumerate(nome):
    print(i)
# utilizando o _ eu descarto a impressao do indice e imprimo apenas o valor

for i in enumerate(nome):
    print(i[0])
# imprimindo apenas o indice

for i in enumerate(nome):
    print(i[0], end='')
# imprimindo apenas o indice, SEM PULAR LINHA


#---------------------------------------
# exemplo de soma usando for
qtd = int(input('\nQuantas vezes o loop deve rodar? '))
soma = 0


for i in range(1, qtd+1):
    num = int(input(f'Informe o {i}/{qtd} valor: '))
    soma = soma + num
print(f'A total dos valores informados é: {soma}')

