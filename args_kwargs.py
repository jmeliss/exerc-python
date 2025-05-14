'''#retorna os valores em uma tupla
def somaTodosNum(*args):
    print(args)

somaTodosNum()
somaTodosNum(1)
somaTodosNum(2, 3)
somaTodosNum(4, 5, 6)
somaTodosNum(6, 7, 8, 9)
#retorna a soma dos valores 
def somaTodosNum(*args):
    total = 0
    for numero in args:
        total = total + numero
    return total
  
print(somaTodosNum())
print(somaTodosNum(1))
print(somaTodosNum(2, 3))
print(somaTodosNum(4, 5, 6))
print(somaTodosNum(6, 7, 8, 9))
#reduzindo a funcao 
def somaTodosNum(*args):
    return sum(args)
  
print(somaTodosNum())
print(somaTodosNum(1))
print(somaTodosNum(2, 3))
print(somaTodosNum(4, 5, 6))
print(somaTodosNum(6, 7, 8, 9))
#outro exemplo de utilizacao de args
def verificaInfo(*args):
    if 'Geeek' in args and 'University' in args:
        return 'Bem-vindo Geek!'
    return 'Eu nao tenho certeza de quem voce e.'
print(verificaInfo())
print(verificaInfo(1, True, 'University', 'Geek'))
print(verificaInfo(1, 'University', 3.145))

#DESEMPACOTADOR
def somaTodosNum(*args):
    return sum(args)

numeros =n[1, 2, 3, 4, 5, 6, 7]
print(somaTodosNum(*numeors)) # o * serve para informar que estamos passando como argumento
#uma colecao de dados, dessa forma ele sabera que precisara desempacotar esses dados '''

#kwargs --- utiliza **
def coresFav(**kwargs):
    print(kwargs)


coresFav(wel='preto', mel='azul', pitchulli='caramelo')
#melhorando a funcao
def coresFav(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()}, e {cor}.')

coresFav(wel='preto', mel='azul', pitchulli='caramelo')

#outro exxemplo
def cumprimentoEspecial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Voce recebeu um cumprimento pythonico geek!'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Nao tenho certeza quem voce e.'

print(cumprimentoEspecial())
print(cumprimentoEspecial(geek='Python'))
print(cumprimentoEspecial(geek='oi'))
print(cumprimentoEspecial(geek='especial'))

#parametro correto de declaracao
#-parametros obrigatorios
#-args
#-parametros default (nao obrigatorios)
#-kwargs

def minhaFunc(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos.')
    print(args)
    if solteiro:
        print('Solteiro.')
    else:
        print('Casado.')
    print(kwargs)

minhaFunc(8, 'Julia')
minhaFunc(18, 'Felicity', 4, 5, 3, solteiro=True)
minhaFunc(34, 'Felipe', eu='nao', voce='vai')
minhaFunc(19, 'Carla', 9, 4, 3, java=False, python=True)

#DESEMPACOTAR COM KWARGS
def mostraNomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"

nomes = {'nome': 'Felicity', 'sobrenome': 'Jones'}
print(mostraNomes(**nomes))

