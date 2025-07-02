
class Node:

    def __init__(self, valor=None):
        self.valor = valor
        self.next = None

    def __str__(self):
        return f"Node {self.valor}"


class LinkedNode:
    """ Classe para linkar a lista """

    def __init__(self):
        self.head = None

    def insert(self, valor):
        """ Método para inserir Nós """

        novo_no = Node(valor)

        if self.head is None:
            # -- Se head for Null a lista ta vazia e inicia a head como o novo no -- #
            self.head = novo_no
        else:
            # — Se houver head, inicia uma variavel índice no ponteiro head apenas para percorrer a lista -- #
            i = self.head

            while i.next:
                # — Condição para chegar com ponteiro indice até o next ser Null (fim da lista) -- #
                i = i.next

            i.next = novo_no  # Após ponteiro indice estar no fim da lista define next para apontar para o novo Nó

        print(f"Valor {valor}")
        print(f"head {self.head}")
        print(f"next {self.head.next}")

    def show(self):
        i = self.head

        while i:
            print(f"{i.valor}", end=" -> ")
            i = i.next
        print("None")

    def reverse(self):
        """ Método para reverter a lista """

        reversed_nodes = None  # Iniciando uma variável para guardar os nós invertidos

        while self.head:
            # — Enquanto o ponteiro head não estiver em Null (fim da lista) inicia e usa uma variável para percorrer e usar os Nós -- #

            prox_no = self.head.next  # vai para o próximo Nó usando o ponteiro next
            self.head.next = reversed_nodes  # ponteiro next para de apontar para onde tava e aponta para nós invertidos
            reversed_nodes = self.head  # Nós invertidos passa a guarda o valor da antiga head
            self.head = prox_no  # Head passa a apontar para o próximo nó da lista

        self.head = reversed_nodes  # No final do loop head está em None, então ela deve apontar para lista invertida


lista = LinkedNode()

lista.insert(1)
lista.insert(2)
lista.insert(3)
lista.show()
lista.reverse()
lista.show()



