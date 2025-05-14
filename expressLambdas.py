#ENTENDENDO EXPRESSOES LAMBDA
#lambdas sao funcoes sem nomes, ou funcoes anonimas
'''expressao lambda --> lambda x: 3 * x + 1'''
#utilizando expressao lambda
calc = lambda x: 3 * x + 1

print(calc(5))
print(calc(7))

#expressoes lambda com multiplas entradas
nomeCompleto = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nomeCompleto(' jheniffer', 'melissa '))
print(nomeCompleto(' WELLINGTON', 'ataide'))

#FUNCAO QUADRATICAS --> f(x) = a * x ** 2 + b * x + c 
#DEFININDO A FUNCAO:
def geradoraFuncaoQuad(a, b,  c):
    return lambda x: a* x ** 2 +b * x + c
    
teste = geradoraFuncaoQuad(2, 3, -5)
    
print(teste(0))
print(teste(1))
print(teste(2))

#definindo a funcao sem criar a variavel teste
print(geradoraFuncaoQuad(3, 0, 1)(2))