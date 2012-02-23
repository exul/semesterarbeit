import math

from graph import Graph
from node import Node
from edge import Edge

class Reader:
    ''' 
    Read a file and create a graph object according to the nodes and edges in
    the file.
    '''

    def euler_2d(self, file_location, node_s_nr = -1, node_t_nr = -1):
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
            line_data = line.split()

            # skip header information
            if line_data[0].isdigit():
                #TODO: Check if node_nr is an integer and the numbering is from 
                #1 to n
                node_nr, node_x, node_y = line_data
            else:
                continue

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

        f.close()

        return graph

    def solution(self, file_location, nodes, is_tsp = True):
        f = open(file_location, 'r')
        solution_numbers = list()
        solution_nodes = list()

        first = True

        for line in f:
            if first:
                first = False
            else:
                line_data = line.split()
                solution_numbers += line_data

#        if len(solution_numbers) <= len(nodes):
#            offset = 1
#            print('Solution is longer, it\' an TSP')
#        else:
#            offset = 0
        if is_tsp:
            offset = 1
        else:
            offset = 0

        print('Solution: {0}'.format(len(solution_numbers)))
        print('Nodes: {0}'.format(len(nodes)))

        is_first = True

        for solution_number in solution_numbers:
            for node in nodes:
                if node.nr == int(solution_number)+offset:
                    if is_first:
                        first_node = node
                        is_first = False

                    solution_nodes.append(node)

        if is_tsp:
            solution_nodes.append(first_node)

        return solution_nodes
