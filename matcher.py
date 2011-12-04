import os
from collections import OrderedDict
from edge import Edge

class Matcher:
    ''' Do a matching on edges in a graph '''

    def calculate(self, graph, temp_path='/tmp/', blossom_path='mpm/blossom5',
            add_s_t = False):
        '''
        Calculate the minimum perfect matching on the odd nodes of the given
        graph and add the new edges to the graph.

        @type   graph: graph
        @param  graph: Graph that contains the odd nodes to calculate the perfect
        machting

        @type   temp_path: string
        @param  temp_path: path to store the temp-file for calculating the perfect
        matching (with trailing slash, e.g. /tmp/)

        @type   blossom_path: string
        @param  blossom_path: path where the blossom executable is stored, it does the
        perfect matching

        @type   add_s_t: boolean
        @param  add_s_t: Indicate if node s and t should be added to the perfect
        matching

        @rtype: graph
        @return: the graph including the new edges calculated by perfect
        matching
        '''

        odd_nodes = dict()
        odd_node_nr = 0

        pm_to_solve = temp_path + 'graph.pm'
        pm_result = temp_path + 'matching.pm'

        # always use the same order to write the nodes into the file, otherwise
        # there will be different results
        nodes = sorted(graph.nodes, key=lambda node: node.nr)

        for node in nodes:
            if len(graph.neighbour_nodes(node)) % 2 == 1:
                   odd_nodes[odd_node_nr] = node
                   odd_node_nr += 1

        # add node s and t if the variable add_s_t is true
        if add_s_t:
            odd_nodes[odd_node_nr] = graph.node_s
            odd_node_nr += 1
            odd_nodes[odd_node_nr] = graph.node_t
            
        # sort dictionary by keys
        odd_nodes = OrderedDict(sorted(odd_nodes.items(), key=lambda t: t[0]))

        f = open(pm_to_solve, 'w')

        # writer number of nodes and number of edges
        node_count = len(odd_nodes.keys())
        edge_count = int((node_count * (node_count - 1))/2)

        # write all edges to the file
        print('{0} {1}'.format(node_count, edge_count), file=f)
        for node_1_nr, node_1 in odd_nodes.items(): 
            for node_2_nr, node_2 in odd_nodes.items(): 
                if node_1 != node_2:
                    distance = graph.lookup_distance(node_1, node_2)[0]
                    print('{0} {1} {2}'.format(node_1_nr, node_2_nr, distance), file=f)
                else:
                    break

        f.close()

        # caculate the perfect matching, use the external program blossom5
        os.system('{0} -e {1} -w {2} >> /dev/null'.format(blossom_path, pm_to_solve, \
            pm_result))

        # read matched nodes and add the edges to graph
        f = open(pm_result, 'r')

        # skip first line, it only contains information about nodes and edges
        next(f)

        # read each line and create an edge that is added to the graph
        for line in f:
            node_1_odd_node_nr,node_2_odd_node_nr = line.split()
            node_1 = odd_nodes[int(node_1_odd_node_nr)]
            node_2 = odd_nodes[int(node_2_odd_node_nr)]
            weight = graph.lookup_distance(node_1, node_2)[0]
            edge = Edge(node_1, node_2, weight)
            graph.add_edge(edge)

        return graph
