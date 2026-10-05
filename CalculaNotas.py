import funcoes_media

print("Programa para calcular notas de alunos.")
print()

a1 = float(input("Informe o primeiro valor: "))
a2 = float(input("Informe o segundo valor: "))
a3 = float(input("Informe o terceiro valor: "))

p1 = 2
p2 = 3
p3 = 5
p4 = p1 + p2 + p3

nota = funcoes_media.media_ponderada(a1, a2, a3, p1, p2, p3, p4)

print()
print(f"A média das suas notas: {nota:.2f}")