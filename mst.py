import random

from node import Node
from edge import Edge
from graph import Graph

class Minimum_Spanning_Tree:
    def calculate(self, graph):
        '''
        Calculate the minimum spanning tree of the given graph. 

        @type: graph: graph
        @param: graph: Graph of which the minimum spanning tree is calculated.

        @rtype: graph
        @return: the minimum spanning tree
        '''
        # create emty graph to store the mst
        mst = Graph()

        # take the first node as start node (it doesn't matter which one)
        start_node = random.choice(graph.nodes)

        # add first node to mst
        mst.add_node(start_node)

        neighbour_edges = graph.neighbour_edges(start_node)

        # get size of the current graph
        graph_size = graph.size

        # lookup antoher edge as long as the two graphs are the same size
        while mst.size < graph_size:
            # sort edges according to their weight
            neighbour_edges = sorted(neighbour_edges, key=lambda edge: edge.weight)
            
            # take next edge (we can take the first element of the list, because the
            # list is sorted)
            next_edge = neighbour_edges[0]

            # remove edge from the original graph
            graph.remove_edge(next_edge)

            # remove edge from neighbours list
            # we have to remove all occurence of the edge, in an undirected graph the
            # same edge meight be added multiple times to neighbour_edges
            #TODO: There meight be a faster solution
            while next_edge in neighbour_edges:
                neighbour_edges.remove(next_edge)
            
            # if both nodes are already in the mst we skip the edge
            if not(mst.contains_node(next_edge.node_1) and \
                    mst.contains_node(next_edge.node_2)):
                # add new reachable edges to the neighbour_edges list
                if mst.contains_node(next_edge.node_1):
                    neighbour_edges = neighbour_edges + graph.neighbour_edges(next_edge.node_2)

                    mst.add_node(next_edge.node_2)
                else:
                    neighbour_edges = neighbour_edges + graph.neighbour_edges(next_edge.node_1)
                    mst.add_node(next_edge.node_1)

                # add edge to mst
                mst.add_edge(next_edge)

        return mst
