arquivo = open('C:\\Users\\Pichau\\Downloads\\telefone.txt', 'r')
texto = arquivo.readlines()
nomes = []

for linha in texto:
    nomes.append(str(linha[0:50]))

nomes_ordenados = sorted(nomes)

for n in nomes_ordenados:
    print(n)

arquivo.close()