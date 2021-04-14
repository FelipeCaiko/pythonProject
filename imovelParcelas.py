import math

valorImovel = float(input("Informe o valor do Imovel: "))
valorSalario = float(input("Informe o valor do Salario: "))
qtdParcelas = int(input("Informe a quantidade de Parcelas: "))


valorParcela = valorImovel / qtdParcelas

if valorParcela <= (valorSalario * 0.3):
    print('\n Será possivel realizar o pagamento das parcelas :)')

else:
    print('\n Não será possivel realizar o pagamento das parcelas :(')