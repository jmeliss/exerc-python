''' MAP é uma funcao que recebe dois parametros: 
o primeiro e a funcao e o segundo um iteravel, retorna um map object
com MAP fazemos um mapeamento de valores para a funcao'''

#calculando a area de um circulo com raio 'r'
import math

def area(r):
    return math.pi * (r ** 2)

print(area(2))
print(area(5.3))

#forma comum
raios = [2, 5, 7.1, 0.3, 10, 44]
areas = []
for r in raios:
    areas.append((area(r)))

print(areas)

#CALCULANDO A AREA DE UM CIRCULO COM MAP
areas = map(area, raios)

print(areas)
print(type(areas))

print(list(areas))

# MAP COM LAMBDA
print(list(map(lambda r: math.pi * (r ** 2), raios)))

#EXEMPLO COM CONVERSAO DE TEMPERATURA 

cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Sao Psulo', 32), ('Tokio', 27)]

print(cidades)

cParaF = lambda dado: (dado[0], (9/5) * dado[1] + 32) #f = 9/5 * c + 32

print(list(map(cParaF, cidades)))

