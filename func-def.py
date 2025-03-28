def cubo(num):
    return num * num * num
num= float(input('Digite um numero: '))
cubo(num)
print(num, " elevado ao cubo e: ", cubo(num))
'''o print abaixo calcula a nona de num com a instrução cubo(cubo(num))'''
print(num," elevado a nona e: ", cubo(cubo(num)))



