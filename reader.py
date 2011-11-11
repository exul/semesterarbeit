import math

from graph import Graph
from node import Node
from edge import Edge

class Reader:
    ''' 
    Read a file and create a graph object according to the nodes and edges in
    the file.
    '''

    def graph_euler_2d(self, file_location):
        '''
        Read a file that contains nodes and theire x and y coordinats.
        Create a complete undirected graph.
        File format:
        id_node x_Position y_Position
        '''
        graph = Graph()

        #TODO: Expection Handling needed?
        nodes = list()
        f = open(file_location, 'r')

        # read id, x-coordinate and y-coordinate
        for line in f:
            node_id, node_x, node_y = line.split()
            temp_node = Node(node_x, node_y, node_id)
            nodes.append(temp_node)

        # calculate distance and add nodes and edges to the graph
        for node_1 in nodes:
            graph.add_node(node_1)
            for node_2 in nodes:
                if node_1 != node_2:
                    if not graph.contains_node(node_2):
                        graph.add_node(node_2)

                    temp_distance = math.sqrt((node_1.x - node_2.x)**2 + \
                                    (node_1.y - node_2.y)**2)
                    temp_edge = Edge(node_1, node_2, temp_distance)
                    graph.add_edge(temp_edge)
                else:
                    # break, because the graph is undirected
                    # when we add an edge it will create both directions
                    # e.g.  node_1 node_2 with weight 5 was added, then
                    #       node_2 node_1 with weight 5 is added too
                    break

        return graph

    #TODO: This part has to be improved!
    def edges_blossom_iv(self, file_location, lookup_nodes, graph_original, graph):
        '''
        Read a file that contains edges. An edge consists of two nodes. 
        Add these edges to the given graph.
        e.g. id_node_1 id_node_2
        To match ne node identifiers we need a list that contains all the nodes
        that are red from the file.
        '''
        #TODO: Find a better way to match the identifiers to the node objects
        nodes = sorted(lookup_nodes, key=lambda node: node.odd_node_nr)

        #TODO: Expection Handling needed?
        f = open(file_location, 'r')

        print('=== Debug reading mpm ===')
        first_line = True
        for line in f:
            if first_line:
                first_line = False 
            else:
                id_node_1, id_node_2 = line.split()
                node_1 = nodes[int(id_node_1)]
                node_2 = nodes[int(id_node_2)]
                #TODO: At the moment we just take the first edge
                edge_list = graph_original.edge_by_nodes(node_1, node_2)
                temp_edge = edge_list[0]
                weight = temp_edge.weight
                temp_edge = Edge(node_1, node_2, weight)
                print('From {0} to {1} with weight {2}'. \
                        format(temp_edge.node_1.label, temp_edge.node_2.label, \
                            temp_edge.weight))
                graph.add_edge(temp_edge)
        print('=== End Debug reading mpm ===')

        return graph
