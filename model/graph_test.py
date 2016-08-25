""" test class for graph.py module"""

import unittest

import graph


class GraphTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def _basic_edge(self):

        node_1 = graph.Node()
        node_2 = graph.Node()

        return graph.Edge(node_1,node_2,graph.Edge.CATEGORIES.PARENT_CHILD)

    def test_edge_is_directed_default_false(self):
        edge = self._basic_edge()

        self.assertTrue(not edge.is_directed(), "Expected False, got %s" % str(edge.is_directed()))

    def test_edge_returns_nodes(self):
        node_1 = graph.Node()
        node_2 = graph.Node()

        edge = graph.Edge(node_1, node_2, None)

        actual_left, actual_right = edge.get_nodes()
        expected_left = node_1
        expected_right = node_2

        self.assertEqual(expected_left, actual_left, "Expected %s, got %s" % (str(expected_left), str(actual_left)))
        self.assertEqual(expected_right, actual_right, "Expected %s, got %s" % (str(expected_right), str(actual_right)))
