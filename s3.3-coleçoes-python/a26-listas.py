"""
listas -> são como vertores/matrizes;
    são dinâmicas e podem armazenar qualquer tipo de dados
    listas aceitam repetição

    ex: lista = []
"""
# funções interessantes:
"""
# verificar se valor está contido na lista
num = 8
if num in lista_4:
    print(f'{num} -> Número encontrado.')
else:
    print(f'{num} -> Não encontrado.')

# função de ordenação de lista -> sort
lista_1.sort()
print(lista_1)

# função para contar número de ocorrências -> count
print(lista_1.count(1))

# função para adiconar elemento -> append
lista_1.append(6)
print(lista_1)

# função para adicionar mais de um elemento a lista -> extend
lista_1.extend([7, 8, 9])
print(lista_1)

# função para adicionar elemento informando a posição da lista (não substiui o valor original)
lista_1.insert(0, 0)
print(lista_1)

# função para imprimir inversa
lista_1.reverse()
print(lista_1)

# função para copiar elementos da lista -> copy
lista_6 = lista_2.copy()
print(lista_6)

# função para contar elementos da lista -> len
print(len(lista_6))

# função remover último elemento -> pop
lista_6.pop()  # obs: retorna o elemento excluído
print(lista_6)

# também é possível remover pelo índice -> pop(2)
lista_6.pop(0)
print(lista_6)

# função remover toda a lista -> clear
lista_6.clear()
print(lista_6)

# função para transformar string em lista
string = 'Felipe Savaris: Desenvolvedor Python'
lista_dev = string.split()
print(lista_dev)
string = string.split(':')
print(string)

# função para transformar lista em string
lista_7 = ['Felipe', 'Savaris:', 'Desenvolvedor', 'Python']
string_dev = ' '.join(lista_7)
print(string_dev)

# alterar caracter de um string
string = 'Felipe.Savaris:.Desenvolvedor.Python'
string_dev = string.replace('.', ' ')
print(string_dev)

# ----------------------------------------------------------------
# iterando entre lista
soma = 0
for i in lista_1:
    print(i)
    soma = soma + i
print(f'Total: {soma}')

soma = ''
for i in lista_2:
    soma = soma + i
print(f'Total: {soma}')

# ----------------------------------------------------------------
carrinho = []
produto = ''

while produto != 'sair':
    print("Informe o produto a ser adicionado ou digite 'sair' para encerrar.")
    produto = input("Digite aqui: ")
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)


# em listas faz acesso de forma indexada
cores = ['verde', 'azul', 'preto', 'branco']
print(cores[1])
print(cores[-2])

print('----------------------')
indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1
    
# gerar indice em um for
for indice, cor in enumerate(cores):
    print(indice, cor)
    

# função para descobrir qual é o indice de um determinado elemento da lista -> index
print(cores.index('azul'))
print(cores.index('azul, 1) # começa a buscar o indice a partir da posição 1 da lista

"""

lista_1 = [1, 2, 3, 4, 5, 1, 2]
lista_2 = ['F', 'e', 'l', 'i', 'p', 'e', ' ', 'S', 'a', 'v', 'a']
lista_3 = []
lista_4 = list(range(11))
lista_5 = list("Felipe Savaris")
cores = ['verde', 'azul', 'preto', 'branco']

# parei o vídeo em: 1h 51min 28s
