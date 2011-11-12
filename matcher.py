class Matcher:
    ''' Do a perfect matching '''

    def calculate(self, graph):
        '''
        Calculate the minimum perfect matching on the odd nodes

        @type: graph: graph
        @param: Graph that contains the odd nodes to calculate the perfect
        machting
        '''

        odd_nodes = dict()
        odd_node_nr = 0

        for node in graph.nodes:
            if len(graph.neighbour_nodes(node)) % 2 == 1:
                   odd_nodes[node] = odd_node_nr
                   odd_node_nr += 1
