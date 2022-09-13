#!/usr/bin/python3
""" Single """


class Node:
    """ Singly linked list """
    def __init__(self, data, next_node=None):
        """the init method """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """getter """
        return self.__data

    @data.setter
    def data(self, value):
        """setter """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """getter """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """setter """
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

    def __str__(self):
        """String """
        return str(self.__data)


class SinglyLinkedList:
    """singly-linked list"""

    def __init__(self):
        """Initalize a new SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert New Node """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """String """
        string = ""
        tmp = self.__head
        while tmp is not None:
            string += str(tmp)
            if tmp.next_node is not None:
                string += "\n"
            tmp = tmp.next_node
        return string
