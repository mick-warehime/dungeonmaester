""" Module for graph representing the game world."""


class Node(object):
    def __init__(self, description = None, edge_list = None):
        self.description = None
        self.edge_list = None


class Edge(object):
    def __init__(self, first_node, second_node, category, is_directed=False):
        self._first_node = first_node
        self._second_node = second_node
        self._category = category
        self._is_directed = is_directed

    def is_directed(self):
        return self._is_directed

    def get_nodes(self):
        return self._first_node, self._second_node
