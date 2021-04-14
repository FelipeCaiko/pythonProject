nomes = []
avaliacoes = []
generos = []

n1=1

while True:
    opcao = input("\nMenu de opções: \n1 - Inserir Filme e Avaliações  \n2 - Listar Filmes e Avaliações  \n3 - Remover Filme e Avaliações  \n4 - Imprimir Relátorio  \n5 - Sair\n\n **INFORME NÚMERO OPÇÃO DESEJADA: ")

    if (opcao == "1"):
        nome = input('Informe o nome de um filme que gostaria de cadastrar: ')
        nomes.append(nome)
        genero= input('Informe o genêro do filme informado: ')
        generos.append(genero)

        while True:
            avaliacao = int(input("Insira a avaliação: "))
            if avaliacao>10:
                avaliacoes.append(avaliacao)

            break

    if (opcao == "2"):

        i=0

        while i < len(nomes):
            print("Nome: " + nomes[i] + "\nGenêro: " + generos[i] + "\nAvaliação: " + avaliacoes[i])
            i=i+1

    if (opcao == "3"):
        for a , d in enumerate(nomes):
            print(f'Posição:{a}\n' , d)
            n1 = int(input("Qual filme você deseja remover da lista?: "))
            del (nomes[n1])
            print("O filme escolhido foi: " , nome)
        if (opcao == "0"):
            break

    if (opcao == "4"):

        arq = open("filme.txt", "w")
        print("Relatório gerado com sucesso")
        if (opcao == "0"):
            break

    if (opcao == "5"):
        break
