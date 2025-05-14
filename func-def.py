def cubo(num):
    return num * num * num
num= float(input('Digite um numero: '))
cubo(num)
print(num, " elevado ao cubo e: ", cubo(num))

'''o print abaixo calcula a nona de num com a instrução cubo(cubo(num))'''
print(num," elevado a nona e: ", cubo(cubo(num)))

def quadrado(num):
    return num * num
''' coloque dentro do parenteses o numero que deseja calcular'''
print(quadrado())

'''ou também é possível obter o mesmo resultado desta forma '''
def quadrado(num):
    return num ** 2
print(quadrado())

'''agora uma função para cantar parabéns '''
def cantar_parabens(aniversariante):
    print("Parabens para voce")
    print("Nessa data querida")
    print("Muitas felicidades")
    print("muitos anos de vida")
    print(f"Viva o/a {aniversariante}!")
'''digite o nome do aniversáriante dentro do parenteses abaixo'''
cantar_parabens()




