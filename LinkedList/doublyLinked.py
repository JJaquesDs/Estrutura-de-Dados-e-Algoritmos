class Node:
    """ Classe base do Nó """

    def __init__(self, valor):
        """ Construtor """
        self.valor = valor
        self.front = None
        self.back = None

    def __str__(self):
        """ Função só para imprimir o Node formatado """
        return f"Node {self.valor}"


class DuploLink:
    """ Classe dos links head e tail """

    def __init__(self):
        """ Construtor de head e tail """
        self.head = None
        self.tail = None

    def adicionar_ini(self, valor):

        """ Adicionar no inicio """

        novo_no = Node(valor)  # instânciando objeto da classe Node
        novo_no.back = self.head  # set do ponteiro de trás para apontar para a antiga head
        print(f" Adicionado {valor}")

        if self.head:
            # — Se tiver um head, ponteiro da frente desse head sai de onde ele tava apontando e aponta pro novo nó -- #
            self.head.front = novo_no

        else:
            # — Se não existir head, não existe tail e a lista estará fazia, então o tail receberá o novo nó -- #
            self.tail = novo_no

        self.head = novo_no  # Fazendo a head virar o novo nó
        print(f" Head {self.head}")
        print(f" Tail {self.tail}")

    def adicionar_fim(self, valor):

        """ Adiconar no fim """

        novo_no = Node(valor)
        novo_no.front = self.tail  # set do ponteiro da frente para apontar para o tail
        print(f" Adicionado {valor}")

        if self.tail:
            # -- Se existir um tail, define o ponteiro de trás desse tail para apontar para o novo nó -- #
            self.tail.back = novo_no
        else:
            # --  Se nao existir tail, nao existe head, entao define head como o novo nó -- #
            self.head = novo_no

        self.tail = novo_no  # define tail  como o novo nó
        print(f" Head {self.head}")
        print(f" Tail {self.tail}")

    def remover_inicio(self):
        """ Removendo do início """

        if not self.head:
            # — Condição para retornar e impedir o funcionamento do método caso a lista esteja vazia -- #
            return None and f"Nao existe valor para ser tirado"

        self.head = self.head.back  # definindo o head para o node anterior a ele usando o ponteiro de trás do antigo head

        if self.head:
            # -- Se existir head, define o ponteiro da frente para apontar para Null e desvincular o Node removido da lista - #
            self.head.front = None
        else:
            # — Se não existir head não existe tail, então define tail para Null -- #
            self.tail = None
        print(f" Head {self.head}")
        print(f" Tail {self.tail}")

    def remover_fim(self):
        """ Remover do fim """

        if not self.tail:
            return None and f"Nao existe valor para ser tirado"

        self.tail = self.tail.front  # definindo tail para o Node anterior usando o ponteiro da frente do antigo tail

        if self.tail:
            # -- Se existir tail, define o ponteiro de trás para apontar para Null e desvincular o Node removido da lista - #
            self.tail.back = None
        else:
            # — Se não existir tail não existe head, então define head para Null -- #
            self.head = None

        print(f" Head {self.head}")
        print(f" Tail {self.tail}")

    def mostrar(self):
        """ Mostrar a lista """

        atual = self.head  # variável para guardar head

        while atual:
            # -- " <-> " para representar "front" e "back" -- #
            print(f"{atual.valor}", end=" <-> ")
            atual = atual.back  # definindo atual como atual.back para sempre percorrer os Nodes um Node anterior usando o ponteiro de trás

        print("None")  # fim da lista


lista = DuploLink()

lista.adicionar_ini(1)
lista.adicionar_ini(2)
lista.adicionar_ini(3)
lista.adicionar_ini(4)
lista.adicionar_fim(0)
lista.mostrar()
lista.remover_inicio()
lista.mostrar()
lista.remover_fim()
lista.mostrar()
lista.remover_fim()
lista.mostrar()
