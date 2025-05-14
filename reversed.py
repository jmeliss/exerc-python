#funciona em qualquer iteravel (lista,tupla, set), sua funçao e inverter o iteravel

lista = [1, 2, 3, 4 , 5]


res = reversed(lista)
#retorna um iterável chamado list reverse iterator

print(res)
print(type(res))
#para converter para uma lista, tupla ou set 
print(list(reversed(lista)))
print(tuple(reversed(lista)))
print(set(reversed(lista)))#no SET nao definimos a ordem dos elementos

#podemos iterar sobre o REVERSED()
for letra in reversed('Geek University'):
    print(letra, end='')

#iterando sem utilizar o FOR
print(''.join(list(reversed('Geek University'))))#.JOIN()

#utilizando slice de strings
print('Geek University'[::-1])

#utilizando REVERD() para fazer um loop for reverso
for n in reversed(range(0, 10)):
    print(n)
    