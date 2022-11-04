n1 = int(input('Informe o primeiro número '))
n2 = int(input('Informe o Segundo número '))

if n1 > n2:
    calc = n1 - n2
    maior = n1
    print('A diferença entre os dois é', calc,'e o maior número é ', maior)
if n1 < n2:
    calc = n2 - n1
    maior = n2
    print('A diferença entre os dois é', calc,'e o maior número é ', maior)
else:
    print('Os números são iguais')


