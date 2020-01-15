soma = 0
nidt = 0
n = int(input('digite o numero maximo:'))
for n in range(1,n+1,2):
    if n % 3 == 0:
        nidt = nidt + 1
        soma = soma + n
print('A soma de todos os {} valores é {}'.format(nidt,soma), end=' ')