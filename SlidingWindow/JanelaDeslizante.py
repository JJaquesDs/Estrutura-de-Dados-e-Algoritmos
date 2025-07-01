def maxima_substring(s: str) -> int:
    esquerda: int = 0
    direita: int = 0
    max_atual: int = 1

    counter: dict = {s[0]: 1}

    while direita < len(s) - 1:  # while operador para mover e trabalhar com o ponteiro da direita até o tamanho da string
        direita += 1

        if counter.get(s[direita]):  # Se houver um ‘item’ preenchido no ponteiro da direita
            counter[s[direita]] += 1  # Incrementa com uma instância na posição apontada pelo ponteiro direito

        else:  # Caso o ‘item’ nao tenha sido visto ja na lista, cria-se ele então com 1 instância
            counter[s[direita]] = 1

        while counter[s[direita]] == 3:  # Se houver 3 itens na janela, remove o ‘item’ do ponteiro da esquerda
            counter[s[esquerda]] -= 1
            esquerda += 1  # Move o ponteiro da esquerda para uma posição a frente

        max_atual = max(max_atual, (esquerda - direita) + 1)

    return max_atual

