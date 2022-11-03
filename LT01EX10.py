num1 = int(input("Informe o primeiro número "))
num2 = int(input("Informe o segundo número "))

if num1 >= num2:
    calc = num1 - num2
else:
    calc = num2 - num1

print("A diferença entre ", num1," e ", num2, " é ", calc)