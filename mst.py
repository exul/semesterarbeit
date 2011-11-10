import random

from node import Node
from edge import Edge
from graph import Graph

#my_node1 = Node(1,1)
#my_node2 = Node(1,2)
#my_node3 = Node(1,3)
#my_node4 = Node(1,4)
#my_node5 = Node(1,5)
#my_node6 = Node(1,6)
#my_node7 = Node(1,7)

#self.graph = Graph()

#self.graph.add_node(my_node1)
#self.graph.add_node(my_node2)
#self.graph.add_node(my_node3)
#self.graph.add_node(my_node4)
#self.graph.add_node(my_node5)
#self.graph.add_node(my_node6)
#self.graph.add_node(my_node7)

#my_edge1 = Edge(my_node1, my_node2, 7)
#my_edge2 = Edge(my_node1, my_node4, 5)
#my_edge3 = Edge(my_node2, my_node3, 8)
#my_edge4 = Edge(my_node2, my_node4, 9)
#my_edge5 = Edge(my_node2, my_node5, 7)
#my_edge6 = Edge(my_node3, my_node5, 5)
#my_edge7 = Edge(my_node4, my_node5, 15)
#my_edge8 = Edge(my_node4, my_node6, 6)
#my_edge9 = Edge(my_node5, my_node6, 8)
#my_edge10 = Edge(my_node5, my_node7, 9)
#my_edge11 = Edge(my_node6, my_node7, 11)

#self.graph.add_edge(my_edge1)
#self.graph.add_edge(my_edge2)
#self.graph.add_edge(my_edge3)
#self.graph.add_edge(my_edge4)
#self.graph.add_edge(my_edge5)
#self.graph.add_edge(my_edge6)
#self.graph.add_edge(my_edge7)
#self.graph.add_edge(my_edge8)
#self.graph.add_edge(my_edge9)
#self.graph.add_edge(my_edge10)
#self.graph.add_edge(my_edge11)

class Minimum_Spanning_Tree:
    
    def __init__(self, graph):
        self.graph = graph

    def calculate(self):
        # create emty graph to store the mst
        mst = Graph()

        # take the first node as start node (it doesn't matter which one)
        #start_node = self.graph.nodes[0]
        start_node = random.choice(self.graph.nodes)

        # add first node to mst
        mst.add_node(start_node)

        neighbour_edges = self.graph.neighbour_edges(start_node)

        # get size of the current graph
        graph_size = self.graph.size

        while mst.size < graph_size:
            # sort edges according to their weight
            neighbour_edges = sorted(neighbour_edges, key=lambda edge: edge.weight)
            
            # take next edge (we can take the first element of the list, because the
            # list is sorted
            next_edge = neighbour_edges[0]

            # remove edge from the original graph
            self.graph.remove_edge(next_edge)

            # remove edge from neighbours list
            # we have to remove all occurence of the edge, in an undirected graph the
            # same edge meight be added multiple times to neighbour_edges
            #TODO: There meight be a faster solution
            while next_edge in neighbour_edges:
                neighbour_edges.remove(next_edge)
            
            # if both nodes are already in the mst we skip the edge
            if not(mst.contains_node(next_edge.node_1) and \
                    mst.contains_node(next_edge.node_2)):
                # add new reachable edges to the edge_neighbours list
                if mst.contains_node(next_edge.node_1):
                    neighbour_edges = neighbour_edges + self.graph.neighbour_edges(next_edge.node_2)

                    mst.add_node(next_edge.node_2)
                else:
                    neighbour_edges = neighbour_edges + self.graph.neighbour_edges(next_edge.node_1)
                    mst.add_node(next_edge.node_1)

                # add edge to mst
                mst.add_edge(next_edge)

        #TODO: Remove debug output
        '''
            Just debug output, not needed in production
        '''
        print('============= Debug =============')
        # get edges that are in the mst
        mst_edges = set()
        for edge in mst.edges:
            mst_edges.add(edge)

        for edge in mst_edges:
            print('Distance from Node {0} to Node {1} is {2}' \
                    .format(edge.node_1.label,edge.node_2.label, edge.weight))

        return mst
