"""
Range

o range é muito util enquanto utilizado no LOOP FOR
este gera sequencias numéricas específicas

o range pode substituir uma variavel count
-------------------------------------------------------------
formas de range
range(valor_de_parada)
"""
for num in range(11):
    print(num)
"""
range(valor_de_inicio, valor de parada)
"""
for num in range(1, 10):
    print(num)
"""
range(valor_de_inicio, valor_de_parada, passo)
"""
for num in range(1, 11, 2):
    print(num)
"""
range com passo inverso
range(valor_inicio, valor_de_parada, passo)
"""
for num in range(10, 0, -1):
    print(num)
"""
range em lista
"""
lista = list(range(10, -1, -1))
print(lista)

