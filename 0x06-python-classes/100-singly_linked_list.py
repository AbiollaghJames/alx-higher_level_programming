#!/usr/bin/python3
"""Define node and single linked list class"""


class Node:
    """Define Node of a singlylinked list"""

    def __init__(self, data, next_node=None):
        """Instance of a Node/Constructor"""

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get data"""

        return self.__data

    @data.setter
    def data(self, value):
        """Set data"""

        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """Define SinglyLinkedList class"""

    def __init_(self):
        """Instance of SinglyLinkedList/constructor"""

        self.__head = None

    def sorted_insert(self, value):
        """insert new node to correct position"""
