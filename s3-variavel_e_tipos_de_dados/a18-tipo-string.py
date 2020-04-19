nome = 'Felipe Savaris'

print(nome.split()) # transforma a string em lista

barran = 'Felipe \n Savaris'  #  \n divide a string em linhas

print(barran)

#fatiando string ou SLICE
print(nome[:5])
print(nome[7:])

print(nome.split())
print(nome.split()[1])

#invertendo a sequencia da string
print(nome[::-1])

#usando help ou dir pra ler o tutorial
#print(help(nome.istitle()))

# replace -> substituir palavras
print(nome.replace('F', 'f').replace('S', 's'))

teste = 'nome sobre '
print(teste.strip())  # o método strip remove espaço no final da string

print(teste.title()) # o método title faz com que a primeira letra seja maiúscula

