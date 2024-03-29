from winwin.node import Node
from winwin.edge import Edge
from winwin.graph import Graph
from winwin.pqueue import PQueue

class Minimum_Spanning_Tree:
    def calculate(self, graph):
        '''
        Calculate the minimum spanning tree of the given graph. 

        @type   graph: graph
        @param  graph: Graph of which the minimum spanning tree is calculated.

        @rtype  graph
        @return the minimum spanning tree
        '''
        # create emty graph to store the mst
        mst = Graph(graph.distance_lookup, graph.node_s, graph.node_t)

        # create priority queue
        neighbour_edges = PQueue()

        # take the first node as start node
        start_node = min(graph.nodes)

        # add first node to mst
        mst.add_node(start_node)

        #neighbour_edges = graph.neighbour_edges(start_node)
        for new_edge in graph.neighbour_edges(start_node):
            neighbour_edges.add_item(new_edge.weight, new_edge)
            

        # get size of the current graph
        graph_size = graph.size

        # lookup antoher edge as long as the two graphs are the same size
        while mst.size < graph_size:
            # take next edge 
            next_edge = neighbour_edges.get_top_priority()

            # remove edge from the original graph
            graph.remove_edge(next_edge)

            # if both nodes are already in the mst we skip the edge
            if not(mst.contains_node(next_edge.node_1) and \
                    mst.contains_node(next_edge.node_2)):

                # add new reachable edges to the neighbour_edges list
                if mst.contains_node(next_edge.node_1):
                    next_edges = graph.neighbour_edges(next_edge.node_2)
                    for new_edge in next_edges:
                        neighbour_edges.add_item(new_edge.weight, new_edge)

                    mst.add_node(next_edge.node_2)
                else:
                    next_edges = graph.neighbour_edges(next_edge.node_1)
                    for new_edge in next_edges:
                        neighbour_edges.add_item(new_edge.weight, new_edge)
                    mst.add_node(next_edge.node_1)

                # add edge to mst
                mst.add_edge(next_edge)
        
        return mst
