ht = int(input("Informe quantas horas trabalhou no mês "))
vh = int(input("Informe o valor pago por hora trabalhada "))
pdd = int(input("informe o percentual de desconto "))
den = int(input("Informe o número de dependentes "))
sal = ht * vh
ppdd = pdd / 100
cden = den * 100
salliq = (sal - (sal * ppdd)) + cden
print(" Seu salario é ", sal,"já o salario liquído é ",salliq)