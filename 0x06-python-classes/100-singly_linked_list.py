#!/usr/bin/python3
"""defines a node of a singly linked list"""


class Node:
    """
    A class that represents a singly linked list
    """

    def __init__(self, data, next_node=None):
        """
        Initialize a singly linked list instance.

        Args:
            data (int): size of the square.
            next_node: position of the square
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter method for retrieving data.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter method for setting data.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Getter method for retrieving next_node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter method for setting next_node.
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    A class that represents a singly linked list
    """
    def __init__(self):
        """Initialize"""
        self.head = None

    def sorted_insert(self, value):
        """
        inserts a new Node into the correct sorted position in the list
        """
        new_node = Node(value)
        if not self.head or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return
        current = self.head
        while current.next_node and current.next_node.data < value:
            current = current.next_node
        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        if not self.head:
            return ""
        result = ""
        current = self.head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result[:-1]
