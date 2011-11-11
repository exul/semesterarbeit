import random

from node import Node
from edge import Edge
from graph import Graph

class Euler_Tour:
    def __init__(self, graph):
        self.graph = graph

    def calculate(self):
        euler = list()
        self._euler_graph = Graph()

        # save start node, so we can check if we did a cycle
        # we just take the first node in the graph, it doesn't matter
        start_node = self.graph.nodes[0]
        # for the first walk our start_node is the current_node
        current_node = start_node
        # we want wo walk at least once
        condition = True

        # get size of the current graph
        graph_size = self.graph.size

        # TODO: list only for debugging
        euler_ori = list()

        while self._euler_graph.size < graph_size:
            # list to store nodes for each cycle
            euler_sub = list() 
            # list to store a copy of the original euler list, needed to merge euler
            # with euler_sub
            euler_tmp = list()
            # loop until we hit the start_node, but at least once
            while condition:
                # add the current node to the euler tour
                euler_sub.append(current_node)
                # take an arbitrary neighbour
                neighbours = self.graph.neighbour_nodes(current_node)
                next_node = random.choice(list(neighbours.copy().keys()))
                # get the edge between the current node an our new node
                # if there is more than one edge, just take the first one
                edge_list = self.graph.edge_by_nodes(current_node, next_node)
                current_edge = edge_list[0]
                # delete the edge from the graph, we don't want to take the the same edge twice
                self.graph.remove_edge(current_edge)

                # add nodes and edges to the graph that represents the euler cycle
                if not self._euler_graph.contains_node(current_node):
                    self._euler_graph.add_node(current_node)

                if not self._euler_graph.contains_node(next_node):
                    self._euler_graph.add_node(next_node)

                current_node.visits += 1
                self._euler_graph.add_edge(current_edge)

                # start agein with the next_node as current_node
                current_node = next_node
                # check if we hit the start_node
                condition = (current_node != start_node)

            # edge the last node
            euler_sub.append(current_node)
            # merge current cycle with the already computed one
            euler = self.merge_cycles(euler, euler_sub, current_node) 

            for node in euler:
                #TODO: Find better solution to get the next_node, best would be a list
                #with nodes that are candiates (nodes that are in the last cycle and
                #have at least 1 neighbour)
                if self.graph.contains_node(node):
                    neighbours = self.graph.neighbour_nodes(node)
                    if len(neighbours) > 0:
                        start_node = node
                        current_node = start_node
                        condition = True
                        break

        print('========== Debug ========')
        print('Real euler')
        for node in euler:
            print('Node {0} visited {1}'.format(node.label, node.visits))

        # return a list of nodes in the order of the euler tour
        return euler

    def merge_cycles(self, euler, euler_sub, current_node):
        '''
        Merge two eulerian cycles.

        @type:  euler:list
        @param: List that contains the eulerian path.
        @type:  euler_sub:list
        @param: List that should be merged into eulerian path.
        @type:  current_node: node
        @param: Node at which the two lists should be murged

        @rtype: list
        @return: A list containing all nodes.
        '''
        # copy content of euler list to euler_tmp
        euler_tmp = list()
        euler_tmp += euler
        # empty euler list
        euler = list()
        # only append list once
        found = False

        if len(euler_tmp) > 0:
            for node in euler_tmp:
                if node == current_node and found == False:
                    for node_sub in euler_sub:
                        euler.append(node_sub)
                    found = True
                else:
                    euler.append(node)
        else:
            euler += euler_sub

        return euler

    def shorten(self, graph_original, graph_eulerian, euler_nodes):
        first = True
        shorten = False
        # use i instead of index, because the same node can be in then list
        # more than once
        i = 0 

        print('=== Debug eulerian graph ===')
        for edge in graph_eulerian.edges:
            print('Edge from {0} to {1}'\
                    .format(edge.node_1.label, edge.node_2.label))
        print('=== End Debug eulerian graph ===')

        for node in euler_nodes:
            # get previous node
            if i == 0 and node.visits > 1:
                # the previous node of the first node is the second last node,
                # because the last node is the same as the first node
                previous_node = euler_nodes[len(euler_nodes)-2]
                shorten = True
            elif node.visits> 1:
                previous_node = euler_nodes[i-1]
                shorten = True

            if shorten:
                # get next node
                next_node = euler_nodes[i+1]

                # lookup the new edge in the original graph that contains all
                # connections
                new_edge = graph_original.edge_by_nodes(previous_node, \
                        next_node)[0]
                # lookup the previous and the next edge in the eulerian graph
                # that contains all edges that are in the eulerian tour
                previous_edge = graph_eulerian.edge_by_nodes(previous_node, \
                        node)[0]
                next_edge = graph_eulerian.edge_by_nodes(node, next_node)[0]

                # delete previous and next edge in the eulerian graph
                graph_eulerian.remove_edge(previous_edge)
                graph_eulerian.remove_edge(next_edge)

                # the current node is now visited even less
                node.visits -= 1

                # delete node from the list, because now we walk directly from
                # the previous node to the next node
                del euler_nodes[i]

                # add the new edge to the eulerian graph, it covers the
                # connection that previous_edge and next_edge connected befor
                graph_eulerian.add_edge(new_edge)


            # count and reset shorten
            i += 1
            shorten = False
        return euler_nodes

    @ property
    def euler_graph(self):
        return self._euler_graph
