import unittest

from winwin.edge import Edge
from winwin.reader import Reader
from winwin.writer import Writer
from winwin.mst import Minimum_Spanning_Tree
from winwin.matcher import Matcher
from winwin.euler import Euler
from winwin.generator import Generator

class Test_Euler(unittest.TestCase):

    def setUp(self):
        reader = Reader()
        graph_tsp = reader.euclidean('data/in/christofides.tsp')
        graph_hpp = reader.euclidean('data/in/christofides.tsp', 1, 39) 

        mst = Minimum_Spanning_Tree()
        graph_tsp = mst.calculate(graph_tsp)
        graph_hpp = mst.calculate(graph_hpp)

        matcher = Matcher()
        self.graph_tsp = matcher.calculate(graph_tsp)

        node_s = graph_hpp.node_s
        node_t = graph_hpp.node_t
        weight = graph_hpp.lookup_distance(node_s, node_t)[0]

        if not graph_hpp.contains_edge(node_s, node_t):
            edge_st = Edge(node_s, node_t, weight)
            graph_hpp.add_edge(edge_st)

        self.graph_hpp = matcher.calculate(graph_hpp)

        self.euler = Euler()

    def test_calculate(self):
        euler_nodes_tsp = self.euler.calculate(self.graph_tsp)
        euler_nodes_hpp = self.euler.calculate(self.graph_hpp, False)

        euler_cost_tsp = 0
        euler_cost_hpp = 0

        for i in range(len(euler_nodes_tsp)):
            if i > 0:
                euler_cost_tsp += self.graph_tsp.lookup_distance(euler_nodes_tsp[i-1], euler_nodes_tsp[i])[0]

        for i in range(len(euler_nodes_hpp)):
                    if i > 0:
                        euler_cost_hpp += self.graph_hpp.lookup_distance(euler_nodes_hpp[i-1], euler_nodes_hpp[i])[0]

        self.assertEqual(euler_cost_hpp, 7490)

