# ------------------------List Comprehensions-----------------------

# LIST COMPREHENSIONS X LOOP
# LOOP
'''numerosDobrados = []

for numeor in [1, 2, 3, 4]:
    numerosDobrados.append(numero * 2)
    
print(numerosDobrados)'''
# LIST COMPREHENSIONS
'''print([numero * 2 for numero in [1, 2, 3, 4]])'''

# outro exemeplo
numeros = [1, 2, 3, 4, 5]

res = [numeros * 10 for numero in numeros]

print(res)
'''para entender melhor:
1º numero * 10 
2º for numero in numeros'''
# LIST COMPREHENSION COM ESTRUTURAS CONDICIONAL
'''numeros = [1, 2, 3, 4, 5]'''

pares = [numero for numero in  numeros if numero % 2 ==0]
impares = [numero for numero in  numeros if numero % 2 !=0]

print(pares)
print(impares)

# LIST COMPREHENSION COM ESTRUTURAS CONDICIONAL REFATORADO 
'''qualquer numero par modulo de 2 e 0, o em python é false. not false= true
qualquer numero impar modulo de 2 e 1, 1 em python e true'''
pares = [numero for numero in numeros if not numero % 2]
impares = [numero for numero in numeros if numero % 2]

print(pares)
print(impares)
# LIST COMPREHENSION COM RES
'''numeros = [1, 2, 3, 4, 5]'''
res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)

#LISTAS ANINHADAS (nested lists)------------------------------------------------
'''Algumas linguagens de prog. (C/JAVA/PHP) possuem uma estrutura de dados chamadas arrays:
UNIDIMENSIONAIS (ARRAYS/VETORES)
MULTIDIMENSIONAIS (MATTIZES)
em PYTHON temos as LISTAS : Listas  = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 
- Iterando com loops em uma kista anunhada:
for lista in listas:
    for num in lista:
        print(num)'''
Listas  = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[[print (valor) for valor in lista]for lista in Listas] #cCOMPREHENSIOOS LIST

#GERANDO UM TABULEIRO
tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)





