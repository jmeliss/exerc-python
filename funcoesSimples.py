#---------- LEN, ABS, SUM, ROUND----------------
#LEN() --> retorna o tamanho de um iteravel -- o numero de itens
print(len('Geek University'))

print(len(range(0, 10)))

'''por debaixo dos panos, quando utilizamos a funcao LEN() o python aplica essa funcao:
print('Geek University'._len_()) --> essa funcao é chamada de DUNDER LEN'''

#ABS() ---> retorna o valor absoluto de um numero inteiro ou real de forma basica seria o seu valor real sem o sinal
print(abs(-5))

print(abs(3.56))

print(abs(55))

print(abs(-4.7))
'''ele nao pode ser utilizado para uma string'''

#SUM() --> recebe como parametro um iteravel, podoendo receber um valor inicial e retorna a soma total dos elementos 
#incluindo o valor inicial
print(sum([1, 4, 2 , 5]))#lista sem valor inicial

print(sum([1, 3, 5 ,6], 2)) #o 2 é o valor inicial (valor defaul)

'''podemos utilizar para tuplas, sets, listas e dicionarios, não pode ser usado para strings'''
#utilizando sum() em dicionarios
print(sum({'a': 3, 'b':2, 'c': 5, 'd': 7}.values()))#adicionando .values()

#ROUND ---> RETORNA UM(inteiro) NUMERO ARREDONDADO PARA N DIGITOS DE PRECISAO APOS A CASA DECIMAL
#se a precisao nao for informada, retorna o inteiro mais proximo da entrada
print(round(10.2))#arredonda para baixo

print(round(10.6))#arredonda para cima

print(round(7.99999, 2))#declaramos que queremos apenas duas casas decimais
