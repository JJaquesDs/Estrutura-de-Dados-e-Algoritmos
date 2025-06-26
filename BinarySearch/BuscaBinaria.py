def busca_binaria(array, busca):
    esquerda_point: int = 0
    direita_point = len(array)  #  Iniciando o ponteiro da esquerda no final do array
    passos: int = 0

    while esquerda_point < direita_point:

        passos += 1

        meio_point = int((esquerda_point + direita_point) / 2)  # transformando o ponteiro do meio em um inteiro

        print(f"Esquerda {esquerda_point}")
        print(f"Meio {meio_point}")
        print(f"Direita {direita_point}")
        print(f"passos {passos}")

        if meio_point == busca or array[meio_point] == busca:  # Se a posição do ponteiro do meio no array, for o número buscado

            print(f"O numero de passos foi {passos}, numero buscado {busca}")
            return 0

        elif busca > array[meio_point]:
            esquerda_point = meio_point + 1  #  +1 para satisfazer uma condição de parada
        else:
            direita_point = meio_point

    return -1


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
busca = int(input(f"Digite um numero para buscar no array crescente e ordenado de {len(array)} elementos\n"))
busca_binaria(array, busca)
