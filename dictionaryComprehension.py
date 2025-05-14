#Para criarmos um conjunto --> conjunto = {1, 2, 3, 4}
#Para criarmos um dicionário --> dicionario = {'a': 1, 'b':2, 'c':3, 'd':4}
numeros = {'a': 1, 'b':2, 'c':3, 'd':4, 'e':5}

quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}

print(quadrado)
#OUTRA FORMA 
chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}

print(mistura)

#para gerar um dicionario apartir de uma lista
numero = [1, 2, 3, 4, 5]

quadrados = {valor: valor ** 2 for valor in numero}

print(quadrados)

'''PARA GERAR UM DICIONARIO APARTIR DE UM SET(CONJUNTO)
numero = {1, 2, 3, 4, 5}

quadrados = {valor: valor ** 2 for valor in numero}

print(quadrados)'''

#EXEMPLO COM LOGICA CONDICIONAL USANDO RES
numero = [1, 2, 3, 4, 5]

res = {num:('par' if num % 2 == 0 else 'impar') for num in numero}

print(res)

# ----------------------------------------- SET COMPREHENSION
'''em um conjunto não existe repeticao de valores, nem ordenacao'''
letras = {letra for letra in 'Geek University'}

print(letras)

#CRIANDO UM CONJUNTO 
digitos = {num for num in range(1, 7)}

print(digitos)
#conjunto de numeros elevados a 2 potencia
numeros = {x ** 2 for x in range(10)}

print(numeros)
