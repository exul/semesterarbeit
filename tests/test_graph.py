import unittest

from reader import Reader
from node import Node
from edge import Edge
from graph import Graph

class Test_Graph(unittest.TestCase):

    def setUp(self):
        self.reader = Reader()
        
    def test_add_node(self):
        graph = self.reader.euler_2d('../data/in/eil51.tsp')
        size_before = graph.size
        node = Node(size_before, 999, 999, 'test_node')
        graph.add_node(node)
        size_after = graph.size
       
        self.assertEqual(size_before, 51)
        self.assertEqual(size_after, 52)

    def test_add_edge(self):
        graph = self.reader.euler_2d('../data/in/eil51.tsp')
        size = graph.size
        node_1 = Node(size, 998, 998, 'test_node_1')
        size = graph.size
        node_2 = Node(size, 999, 999, 'test_node_2')

        edge = Edge(node_1, node_2, 999)


        graph.add_node(node_1) 
        graph.add_node(node_2) 

        contains_before = graph.contains_edge(edge.node_1, edge.node_2)

        graph.add_edge(edge)

        contains_after = graph.contains_edge(edge.node_1, edge.node_2)

        self.assertFalse(contains_before)
        self.assertTrue(contains_after)

    def test_remove_edge(self):
        graph = self.reader.euler_2d('../data/in/eil51.tsp')
        nodes = graph.nodes

        node_1 = nodes[0]
        node_2 = nodes[1]

        edge = graph.edge_by_nodes(node_1, node_2)[0]

        contains_before = graph.contains_edge(edge.node_1, edge.node_2)

        graph.remove_edge(edge)

        contains_after = graph.contains_edge(edge.node_1, edge.node_2)

        self.assertTrue(contains_before)
        self.assertFalse(contains_after)

    def test_neighbours_nodes(self):
        graph = self.reader.euler_2d('../data/in/eil51.tsp')
        node = graph.nodes[0]

        neighbours = graph.neighbour_nodes(node)
        neighbours_size = len(neighbours)
        neighbour_list = list(neighbours)
        neighbour_list = sorted(neighbour_list, key=lambda node: node.nr)

        # there have to be 50 neighbours nodes, because it is a complete graph
        self.assertEqual(neighbours_size, 50)

        node_nr = 1
        for neighbour in neighbour_list:
            if node.nr == node_nr:
                node_nr += 1
                next

            self.assertEqual(neighbour.nr, node_nr)
            node_nr += 1

    def test_size(self):
        graph = self.reader.euler_2d('../data/in/eil51.tsp')
        size = graph.size
        self.assertEqual(size, 51)

