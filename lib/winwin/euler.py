import random

from winwin.node import Node
from winwin.edge import Edge
from winwin.graph import Graph

class Euler:
    ''' Algorithms to calculate euler tour/path  '''

    def calculate(self, graph, tour=True):
        '''
        Calculate the euler tour in a given graph

        @type   graph: graph
        @param  graph: Graph to calculate eulerian tour/path.

        @type   tour: boolean
        @param  tour: If True, an eulerian tour is calculated, if false an
        eulerian path is calculated.

        @rtype: list
        @return: A list of nodes in order of the eulerian tour/path.
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

        if tour == False:
            euler = self.euler_path(euler, graph.node_s, graph.node_t)

        # return a list of nodes in the order of the euler tour
        return euler

    def merge_cycles(self, euler, euler_sub, current_node):
        '''
        Merge two eulerian cycles.

        @type   euler: list
        @param  euler: List that contains the eulerian path.
        @type   euler_sub: list
        @param  euler_sub: List that should be merged into eulerian path.
        @type   current_node: node
        @param  current_node: Node at which the two lists should be murged

        @rtype: list
        @return: A list containing all nodes.
        '''

        # if euler list is empty, merging euler_sub into euler = euler_sub
        if len(euler) == 0:
            return euler_sub

        # copy content of euler list to euler_tmp
        euler_tmp = list()
        euler_tmp += euler
        # empty euler list
        euler = list()
        # only append list once
        found = False

        for node in euler_tmp:
            if node == current_node and found == False:
                for node_sub in euler_sub:
                    euler.append(node_sub)
                found = True
            else:
                euler.append(node)

        return euler

    def shorten_tour(self, nodes):
        ''' Shortens an eulerian tour, so that every node is visited only once.

        @type   nodes: list
        @param  nodes: List of nodes in order of the eulerian tour.

        @rtype: list
        @return: List of nodes in order of the eulerian tour (but every node is
        visited only once).
        '''
        nodes_shortened = []
        for node in nodes:
            if node not in nodes_shortened:
                nodes_shortened.append(node)

        # add the first element at the end, because we want to do a tour
        nodes_shortened.append(nodes_shortened[0])

        return nodes_shortened

    def shorten_path(self,nodes):
        ''' Shortens an eulerian path, so that every node is visited only once.

        @type   nodes: list
        @param  nodes: List of nodes in order of the eulerian tour.

        @rtype: list
        @return: List of nodes in order of the eulerian tour (but every node is
        visited only once).
        '''

        nodes_shortened = []
        node_t = nodes[-1]

        for node in nodes:
            if node not in nodes_shortened and node != node_t:
                nodes_shortened.append(node)

        nodes_shortened.append(node_t)

        return nodes_shortened


    # TODO: There should be a nicer solution to create an euler path out of an
    # euler tour
    def euler_path(self, euler, node_s, node_t):
        del euler[-1]
        second_to_last_idx = len(euler)-1

        # if the lists starts with s and ends with t we already have the
        # correct list
        if euler[0] == node_s and euler[len(euler)-1] == node_t:
               return euler
        # if the lists starts with t and ends with s we only have to sort the
        # list the other way round and have the correct list
        elif euler[len(euler)-1] == node_s and euler[0] == node_t:
            euler.reverse()
            return euler


        # iterate over the list, from the first to the second to last element
        for idx, node in enumerate(euler[:second_to_last_idx]):
            next_idx = idx+1
            # find s and t together (this is our start and end point)
            if euler[next_idx] == node_s and euler[idx] == node_t:
                euler = euler[next_idx:] + euler[:next_idx]
                return euler

            if euler[next_idx] == node_t and euler[idx] == node_s:
                euler = euler[next_idx:] + euler[:next_idx]
                euler.reverse()
                return euler
