ang1 = int(input("Informe o primeiro Angulo "))
ang2 = int(input("Informe o Segundo Angulo "))

if (ang1 + ang2) >= 180:
    print("Não é valido esses valores de angulos")
else:
    calc = 180 - (ang1 + ang2)
    print("O valor do terceiro angulo é ", calc)