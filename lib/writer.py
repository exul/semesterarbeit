from graph import Graph

class Writer:
    '''
    Write a graph or a list of nodes into a file.
    '''
#    def write_blossom_iv(self, graph, file_location):
#        '''
#        Write a graph to a file, use the blossom IV format
#
#        @type  graph: graph
#        @param graph: graph that should be written to file
#
#        @type  file_location: string
#        @param     location to save the file
#        '''
#        f = open(file_location, 'w')
#        
#        # write number of nodes and edges
#        print('{0} {1}'.format(graph.size, graph.edge_count), file=f)
#        
#        # write and edge on every line
#        # ID node_1 node_2 weight
#        #TODO: Use a more generic solution, do not just print odd_node_nr
#        for node in graph.nodes:
#            for neighbour in graph.neighbour_nodes(node):
#                edge_list = graph.edge_by_nodes(node, neighbour)
#                for edge in edge_list:
#                    print('{0} {1} {2}' \
#                            .format(node.odd_node_nr, neighbour.odd_node_nr,
#                                edge.weight), \
#                                        file=f)
#        f.close()

    def write_nodes(self, nodes, file_location):
        '''
        Writes a list of nodes into a file with their x and y coordinates

        @type   nodes: list
        @param  nodes: a list of nodes.

        @type   file_location: string
        @param  file_location: location to save the file
        '''
        f = open(file_location, 'w')

        for node in nodes:
            print('{0} {1} {2}'.format(node.nr, node.x, node.y), file=f)

        f.close()

    def write_edges(self, graph, file_location):
        '''
        Write all edges of a graph into a file. The file format is 
        node_1 node_2 weight, so each line contains one edge.

        @type   graph: graph
        @param  graph: graph that contains the edges

        @type   file_location: string
        @param  file_location: location to save the file
        '''
        f = open(file_location, 'w')
        edges = graph.edges

        for idx, edge in enumerate(edges):
            print('{0} {1} {2}' \
                .format(edge.node_1.nr, edge.node_2.nr, edge.weight), file=f)


    def write_matrix(self, graph, file_location, dummy_city=False):
        '''
        Write a graph to a file, edges are represented in a matrix

        @type   graph: graph
        @param  graph: graph that should be written to file

        @type   file_location: string
        @param  location to save the file
        '''

        f = open(file_location, 'w')

        # sort nodes by number, because they have to be in order when we write
        # the matrix
        nodes = sorted(graph.nodes, key=lambda node: node.nr)

        # create header
        dimension = len(nodes)

        if dummy_city:
            dimension += 1

        print('NAME: cities {0}'.format(dimension),file=f)
        print('TYPE: TSP', file=f)
        print('COMMENT: Semesterarbeit', file=f)
        print('DIMENSION: {0}'.format(dimension), file=f)
        print('EDGE_WEIGHT_TYPE: EXPLICIT', file=f)
        print('EDGE_WEIGHT_FORMAT: UPPER_ROW', file=f)
        print('EDGE_WEIGHT_SECTION', file=f)

        # write dummy city if needed (to calculate hpp instead of tsp)
        # TODO: Not really nice
        if dummy_city:
            for i in range(dimension-1):
                print('0',end=" ",file=f)
            print('',file=f)

        # write all distances between a node an all its neighbours on one line
        for idx, node in enumerate(nodes):
            neighbour_nodes = sorted(graph.neighbour_nodes(node), key=lambda \
                    node: node.nr)
            weight_list = list()

            for idx_inner, neighbour in enumerate(neighbour_nodes):
                edge_list = graph.edge_by_nodes(node, neighbour)
                weight = edge_list[0].weight

                if node.nr < neighbour.nr:
                    weight_list.append('{0}'.format(weight))

            # write line to file
            print(*weight_list, sep = ' ', end = '\n', file=f)

        f.close()
