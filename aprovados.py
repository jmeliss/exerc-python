
print("Digite o seu nome:")
nome = input ( )
print("Digite as suas duas notas:")
nota1 = float(input())
nota2 = float(input())
soma = (nota1 + nota2) // 2
if soma >= 6:
    print("Voce foi aprovado!")
else:
    print("Voce foi reprovado!") 
print("Sua nota final é: ", soma)