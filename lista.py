<<<<<<< HEAD
=======
#Victor Hugo Macedo Silva
>>>>>>> f578e9b (first commit)

class Node:

    def __init__(self, x):
        self.x = x
        self.next = None
        self.prev = None


class Lista:

    def __init__(self):
        self.init = None
        self.tail = None

    def append(self, node):
        """
        Método para inserir um elemento no final

        :param node:
        :return:
        """
        if self.init is None:
            self.init = node
            self.tail = node
            return

        self.tail.next = node
        node.prev = self.tail
<<<<<<< HEAD
=======
        self.tail = node
>>>>>>> f578e9b (first commit)


    def add(self, node):
        """
        Inserir um elemento sempre no inicio da lista

        :param node:
        :return:
        """
        if self.init is None:
            self.init = node
            self.tail = node
            return

<<<<<<< HEAD
        node.next = self.init
        self.init = node
=======


        node.next = self.init
        self.init = node
        node.next.prev = node




>>>>>>> f578e9b (first commit)

    def __str__(self):
        str_aux = '['
        node_aux = self.init
        while(node_aux is not None):
            str_aux += str(node_aux.x) + ','
            node_aux = node_aux.next
        str_aux += ']'
        return str_aux


if __name__ == '__main__':
    lista = Lista()
    lista.add(Node(x=27))
    lista.add(Node(x=1))
<<<<<<< HEAD
    print(lista)
    lista.append(Node(x=5))
    lista.append(Node(x=19))
=======
    lista.add(Node(x=4))
    lista.add(Node(x=5))
    lista.add(Node(x=6))
    print(lista)
    lista.append(Node(x=10))
    lista.append(Node(x=15))
    lista.append(Node(x=23))
>>>>>>> f578e9b (first commit)
    print(lista)
