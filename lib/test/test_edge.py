import unittest

from winwin.node import Node
from winwin.edge import Edge

class Test_Node(unittest.TestCase):

    def setUp(self):
        self.node_1 = Node(1, 2, 3)
        self.node_2 = Node(2, 3, 4)
        self.node_3 = Node(3, 4, 5)
        self.node_4 = Node(4, 5, 6)
        self.node_5 = Node(5, 6, 7)
        self.node_6 = Node(6, 7, 8)
        self.edge_1 = Edge(self.node_1, self.node_2, 20)
        self.edge_2 = Edge(self.node_3, self.node_4, 40)
        self.edge_3 = Edge(self.node_5, self.node_6, 40)

    def test_lt(self):
        self.assertEqual(self.edge_1 < self.edge_2, True)
        self.assertEqual(self.edge_2 < self.edge_3, True)
