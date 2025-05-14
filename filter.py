#CALCULANDO A MEDIA DOS DADOS UTILIZANDO A FUNCAO MEAN()
import statistics

dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

media = statistics.mean(dados)

print(media)
'''a funcao FILTER() serve para filtrar dados de uma determinada colecao'''
#assim como a funcao map(), a filter() recebe dois parametros: uma funcao e um iteravel
res = filter(lambda valor: valor > media, dados)
print(type(res))
print(list(res))

'''assim como no MAP(), apos serem utilizados os dados de FILTER() eles sao excluidos da memoria'''
# a funcao FILTER() e muito utilizada para a remocao de dados faltantes
paises = ['Chile', '', '', 'Argentina', 'Equador', 'Russia']

#res = filter(lambda pais: len(pais) > 0, paises) --> uma forma de usar
#res = filter(lambda pais: pais != '', paises) --> mais uma forma de usar
res = filter(None, paises)
print(list(res))

'''a diferenca entre a funcao MAP() e FILTER() uma retorna um objeto mapeando a funcao para cada elemento iteravel
a outra  retorna um objeto filtrando apenas os elementos de acordo com a funcao'''

usuarios = [
    {'username': 'samuel', 'tweets': ['eu adoro bolos', 'eu adoro pizzas']},
    {'username': 'bob', 'tweets': ['eu adoro petiscos', 'eu nao gosto de insetos', 'eu gosto de rosnar']},
    {'username': 'carla', 'tweets': []},
    {'username': 'mirela', 'tweets': []},
    {'username': 'lucio', 'tweets': []},
    {'username': 'cida', 'tweets': [ 'eu adoro viagens']},
]

print(usuarios)

#filtrando os usiarios inativos
#inativos = list(filter(lambda u: len(u['tweets']) == 0, usuarios)) ---> uma forma 
inativos = list(filter(lambda u: not u['tweets'], usuarios))

print(inativos)

#------------- COMBINANDO FILTER() & MAP() ----------------
instrutoras = ['Cintia', 'Baby', 'Marilia', 'Joana']

lista = list(map(lambda instrutora: f'Sua instrutora e a {instrutora}!', 
                 filter(lambda instrutora: len(instrutora) < 5, instrutoras)))

print(lista)