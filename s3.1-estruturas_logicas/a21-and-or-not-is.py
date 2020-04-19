"""
estruturas lógicas
and - or - not - is

operador unário:
    - not - in
operadores binários:
    - and - or - is
"""
#----------------------------------------------------------------------------
# estrutufa AND
ativo = True
logado = False


if ativo and logado:
    print('Bem-vindo!')
else:
    print('É preciso ativar a sua conta')


#--------------------------------------------------------------------------
# estrutura OR
if ativo or logado:
    print('Bem-vindo (estrutura OR)')
else:
    print('É preciso ativar a sua conta')



#-------------------------------------------------------------------------
# estrutura NOT - valor booleano invertido, inversão de valores True e False
if not ativo:
    print('usuário inativo')
else:
    print('O usuário não está ativo (Estrutura NOT)')
#verificando negação
print(not True)
print(not False)


#------------------------------------------------------------------------
# estrutura IS - é
if ativo is False:
    print('usuário inativo (Estrutura IS)')
else:
    print('O usuário não está ativo (Estrutura NOT)')
