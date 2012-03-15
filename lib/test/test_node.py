import unittest

from winwin.node import Node

class Test_Node(unittest.TestCase):

    def setUp(self):
        self.node_1 = Node(1, 3, 4)
        self.node_2 = Node(2, 5, 6)

    def test_lt(self):
        self.assertEqual(self.node_1 < self.node_2, True)
