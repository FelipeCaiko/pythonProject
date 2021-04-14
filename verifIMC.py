altura = float(input('Informe sua altura:'))
peso = float(input('Informe seu peso:'))
imc = peso/(altura * altura)

print('Seu índice de massa corporal é {:.2f}'.format(imc))