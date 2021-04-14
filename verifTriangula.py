a = float(input('Informe o Primeiro lado do triângulo: '))
b = float(input('Informe o Segundo  lado do triângulo: '))
c = float(input('Informe o Terceiro lado do triângulo: '))

if (a + b < c) or (a + c < b) or (b + c < a):
    print('\n Nãoo é um triângulo')
elif (a == b) and (a == c):
    print('\n O tipo desse triângulo é: Equilatero')
elif (a == b) or (a == c) or (b == c):
    print('\n O tipo desse triângulo é: Isósceles')
else:
    print('\n O tipo desse triângulo é: Escaleno')