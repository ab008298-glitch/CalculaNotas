print("Programa para calcular notas de alunos.")
print()

a1 = float(input("Informe o primeiro valor: "))
a2 = float(input("Informe o segundo valor: "))
a3 = float(input("Informe o terceiro valor: "))

p1 = 2
p2 = 3
p3 = 5
p4 = p1 + p2 + p3

nota = (a1 * p1 + a2 * p2 + a3 * p3) / p4

print()
print(f"A média das suas notas: {nota:.2f}")