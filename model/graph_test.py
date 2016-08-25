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
