'''a funcao REDUCE() deixou de ser uma funcao integrada a partir do Python3, após essa versao e necessario
importar a funcao utilizando o modulo FUNCTOOLS

ela funciona em dois passos:
1 res1 = f(a1, a2) --> aplica a funcao nos dois primeiros elementos da colecaoe guarda o resultado
2 res2: f(res1, a3) --> aplica a funcao passando o resultado do passo 1 mais o terceiro elemento e
guarda o resultado
isso se repete ate o final... Passon: resn = f(resn, an)
No final, REDUCE() retornara o resultado final'''

from functools import reduce

dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]
multi = lambda x, y: x * y

res = reduce(multi, dados)

print(res)


#GUIDO VAN ROSSUM: 'Utilize a funcao REDUCE() se voce realmente precisa dela. 99% das vezes
# um LOOP FOR e mais legivel.
#utilizando loop normal

res = 1
for n in dados:
    res = res + n

print(res)

#------------------ANY E ALL --------------------------

#all() - retorna true se todos os elementos do iteravel sao verdadeiros ou se o iteravel esta vazio

print(all([0, 1, 2, 3, 4])) #false

print(all([1, 2, 3, 4])) #true

print(all([])) #true

nomes = ['Carlos', 'Carla', 'Camila', 'Carminha', 'Danillo']

print(all([nomes[0] == 'C' for nome in nomes]))

#um iteravel vazio convertido em boolean é FALSE, mas o ALL() entende como TRUE
print(all([letra for letra in 'aeio' if letra in 'aeiou'])) 

print(all([num for num in [14, 2, 10, 6, 8, 37]if num % 2 == 0]))

#any() - retorna TRUE se qualquer elemento do iteravel for verdadeiro, e se o iteravel estiver vazio retorna FALSE

print(any([0, 1, 2, 13, 7])) #true

print(any([0, False, {}, []])) #false


nomes = ['Carlos', 'Carla', 'Camila', 'Carminha', 'Danillo']
print(any([nome[0] == 'C' for nome in nomes]))

print(any([num for num in [14, 2, 10, 6, 8, 37]if num % 2 == 0]))