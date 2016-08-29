""" test class for database.py module"""

import unittest
import database
import xml.etree.ElementTree as etree
from collections import defaultdict

# subclassing avoids initilization in super class (which loads data from file)
class test_database(database.database):
    def __init__(self):
        self.node_dict = defaultdict(set)
        self.edge_dict = defaultdict(defaultdict)


class GraphTest(unittest.TestCase):

    def test_node_types(self):
        xml = '<root><monster><type>beast</type></monster><item><type>rat</type></item></root>'
        root = etree.fromstring(xml)
        d = test_database()
        d.init_nodes(root)
        self.assertTrue(d.get_node_types() == ['item', 'monster'], 'didnt read in nodes correctly')

    def test_category_types(self):
        xml = '<root><monster><type>beast</type></monster><monster><type>rat</type></monster><item><type>chest</type></item></root>'
        root = etree.fromstring(xml)
        d = test_database()
        d.init_nodes(root)
        self.assertTrue(d.get_nodes_with_category('monster') == set(['beast', 'rat']), 'didnt read in node types correctly')

    def test_edge_types(self):
        xml = '<root><edge><type>has</type><node>humanoid</node><node>item</node><directed/></edge><edge><type>perk</type><node>humanoid</node></edge></root>'
        root = etree.fromstring(xml)
        d = test_database()
        d.init_edges(root)
        self.assertTrue(d.get_edge_types() == ['humanoid'], 'did not parse edge xml correctly')

    def test_read_directed_edge(self):
        xml = '<root><edge><type>has</type><node>humanoid</node><node>item</node><directed/></edge>></root>'
        root = etree.fromstring(xml)
        d = test_database()
        d.init_edges(root)
        humanoid_edges = d. get_edges_with_category('humanoid')
        item_edges = d.get_edges_with_category('item')
        self.assertTrue(humanoid_edges['item'] == ['has'], 'did not create directed edge')
        self.assertTrue(item_edges.keys() == [], 'did not create asymetrical edge')