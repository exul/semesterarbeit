from graph import Graph

class Writer:
    '''
    Write a graph into file.
    '''
    def write_blossom_iv(self, graph, file_location):
        '''
        Write a graph to a file, use the blossom IV format

        @type: graph: graph
        @param: graph: graph that should be written to file

        @type: file_location: string
        @param: string that contains the file location

        @rtype: boolean
        @return: True, if the file was written successfully and False if
        someting went wrong
        '''
        f = open(file_location, 'w')
        
        # write number of nodes and edges
        print('{0} {1}'.format(graph.size, graph.edge_count), file=f)
        
        # write and edge on every line
        # ID node_1 node_2 weight
        #TODO: Use a more generic solution, do not just print odd_node_nr
        for node in graph.nodes:
            for neighbour in graph.neighbour_nodes(node):
                edge_list = graph.edge_by_nodes(node, neighbour)
                for edge in edge_list:
                    print('{0} {1} {2}' \
                            .format(node.odd_node_nr, neighbour.odd_node_nr,
                                edge.weight), \
                                        file=f)
