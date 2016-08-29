import xml.etree.ElementTree as etree
from collections import defaultdict
import random

import numpy as np

# update this to take to be init_nodes(root) to make it testable

class database():
    NODES_FILES = ['data/beastiary.xml', 'data/items.xml']
    EDGE_FILES = ['data/edges.xml']

    def __init__(self):
        self.node_dict = defaultdict(set)
        for node_file in database.NODES_FILES:
            root = etree.parse(node_file).getroot()
            self.init_nodes(root)

        self.edge_dict = defaultdict(defaultdict)
        for edge_file in database.EDGE_FILES:
            root = etree.parse(edge_file).getroot()
            self.init_edges(root)

    def init_nodes(self, root):

        for child in root:
            node = child.tag
            category = child.find('type').text
            self.node_dict[node].add(category)

    def init_edges(self, root):

        for child in root:
            edge_type = child.find('type').text

            nodes = []
            for n in child.findall('node'):
                nodes.append(n.text)

            is_directed = child.find('directed') is not None
            if is_directed:
                self.add_directed_edge(edge_type, *nodes)
            else:
                self.add_edge(edge_type, *nodes)

    def add_edge(self, edge_type, first_node, second_node = None):
        self.add_directed_edge(edge_type, first_node, second_node)
        if second_node:
            self.add_directed_edge(edge_type, second_node, first_node)

    def add_directed_edge(self, edge_type, first_node, second_node = None):
        if second_node in self.edge_dict[first_node]:
            self.edge_dict[first_node][second_node].append(edge_type)
        else:
            self.edge_dict[first_node][second_node] = [edge_type]

    def get_node_types(self):
        return list(self.node_dict.iterkeys())

    def get_category_types(self, category):
        return self.node_dict[category]

    def get_edges(self):
        return list(self.edge_dict.iterkeys())

    def get_edges_with_type(self, type):
        return self.edge_dict[type]

    def random_node(self):
        return random.choice(self.get_nodes())

    def random_edge(self, node):
        random_node = random.choice(self.edge_dict[node].keys())
        random_edge = random.choice(self.edge_dict[node][random_node])
        return (random_node, random_edge)

    def random_connection(self):
        random_node = random.choice(self.edge_dict.keys())
        another_random_node = random.choice(self.edge_dict[random_node].keys())
        random_edge = random.choice(self.edge_dict[random_node][another_random_node])
        return (random_node, another_random_node, random_edge)
