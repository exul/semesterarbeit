from node import Node
from edge import Edge

class Graph:
    ''' Represents a graph '''

    def __init__(self, is_undirected=True):
        """
        Initialize a graph.

        @type:  is_undirected: boolean
        @param: is_undirected: Defines if the graph is undirected or not
        """
        self._distance_lookup = dict() # store distances between nodes
        self._graph_nodes = dict() # store the nodes
        self._is_undirected = is_undirected
        self._edge_count = 0
        self._odd_node_count = 0

    def add_node(self, node):
        """ 
        Add node to the graph.
        
        @type  node: node
        @param node: Node
        """
        if(not node in self._graph_nodes):
            self._distance_lookup[node] = dict() # add node to lookup
            self._graph_nodes[node] = dict() # add node to the neighbours
        else:
            #TODO: Define AdditionError
            raise AdditionError("This node is already in the graph")

    def add_edge(self, edge):
        """ 
        Add edge to the graph.
        
        @type   edge: edge
        @param  node1: Edge to add, both nodes of the edge have to be in the graph
        """
        node_1 = edge.node_1
        node_2 = edge.node_2 
        weight = edge.weight

        if(node_1 in self._graph_nodes and node_2 in self._graph_nodes):
            #TODO: Use a List of Edges, because we need to add more then one
            #Edge between two nodes
            if(self.is_undirected):
                if node_2 in self._graph_nodes[node_1]:
                    edge_list_distance_lookup = self._distance_lookup[node_1][node_2]
                    edge_list_distance_lookup.append(edge)

                    edge_list = self._graph_nodes[node_1][node_2]
                    edge_list.append(edge)
                else:
                    # TODO: this could be done in one line
                    edge_list_distance_lookup = list()
                    edge_list_distance_lookup.append(edge)
                    self._distance_lookup[node_1][node_2] = edge_list_distance_lookup

                    edge_list = list()
                    edge_list.append(edge)
                    self._graph_nodes[node_1][node_2] = edge_list

                if node_1 in self._graph_nodes[node_2]:
                    edge_list_distance_lookup = self._distance_lookup[node_2][node_1]
                    edge_list_distance_lookup.append(edge)

                    edge_list = self._graph_nodes[node_2][node_1]
                    edge_list.append(edge)
                else:
                    edge_list_distance_lookup = list()
                    edge_list_distance_lookup.append(edge)
                    self._distance_lookup[node_2][node_1] = edge_list_distance_lookup

                    edge_list = list()
                    edge_list.append(edge)
                    self._graph_nodes[node_2][node_1] = edge_list

                self._edge_count += 2
            else:
                if node_2 in self._graph_nodes[node_1]:
                    edge_list_distance_lookup = self._distance_lookup[node_1][node_2]
                    edge_list_distance_lookup.append(edge)

                    edge_list = self._graph_nodes[node_1][node_2]
                    edge_list.append(edge)
                else:
                    edge_list_distance_lookup = list()
                    edge_list_distance_lookup.append(edge)
                    self._distance_lookup[node_1][node_2] = edge_list_distance_lookup

                    edge_list = list()
                    edge_list.append(edge)
                    self._graph_nodes[node_1][node_2] = edge_list

                self._edge_count += 1
        else:
            #TODO: Define AdditionError
            raise AdditionError("One or both nodes not in the graph")
    
    def remove_edge(self, edge):
        """
        Remove an edge.

        @type   edge: edge
        @param  node1: Edge to remove
        """
        if self.is_undirected :
            edge_list = self._graph_nodes[edge.node_1][edge.node_2]
            edge_list.remove(edge)

            # if there are no more edges in the list, delete the neighbour
            if not self._graph_nodes[edge.node_1][edge.node_2]:
                del(self._graph_nodes[edge.node_1][edge.node_2])

            edge_list = self._graph_nodes[edge.node_2][edge.node_1]
            edge_list.remove(edge)

            # if there are no more edges in the list, delete the neighbour
            if not self._graph_nodes[edge.node_2][edge.node_1]:
                del(self._graph_nodes[edge.node_2][edge.node_1])
        else:
            edge_list = self._graph_nodes[edge.node_1][edge.node_2]
            edge_list.remove(edge)

            # if there are no more edges in the list, delete the neighbour
            if not self._graph_nodes[edge.node_1][edge.node_2]:
                del(self._graph_nodes[edge.node_1][edge.node_2])


        del(edge)
        self._edge_count -= 1

    def neighbour_nodes(self, node):
        """
        Return all nodes that are connected to the given node.

        @type: node:node
        @param: Node

        @rtype: dict
        @return: A dict of all nodes that are connected to the node.
        """
        return self._graph_nodes[node]

    def neighbour_edges(self, node):
        """
        Return all edges that are connected to the given node.

        @type: node:node
        @param: Node

        @rtype: list
        @return: A list of all edges that are connected to the node.
        """
        edge_lists = list(self._graph_nodes[node].copy().values())
        edges = list()
        for edge_list in edge_lists:
            for edge in edge_list:
                edges.append(edge)

        return edges
       
    def contains_node(self, node):
        """ 
        Checks, if a given node is in the graph or not.
        
        @rtype:  boolean
        @return: true, if the node is in the graph, otherwise false
        """
        return node in  self._graph_nodes

    def edge_by_nodes(self, node_1, node_2):
        '''
        Return a list of edges between two nodes

        @type: node_1:node
        @param: Node on one end of the edge
        @type: node_2:node
        @param: Node on the other end of the edge

        @rtype: list
        @return: List of edges between the given nodes
        '''

        return self._graph_nodes[node_1][node_2]

    @property
    def odd_nodes(self):
        '''
        Returns a list of all odd nodes in the graph.

        @rtype: list
        @return: List of all odd nodes in the graph.
        '''
        odd_nodes = list() # list to store odd nodes

        for node in self._graph_nodes.keys():
            if len(self._graph_nodes[node]) % 2 == 1:
                # set an odd_node_nr for every odd node, it is needed to
                # calculate the perfect matching
                node.odd_node_nr = self._odd_node_count
                self._odd_node_count += 1
                odd_nodes.append(node)

        return odd_nodes

    @property
    def nodes(self):
        """ 
        Return all nodes in the graph.
        
        @rtype:  list
        @return: List of all nodes in the graph.
        """
        return list(self._graph_nodes.copy().keys())

    @property
    def edges(self):
        """ 
        Return all edges in the graph.
        
        @rtype:  list
        @return: List of all edges in the graph.
        """
        graph_edges = list() # list to store edges

        #TODO: find a better way to do that, three for loops are ugly
        for node in self._graph_nodes.keys():
            edge_lists = list(self._graph_nodes[node].copy().values())
            edges = list()
            for edge_list in edge_lists:
                for edge in edge_list:
                    graph_edges.append(edge)

        return graph_edges

    @property
    def lookup_distance(node_1, node_2):
        '''
        Return all destances between two nodes.

        @rtype: list
        @return: List of distances beteeen two nodes.
        '''
        return self._distance_lookup[node_1][node_2]

    #TODO: rename to node_count?
    @property
    def size(self):
        """ 
        Return the size of the graph (number of nodes).
        
        @rtype:  int
        @return: Number of nodes
        """
        return len(self._graph_nodes)

    @property
    def is_undirected(self):
        """ 
        Returns if a graph is undirected (True) or not (False).
        
        @rtype: boolean
        @return: True or False
        """
        return self._is_undirected

    @ property
    def edge_count(self):
        '''
        Return the number of edges in the graph.

        @rtype: int
        @return: number of edges
        return self._edge_count
        '''
        return self._edge_count
