# coding=utf-8
""" Module for graph representing the game world."""

import enum


class Node(object):
    """
    Represents an object within the game world.

    As components it should have a description, as well as a collection of relationships (edges) to other nodes. The
    string method should spit the node’s description and its relationships. There should a method that outputs all nodes
    that the given nodes has a `contains’ relationship with, as well as the node it’s `contained in’.

    """

    def __init__(self, description=None, edge_list=None):
        self._description = None
        self._edge_list = None


class Edge(object):
    """
    Represents a relationship between two objects (nodes) in the game world.

    It should have a description, as well as information about what nodes it relates. The edge can be directed.
    There should be a method that spits out a string describing the relationship....
    """

    CATEGORIES = enum.enum(PARENT_CHILD=0, KNOWS=1, HATES=2)
    _descriptions = {CATEGORIES.PARENT_CHILD: " contains ",
                     CATEGORIES.KNOWS: " knows of ",
                     CATEGORIES.HATES: " hates "}

    def __init__(self, first_node, second_node, category, is_directed=False):
        # type: (Node, Node, int, bool) -> object

        if not isinstance(first_node, Node):
            raise (TypeError("Expected Node input, got input type %s\n" % (str(type(first_node)))))
        if not isinstance(second_node, Node):
            raise (TypeError("Expected Node input, got input type %s\n" % (str(type(second_node)))))
        if not isinstance(category, int):
            raise (TypeError("Expected int input, got input type %s\n" % (str(type(category)))))
        if not isinstance(is_directed, bool):
            raise (TypeError("Expected bool input, got input type %s\n" % (str(type(is_directed)))))

        self._first_node = first_node
        self._second_node = second_node
        self._category = category
        self._is_directed = is_directed

    def is_directed(self):
        return self._is_directed

    def get_nodes(self):
        return self._first_node, self._second_node

    def get_category(self):
        return self._category

    def get_description(self):
        return Edge._descriptions[self._category]
