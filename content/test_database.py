""" test class for database.py module"""

import unittest
import database
import xml.etree.ElementTree as etree
from collections import defaultdict

# subclassing avoids initilization in super class (which loads data from file)
class test_database(database.database):
    def __init__(self):
        self.node_dict = defaultdict(set)

class GraphTest(unittest.TestCase):

    def test_category_types(self):
        xml = '<root><monster><type>beast</type></monster><monster><type>rat</type></monster><item><type>chest</type></item></root>'
        root = etree.fromstring(xml)
        d = test_database()
        d.init_nodes(root)
        self.assertTrue(d.get_category_types('monster') == set(['beast', 'rat']), 'didnt read in node types correctly')

    def test_node_types(self):
        xml = '<root><monster><type>beast</type></monster><item><type>rat</type></item></root>'
        root = etree.fromstring(xml)
        d = test_database()
        d.init_nodes(root)
        self.assertTrue(d.get_node_types() == ['item', 'monster'], 'didnt read in nodes correctly')
