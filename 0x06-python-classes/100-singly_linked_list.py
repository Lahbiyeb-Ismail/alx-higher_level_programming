#!/usr/bin/python3
"""Singly Linked List"""


class Node:
    """Represents a node in a singly linked list"""

    def __init__(self, data, next_node=None):
        """Initialize node with data and link to next node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get the data stored in the node"""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data stored in the node
        Data must be an integer"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get the next node linked to this node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node linked to this node
        Must be a Node object or None"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Singly linked list data structure"""

    def __init__(self):
        """Create empty linked list"""
        self.head = None

    def __str__(self):
        """Print entire linked list"""
        values = []
        node = self.head
        while node is not None:
            values.append(str(node.data))
            node = node.next_node
        return "\n".join(values)

    def sorted_insert(self, value):
        """Insert node with specified value in sorted order"""
        new_node = Node(value)
        if self.head is None or self.head.data >= new_node.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while (
                current.next_node is not None and current.next_node.data < new_node.data
            ):
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
