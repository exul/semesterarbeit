import math
import re

import winwin
from winwin.graph import Graph
from winwin.node import Node
from winwin.edge import Edge

class Reader:
    ''' 
    Read a file and create a graph object according to the nodes and edges in
    the file.
    '''

    def euclidean(self, file_location, node_s_nr = -1, node_t_nr = -1):
        '''
        Read a file that contains nodes and theire coordinates.
        Create a complete undirected graph.
        File format:
        ID_Node Position_1 Position_2 Position_3 ...

        @type   file_location: string
        @param  file_location: location to save the file

        @type   node_s_nr: int
        @param  node_s_nr: Number to identify node s

        @type   node_t_nr: int
        @param  node_t_nr: Number to identify node t
        '''
        graph = Graph()

        dimension = 0
        euc_dimension = 0

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
                # the first column is the node nr.
                node_nr = line_data[0]
                # all other rows are coordinates
                node_coordinates = line_data[1:]

                # check if euclidean dimensions match
                if euc_dimension != len(node_coordinates):
                    raise EuclideanDimensionMissmatchError(euc_dimension, \
                        len(node_coordinates))

                # convert coordinates to float
                node_coordinates = [float(i) for i in node_coordinates]
            else:
                line_data = line.split(':')

                if line_data[0] == 'EDGE_WEIGHT_TYPE':
                    match = re.search('\d',line_data[1])
                    euc_dimension = int(match.group(0))
                
                if line_data[0] == 'DIMENSION':
                    dimension = int(line_data[1])

                continue

            temp_node = Node(node_nr, node_coordinates)
            nodes.append(temp_node)

            # set node s
            if temp_node.nr == int(node_s_nr):
                graph.node_s = temp_node

            # set node t
            if temp_node.nr == int(node_t_nr):
                graph.node_t = temp_node

        # check if dimensions match
        if dimension != len(nodes):
            raise DimensionMissmatchError(dimension, len(nodes))


        # calculate distance and add nodes and edges to the graph
        for node_1 in nodes:
            graph.add_node(node_1)
            for node_2 in nodes:
                if node_1 != node_2:
                    if not graph.contains_node(node_2):
                        graph.add_node(node_2)

                    # calculate distance for n dimensions
                    total = 0
                    for i in range(0, len(node_1.coordinates)):
                        total += ((node_1.coordinates[i]-node_2.coordinates[i])**2)

                    temp_distance = math.sqrt(total)

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

class EuclideanDimensionMissmatchError(Exception):
    '''Exception if euclidean dimensions do not fit. '''
    def __init__(self, euc_dimension, len_node_coordinates):
        Exception.__init__(self)
        print('The coordinates don\'t match the given euclidean dimension (EDGE_WEIGHT_TYPE), euclidean dimension is {0}, but we have {1} coordinates.'.format(euc_dimension, len_node_coordinates))

class DimensionMissmatchError(Exception):
    '''Exception if dimensions do not fit. '''
    def __init__(self, dimension, len_nodes):
        Exception.__init__(self)

        print('The number of nodes doesn\'t match with the given dimension, dimension is {0}, but {1} nodes are given.'.format(dimension, len_nodes))
