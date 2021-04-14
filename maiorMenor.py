primeiro = int(input('Informe o valor de A: '))
segundo  = int(input('Informe o valor de B: '))
terceiro = int(input('Informe o valor de A: '))

maior = primeiro

if (segundo > maior):
        maior = segundo
if (terceiro > maior):
        maior = terceiro

print('Maior número informado: ',maior)
menor = primeiro

if (segundo < menor):
    menor = segundo
if (terceiro < menor):
    menor = terceiro

print('Menor número informado: ',menor)