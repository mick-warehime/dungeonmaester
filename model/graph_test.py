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

        return graph.Edge(node_1, node_2, graph.Edge.CATEGORIES.PARENT_CHILD, is_directed = True)

    def test_edge_is_directed_default_false(self):
        edge = graph.Edge(graph.Node(),graph.Node(),graph.Edge.CATEGORIES.PARENT_CHILD)

        self.assertTrue(not edge.is_directed(), "Expected False, got %s" % str(edge.is_directed()))

    def test_edge_returns_nodes(self):
        node_1 = graph.Node()
        node_2 = graph.Node()

        edge = graph.Edge(node_1, node_2, graph.Edge.CATEGORIES.PARENT_CHILD)

        actual_left, actual_right = edge.get_nodes()
        expected_left = node_1
        expected_right = node_2

        self.assertEqual(expected_left, actual_left, "Expected %s, got %s" % (str(expected_left), str(actual_left)))
        self.assertEqual(expected_right, actual_right, "Expected %s, got %s" % (str(expected_right), str(actual_right)))

    def test_edge_wrong_input_types_throw_exception(self):
        self.assertRaises(TypeError, graph.Edge, None, graph.Node(), 0)
        self.assertRaises(TypeError, graph.Edge, graph.Node(), None, 0)
        self.assertRaises(TypeError, graph.Edge, graph.Node(), graph.Node(), None)
        self.assertRaises(TypeError, graph.Edge, graph.Node(), graph.Node(), 0, is_directed=3)

    def test_edge_correct_description(self):
        edge = self._basic_edge()
        expected = " contains "
        actual = edge.get_description()

        self.assertEqual(expected, actual)
