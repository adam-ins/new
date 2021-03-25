nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))

mitjana = (nota1 + nota2 + nota3) / 3

print("Mitjana: " + str(round(mitjana, 1)))

if mitjana < 5:
    print("Supès")
elif mitjana < 7:
    print("Suficient")
elif mitjana < 9:
    print("Notable")
else:
    print("Excel·lent")