import random

from node import Node
from edge import Edge
from graph import Graph

class Euler_Tour:
    ''' Algorithms to calculate euler tour  '''

    def calculate(self, graph):
        '''
        Calculate the euler tour in a given graph

        @rtype: list
        @return: A list of nodes in order of the eulerian tour.
        '''

        euler = list()
        euler_graph = Graph()

        # save start node, so we can check if we did a cycle
        # we just take the first node in the graph, it doesn't matter
        start_node = graph.nodes[0]
        # for the first walk our start_node is the current_node
        current_node = start_node
        # we want wo walk at least once
        condition = True

        # get size of the current graph
        graph_size = graph.size

        while euler_graph.size < graph_size:
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
                neighbours = graph.neighbour_nodes(current_node)
                next_node = random.choice(list(neighbours.copy().keys()))
                # get the edge between the current node an our new node
                # if there is more than one edge, just take the first one
                edge_list = graph.edge_by_nodes(current_node, next_node)
                current_edge = edge_list[0]
                # delete the edge from the graph, we don't want to the the same edge twice
                graph.remove_edge(current_edge)

                # add nodes and edges to the graph that represents the euler cycle
                if not euler_graph.contains_node(current_node):
                    euler_graph.add_node(current_node)

                if not euler_graph.contains_node(next_node):
                    euler_graph.add_node(next_node)

                euler_graph.add_edge(current_edge)

                # start agein with the next_node as current_node
                current_node = next_node
                # check if we hit the start_node
                condition = (current_node != start_node)

            # edge to the last node
            euler_sub.append(current_node)
            # merge current cycle with the already computed one
            euler = self.merge_cycles(euler, euler_sub, current_node) 

            for node in euler:
                #TODO: Find better solution to get the next_node, best would be a list
                #with nodes that are candiates (nodes that are in the last cycle and
                #have at least 1 neighbour)
                if graph.contains_node(node):
                    neighbours = graph.neighbour_nodes(node)
                    if len(neighbours) > 0:
                        start_node = node
                        current_node = start_node
                        condition = True
                        break

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

    def shorten(self, nodes):
        ''' Shortens an eulerian tour, so that every node is visited only once.

        @type: nodes: list
        @param nodes: List of nodes in order of the eulerian tour.

        @rtype: list
        @return: List of nodes in order of the eulerian tour (but every node is
        visited only once).
        '''
        
        # use i instead of the list index, because the same node can be in the
        # list more than once
        i = 0

        for node in nodes:
            # delete all nodes that are listed more than once, except the first
            # and the last node
            if nodes.count(node) > 1 and i != 0 and i != len(nodes)-1:
                del(nodes[i])
        
            i += 1

        return nodes
