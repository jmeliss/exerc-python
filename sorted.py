# Diferente do SORT() que só conseguimos usar em lista, o SORTED() podemos utilizar com qualquer iteravel
#Serve pra ordenar
#sempre retorna uma lista independente do tipo de elementos no iteravel
numeros = [6, 1, 8, 2]
print(numeros)

print(sorted(numeros)) #ordena do menor para o maior

'''
numeros = {6, 1, 8, 2}
print(numeros) 
# --> quando o conjunto é um set os numeros são printados ordenados do maior para o menor '''

print(sorted(numeros, reverse=True)) #aqui ele ordenará do maior para o menor

print(tuple(sorted(numeros, reverse=True))) # aqui convertemos de lista para tupla

usuarios = [
    {'username': 'samuel', 'tweets': ['eu adoro bolos', 'eu adoro pizzas']},
    {'username': 'bob', 'tweets': ['eu adoro petiscos', 'eu nao gosto de insetos', 'eu gosto de rosnar']},
    {'username': 'carla', 'tweets': ['gosto de rosa', 'meu cachorro se chama bob']},
    {'username': 'mirela', 'tweets': ['hi!']},
    {'username': 'lucio', 'tweets': []},
    {'username': 'cida', 'tweets': ['semana que vem irei a paris', 'eu adoro viagens', 'comprei 3 casacos', 'bonjour']},
]

print(usuarios)

print(sorted(usuarios, key=len)) #aqui ele retorna o tamanho de cada chave do dicionario

# cada usuário do dicionario recebe o usuario e ordena pelo nome
print(sorted(usuarios, key=lambda usuario:usuario['username']))

musicas = [
    {'titulo': 'Desparado', 'replay': 2},
    {'titulo': 'Diamond', 'replay': 3},
    {'titulo': 'Stay', 'replay': 7},
    {'titulo': 'Man down', 'replay': 4},
    {'titulo': 'Kiss it better', 'replay': 9},
]

print(sorted(musicas, key=lambda musica: musica['replay']))

#da mais tocada para a menos tocada 
print(sorted(musicas, key=lambda musica: musica['replay'], reverse=True))
