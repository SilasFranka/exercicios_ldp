print('Vamos verificar a existencia de raízes reais em sua equação')
a = float(input('Informe LADO A '))
b = float(input('Informe LADO B '))
c = float(input('Informe LADO C '))
delta = (b **2) - (4 * a * c)
rqdel = delta **(1/2)
if delta == 0 :
    calcd = (- b + rqdel) / 2 * a
    print('Sua Equação possuí 1 raiz real e é ', calcd)
elif delta > 0:
    calcdp = (- b + rqdel) / 2 * a
    calcdn = (- b - rqdel) / 2 * a
    print('Sua Equação possuí 2 raízes reais e é ', calcdp, calcdn)
elif delta < 0 :
    print('Sua Equação não possui raízes')
