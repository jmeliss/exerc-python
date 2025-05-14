''' área e classificação de um triangulo'''
print('Digite o valor da base: ')
b= int(input())
print('Digite o valor do lado a: ')
a= int(input())
print('Digite o valor do lado c: ')
c= int(input())
area = (b * a)/2
perimetro = (b+ a + c)
if b == a and b == c :
    print("esse triangulo e um equilatero de area: ", area,"e perimetro: ", perimetro)
elif b != a and a == c:
    print("esse triangulo e um isoceles de area:  ", area,"e perimetro: ", perimetro)
elif b != a and a != c:
    print("esse triangulo e um escaleno de area: ", area,"e perimetro: ", perimetro)    
else:
    print("Fim do programa.")