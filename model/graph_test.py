""" test class for graph.py module"""

import unittest

import graph


class GraphTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_edge_is_directed_default_false(self):
        edge = graph.Edge(None, None, None)

        self.assertTrue(not edge.is_directed(), "Expected False, got %s" % str(edge.is_directed()))

    def test_edge_returns_nodes(self):
        edge = graph.Edge(1, 2, None)

        actual_left, actual_right = edge.get_nodes()
        expected_left = 1
        expected_right = 2

        self.assertEqual(expected_left, actual_left, "Expected %d, got %d" % (expected_left, actual_left))
        self.assertEqual(expected_right, actual_right, "Expected %d, got %d" % (expected_right, actual_right))
