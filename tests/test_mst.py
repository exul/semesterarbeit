import unittest

from reader import Reader
from mst import Minimum_Spanning_Tree

class Test_MST(unittest.TestCase):

    def setUp(self):
        self.reader = Reader()
        self.mst = Minimum_Spanning_Tree()

    def test_length(self):
        self.graph = self.reader.euler_2d('../data/in/eil51.tsp')
        graph = self.mst.calculate(self.graph)

        length = 0
        for edge in graph.edges:
            length += edge.weight

        self.assertEqual(length, 750)
