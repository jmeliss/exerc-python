#ZIP() ---> cria um iteravel (zip object) que agrega elemento de cada um dos iteraveis passados como entrada em pares
lista1 = [1, 2, 3]
lista2 = [8, 5, 4]

zip1 = zip(lista1, lista2)

print(zip1)
print(type(zip1))

#sempre podemos gerar uma lista, tupla ou dicionario
print(list(zip1))
'''retorna vazio
print(tuple(zip1))

print(set(zip1))

print(dict(zip1))'''

zip1 = zip(lista1, lista2)
print(tuple(zip1))

zip1 = zip(lista1, lista2)
print(set(zip1))

zip1 = zip(lista1, lista2)#torna os elementos da lista 1 chave e os da lista 2 valor
print(dict(zip1))

#ZIP() utiliza como parametro o menor tamanho em iteravel
lista3 = [2, 3, 6, 7, 2]

zip1 = zip(lista1, lista2, lista3)#ele ignorou o 7 e o 2
print(list(zip1))

#utilizando zip  com iteraveis diferentes
tupla = 1, 2, 3, 4
lista = [5, 6, 7, 8]
dicionario = {'a': 9, 'b': 10, 'c': 11, 'd': 12}
zt = zip(tupla, lista, dicionario.values())#necessario colocar .VALUES() em dicionarios para utilizar somente o valor

#criando listas de tuplas
num = [(1, 2), (3, 4), (5,6), (7, 8)]#paar desempacotar utiliza-se *
print(list(zip(*num)))

#mostrando a maior nota de cada aluno
prova1 = [10, 9, 8]
prova2 = [7, 6, 5]
alunos = ['agatha', 'lucas', 'simone']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}

print(final)# retorna o nome de cada aluno e sua maior nota