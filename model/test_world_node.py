import unittest
import world_node as wn

class MainTestCase(unittest.TestCase):

    def test_create_empty_node(self):
        n = wn.WorldNode()
        self.assertEqual(n.get_classifier(), wn.NODE_CLASSIFIERS.NONE, 'did not create an empty node')

    def test_create_NPC(self):
        n = wn.WorldNode(wn.NODE_CLASSIFIERS.NPC)
        self.assertEqual(n.get_classifier(), wn.NODE_CLASSIFIERS.NPC, 'created NPC successfully')


