import math

from graph import Graph
from node import Node
from edge import Edge

class Reader:
    ''' 
    Read a file and create a graph object according to the nodes and edges in
    the file.
    '''

    def euler_2d(self, file_location, node_s_nr = None, node_t_nr = None):
        '''
        Read a file that contains nodes and theire x and y coordinats.
        Create a complete undirected graph.
        File format:
        ID_Node X_Position Y_Position

        @type   file_location: string
        @param  file_location: location to save the file

        @type   node_s_nr: int
        @param  node_s_nr: Number to identify node s

        @type   node_t_nr: int
        @param  node_t_nr: Number to identify node t
        '''
        graph = Graph()

        #TODO: Expection Handling needed?
        nodes = list()
        f = open(file_location, 'r')

        # read id, x-coordinate and y-coordinate
        for line in f:
            #TODO: Check if node_nr is an integer and the numbering is from 
            #1 to n
            node_nr, node_x, node_y = line.split()
            temp_node = Node(node_nr, node_x, node_y)
            nodes.append(temp_node)

            # set node s
            #TODO: Check if node_s_nr is an integer
            if temp_node.nr == int(node_s_nr):
                graph.node_s = temp_node

            # set node t
            #TODO: Check if node_t_nr is an integer
            if temp_node.nr == int(node_t_nr):
                graph.node_t = temp_node

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
