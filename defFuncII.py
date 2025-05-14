#Crie uma funcao que recebe um parametro inteiro e devolve o seu dobro

'''def dobro(num):
    return num * 2

print(dobro(1))
print(dobro(20))
print(dobro(30))
print(dobro(400))
print(dobro(5000))'''
#outra maneira de resolver
def dobro(numero: int) -> int:
    return numero *2


if __name__ == '__main__':
    valor; int=4
    print(f'O dobro de {valor} e {dobro(valor)}')

#faca um programa que tenha uma funcao que recebe um parametro 
# no formato 'string' ex: "01/01/2025" e
#imprima ele por extenso como "1 de janeiro de 2025"
'''def porExtenso(dia, mes, ano):
    data_extenso = ''
    mes_map = [
            (1, 'janeiro'),
            (2, 'fevereiro'),
            (3, 'marco'),
            (4,'abril'),
            (5, 'maio'),
            (5, 'junho'),
            (7, 'julho'),
            (8, 'agosto'),
            (9, 'setembro'),
            (10, 'outubro'),
            (11, 'novembro'),
            (12, 'dezembro')
            ]
    for mes_map, mes_extenso in mes_map:
        if mes == mes_map:
            data_extenso = f"{dia} de {mes_extenso} de {ano}"
            break
    return data_extenso

print(porExtenso(4, 4, 2024))'''
#outra maneira de resolver
def dataPorExtenso(data: str) -> None:
    d = data.split('/')

    dia: int = int(d[0])
    mes: int = int(d[1])
    ano: int = int(d[2])

    if mes == 1:
        mes_str = 'janeiro'
    elif mes == 2:
        mes_str = 'fevereiro'
    elif mes == 3:
        mes_str = 'marco'
    elif mes == 4:
        mes_str = 'abril'
    elif mes == 5:
        mes_str = 'maio'
    elif mes == 6:
        mes_str = 'junho'
    elif mes == 7:
        mes_str = 'julho'
    elif mes == 8:
        mes_str = 'agosto'
    elif mes == 9:
        mes_str = 'setembro'
    elif mes == 10:
        mes_str = 'outubro'
    elif mes == 11:
        mes_str = 'novembro'
    elif mes == 12:
        mes_str = 'dezembro'
    else
        mes_str = 'desconhecido'

    print(f'{dia} de {mes} de {ano}')


if __name__ == '__main__':
    dataPorExtenso('01/01/2024')


#faca um programa que tenha uma funcao que receba uma lista de inteiros que retorne  o maior valor

'''def maiorNum (numeros):
    maiorNum = 0
    for num in numeros:
        if num > maiorNum:
            maiorNum = num
    return maiorNum


numeros = [1, 23, 4, 5, 43, 56, 94, 87]
print(maiorNum(numeros))'''
def maior(inteiros: list[int]) -> int:
    return max(inteiros)

if __name__ == '__main__':
    lista: list[int] = [1, 23, 4, 5, 43, 56, 94, 87]
    print(f'O maior valor da lista {lista} e {maior(lista)}')