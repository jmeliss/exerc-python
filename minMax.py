#MAX() --> retorna o maior valor em um iteravel ou o maior valor em dois ou mais elementos

lista = [1, 3, 4, 8, 99, 63, 129] #lista
print(max(lista))

lista = (1, 3, 4, 8, 99, 63, 129) #tupla
print(max(lista))


lista = {1, 3, 4, 8, 99, 63, 129} #conjunto
print(max(lista))

lista = {'a': 1,'b': 3,'c': 4,'d': 8,'e': 99,'f': 63,'g': 129} #dicionario
print(max(lista))#retorna a chave

lista = {'a': 1,'b': 3,'c': 4,'d': 8,'e': 99,'f': 63,'g': 129} #dicionario
print(max(lista.values())) #retorna o valor da chave

'''recebe dois valores e retorna o maior'''
val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))
print(max(val1, val2))

print(max('Geek University!'))

# ---------------------MIN ------------------
lista = {'a': 1,'b': 3,'c': 4,'d': 8,'e': 99,'f': 63,'g': 129} #dicionario
print(min(lista.values())) #retorna o valor da chave

'''recebe dois valores e retorna o maior'''
val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))
print(min(val1, val2))

print(min('Geek University!')) #avalia a ordem alfabetica para retornar o valor

lista = [1, 3, 4, 8, 99, 63, 129] #lista
print(min(lista))

lista = (1, 3, 4, 8, 99, 63, 129) #tupla
print(min(lista))


lista = {1, 3, 4, 8, 99, 63, 129} #conjunto
print(min(lista))

users = {'amanda','bianca','cintya','dado','elza','fabian','gianine'}
print(max(users)) #avalia a ordem alfabetica para retornar
print(min(users))

print(max(users, key=lambda users: len(users)))
print(min(users, key=lambda users: len(users)))

musicas = [
    {'titulo': 'Desparado', 'replay': 2},
    {'titulo': 'Diamond', 'replay': 3},
    {'titulo': 'Stay', 'replay': 7},
    {'titulo': 'Man down', 'replay': 4},
    {'titulo': 'Kiss it better', 'replay': 9},
]

print(max(musicas, key=lambda musica: musica['replay']))
print(min(musicas, key=lambda musica: musica['replay']))

print(max(musicas, key=lambda musica: musica['replay'])['titulo'])
print(min(musicas, key=lambda musica: musica['replay'])['titulo'])

#urilizando FOR para resolversem MIN() e MAX()
mais = 0 
menos = 0
for musica in musicas:
    if musica['replay'] > mais:
        mais = musica['replay']

for musica in musicas:
    if musica['replay'] == mais:
        print(musica['titulo'])

for musica in musicas:
    if musica['replay'] < menos:
        menos = musica['replay']

for musica in musicas:
    if musica['replay'] == menos:
        print(musica['titulo'])
