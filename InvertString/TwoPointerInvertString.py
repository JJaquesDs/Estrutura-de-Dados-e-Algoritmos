
word: str = "O abacaxi vai entrar"


def reversa_palavra(word):

    saida: str = ""
    esquerda: int = 0  # iniciando dois ponteiros na primeira posição da String
    direita: int = 0

    while direita < len(word):

        if word[direita] != ' ':  # Se direita nao tiver uma palavra vazia
            direita += 1  #  Anda com ponteiro esquerdo
        else:
            saida += word[esquerda:direita + 1][:: - 1]  # saida recebendo os caracteres da esquerda pra direita e invertendo eles

            direita += 1  # direita pula para a próxima palavra
            esquerda = direita  #  esquerda vai para a mesma palavra que direita

    """ Quando acabar o while para concatenar a ultima palavra que ficou de fora: """

    saida += " "
    saida += word[esquerda:direita][:: -1]
    return print(f"{saida[1:]}")  # Printando a saída começando de 1 por que se nao vai pegar o espaço em branco invertido


reversa_palavra(word)
