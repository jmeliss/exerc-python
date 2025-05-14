'''def cubo(num):
    return num * num * num
num= float(input('Digite um numero: '))
cubo(num)
print(num, " elevado ao cubo e: ", cubo(num))

#o print abaixo calcula a nona de num com a instrução cubo(cubo(num))
print(num," elevado a nona e: ", cubo(cubo(num)))

def quadrado(num):
  return num * num
#coloque dentro do parenteses o numero que deseja calcular
print(quadrado())

#ou também é possível obter o mesmo resultado desta forma
def quadrado(num):
    return num ** 2
print(quadrado())
'''
#agora uma função para cantar parabéns
'''def cantar_parabens(aniversariante):
    print("Parabens para voce")
    print("Nessa data querida")
    print("Muitas felicidades")
    print("muitos anos de vida")
    print(f"Viva o/a {aniversariante}!")
#digite o nome do aniversáriante dentro do parenteses abaixo
cantar_parabens()

#funcao para jogar moeda

from random import random

def jogaMoeda():
    #valor = random() --- nao e necessario criar essa variavel, podendo chamar o random 
    # no lugar da variavel
    if valor > 0.5:
       return 'cara'
    return 'coroa'
print(jogaMoeda())'''

#FUNCOES COM PARAMETROS
#funcoes podem ter N parametros de entrada, eles sao separados por virgula. 

'''def exponencial(numero, potencia=2):
    return numero ** potencia

print(exponencial(2, 3))
print(exponencial(5))

print(exponencial())

def somaImpares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total =  total + num
    return total

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
soma = somaImpares(numeros)
print(soma)
#Variaveis globais / variaveis locais
#  --- variavel global
instrutor = 'geek'
def dizOi():
    return f'Oi {instrutor}!'

print(dizOi())
#variavel local
instrutor = 'geek'
def dizOi():
    instrutor = 'Python' #variavel local tem preferencia quando a
    #variavel global e local tem o mesmo nome
    return f'Oi {instrutor}!'

print(dizOi())'''
#podemos ter funcoes que sao declaradas dentro de funcoes

def fora():
    contador = 0

    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()

print (fora())


