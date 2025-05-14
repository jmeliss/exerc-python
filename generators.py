# --------------  GENERETOR EXPRESSION -------------------
'''são como as lists comprehension mas o generetor ocupa menos recurso em memoria.
GENERETORS é o nome dado as tuple comprehension'''

#nomes = ['Carlos', 'Camila', 'Carla', 'Cristina', 'Laura']
#print(any(nome[0] == 'C' for nome in nomes)) #sem generetor
nomes = ['Carlos', 'Camila', 'Carla', 'Cristina', 'Laura']
res = (nome[0] == 'C' for nome in nomes)
for nome  in res:
    print(nome)
print(type(res))

'''qual a utilidade de GETSIZEOF() ? --> retorna a quantidade de bytes em memoria do elemento passado como 
parametro''' 
from sys import getsizeof

print(getsizeof('Geek'))

print(getsizeof('University'))

print(getsizeof(17051996))

print(getsizeof(91))

print(getsizeof(True))

#Gerando uma lista de numeros com:
list_comp = getsizeof([x * 10 for x in range(100)])

set_comp = getsizeof({x * 10 for x in range(100)})

dic_comp = getsizeof({x: x * 10 for x in range(100)})

gen = getsizeof(x * 10 for x in range(100))

gen = (x * 10 for x in range(100))

for num  in gen:
    print(num)

print('Para realizar a mesma tarefa, gastamos em memoria: ')
print(f'List Comprehension: {list_comp} bytes')
print(f'Set Comprehension: {set_comp} bytes')
print(f'Dictionary Comprehension: {dic_comp} bytes')
print(f'Generetor Expression: {gen} bytes')


            