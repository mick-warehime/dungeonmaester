# coding=utf-8
""" Module for graph representing the game world."""


class Node(object):
    """
    Represents an object within the game world.

    As components it should have a description, as well as a collection of relationships (edges) to other nodes. The
    string method should spit the node’s description and its relationships. There should a method that outputs all nodes
    that the given nodes has a `contains’ relationship with, as well as the node it’s `contained in’.

    """

    def __init__(self, description=None, edge_list=None):
        self.description = None
        self.edge_list = None


class Edge(object):
    CAT_PARENT_CHILD = 0
    CAT_KNOWS = 1
    CAT_HATES = 2

    def __init__(self, first_node, second_node, category, is_directed=False):
        self._first_node = first_node
        self._second_node = second_node
        self._category = category
        self._is_directed = is_directed

    def is_directed(self):
        return self._is_directed

    def get_nodes(self):
        return self._first_node, self._second_node
