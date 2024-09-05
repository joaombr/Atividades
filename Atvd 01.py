total  = 0
for x in range(0,4):
    nota = float(input("Informe a nota: "))
    total += nota

media = total/4

if media >= 7:
    print(f"Aprovado {media}")
else:
    print(F"Reprovado {media}")