from graph import Graph

class Writer:
    '''
    Write a graph or a list of nodes into a file.
    '''
    #def write_blossom_iv(self, graph, file_location):
        #'''
        #Write a graph to a file, use the blossom IV format

        #@type: graph: graph
        #@param: graph: graph that should be written to file

        #@type: file_location: string
        #@param: location to save the file
        #'''
        #f = open(file_location, 'w')
        
        ## write number of nodes and edges
        #print('{0} {1}'.format(graph.size, graph.edge_count), file=f)
        
        ## write and edge on every line
        ## ID node_1 node_2 weight
        ##TODO: Use a more generic solution, do not just print odd_node_nr
        #for node in graph.nodes:
            #for neighbour in graph.neighbour_nodes(node):
                #edge_list = graph.edge_by_nodes(node, neighbour)
                #for edge in edge_list:
                    #print('{0} {1} {2}' \
                            #.format(node.odd_node_nr, neighbour.odd_node_nr,
                                #edge.weight), \
                                        #file=f)
        #f.close()

    def write_nodes(self, nodes, file_location):
        '''
        Writes a list of nodes into a file with their x and y coordinates

        @type nodes: list
        @param: nodes: a list of nodes.

        @type file_location: string
        @param: location to save the file
        '''
        f = open(file_location, 'w')

        for node in nodes:
            print('{0} {1} {2}'.format(node.nr, node.x, node.y), file=f)

        f.close()

    def write_matrix(self, graph, file_location):
        '''
        Write a graph to a file, edges are represented in a matrix

        @type graph: graph
        @param: graph: graph that should be written to file

        @type: file_location: string
        @param: location to save the file
        '''

        f = open(file_location, 'w')

        # sort nodes by number, because they have to be in order when we write
        # the matrix
        nodes = sorted(graph.nodes, key=lambda node: node.nr)

        # create header
        dimension = len(nodes)

        print('NAME: cities {0}'.format(dimension),file=f)
        print('TYPE: TSP', file=f)
        print('COMMENT: Semesterarbeit', file=f)
        print('DIMENSION: {0}'.format(dimension), file=f)
        print('EDGE_WEIGHT_TYPE: EXPLICIT', file=f)
        print('EDGE_WEIGHT_FORMAT: UPPER_ROW', file=f)
        print('EDGE_WEIGHT_SECTION', file=f)

        # write all distances between a node an all its neighbours on one line
        for idx, node in enumerate(nodes):
            neighbour_nodes = sorted(graph.neighbour_nodes(node), key=lambda \
                    node: node.nr)
            weight_list = list()

            for idx_inner, neighbour in enumerate(neighbour_nodes):
                # we only write the upper triangular matrix, not the full
                # matrix, so we break, when we reach the diagonal element
                if dimension-idx == idx_inner:
                    break;

                edge_list = graph.edge_by_nodes(node, neighbour)
                weight = edge_list[0].weight

                weight_list.append('{0}'.format(weight))

            # write line to file
            print(*weight_list, sep = ' ', end = '\n', file=f)

        f.close()
