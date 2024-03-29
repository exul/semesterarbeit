from winwin.node import Node
from winwin.edge import Edge

class Graph:
    ''' Represents an undirected graph '''

    def __init__(self, distance_lookup=dict(), node_s = None, node_t = None):
        """
        Initialize a graph.
        """
        self._distance_lookup = distance_lookup # store distances between nodes
        self._graph_nodes = dict() # store the nodes
        self._edge_count = 0
        self.node_s = node_s # represent start node in a hamiltonian path
        self.node_t = node_t # represent end node in a hamiltonian path

    def add_node(self, node):
        """ 
        Add node to the graph.
        
        @type  node: node
        @param node: Node
        """
        if not node in self._graph_nodes:
            self._graph_nodes[node] = dict() # add node to the neighbours
        else:
            raise NodeAdditionError(node.nr)

        if not node in self._distance_lookup:
            self._distance_lookup[node] = dict() # add node to lookup

    def add_edge(self, edge):
        """ 
        Add edge to the graph.
        
        @type   edge: edge
        @param  edge: Edge to add, both nodes of the edge have to be in the graph
        """
        node_1 = edge.node_1
        node_2 = edge.node_2 
        weight = edge.weight

        # add edge to the graph
        if node_1 in self._graph_nodes and node_2 in self._graph_nodes:
            # add edge in one direction
            if node_2 in self._graph_nodes[node_1]:
                edge_list = self._graph_nodes[node_1][node_2]
                edge_list.append(edge)
            else:
                edge_list = list()
                edge_list.append(edge)
                self._graph_nodes[node_1][node_2] = edge_list

            # add edge in other direction
            if node_1 in self._graph_nodes[node_2]:
                edge_list = self._graph_nodes[node_2][node_1]
                edge_list.append(edge)
            else:
                edge_list = list()
                edge_list.append(edge)
                self._graph_nodes[node_2][node_1] = edge_list

            self._edge_count += 2
        else:
            raise EdgeAdditionError("One or both nodes not in the graph")
    
        # add weight to lookup dictionary, if it isn't already there
        # add weight in one direction
        if node_2 in self._distance_lookup[node_1]:
            if not edge.weight in self._distance_lookup[node_1][node_2]:
                edge_list_distance_lookup = \
                    self._distance_lookup[node_1][node_2]
                edge_list_distance_lookup.append(edge.weight)
        else:
            edge_list_distance_lookup = list()
            edge_list_distance_lookup.append(edge.weight)
            self._distance_lookup[node_1][node_2] = edge_list_distance_lookup

        # add weight in other direction
        if node_1 in self._distance_lookup[node_2]:
            if not edge.weight in self._distance_lookup[node_2][node_1]:
                edge_list_distance_lookup = \
                    self._distance_lookup[node_2][node_1]
                edge_list_distance_lookup.append(edge.weight)
        else:
            edge_list_distance_lookup = list()
            edge_list_distance_lookup.append(edge.weight)
            self._distance_lookup[node_2][node_1] = edge_list_distance_lookup


    def remove_edge(self, edge):
        """
        Remove an edge.

        @type   edge: edge
        @param  edge: Edge to remove
        """
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

        del(edge)
        self._edge_count -= 1

    def neighbour_nodes(self, node):
        """
        Return all nodes that are connected to the given node.

        @type   node: node
        @param  node: Node

        @rtype: dict
        @return: A dict of all nodes that are connected to the node.
        """
        return self._graph_nodes[node]

    def neighbour_edges(self, node):
        """
        Return all edges that are connected to the given node.

        @type   node: node
        @param  node: Node

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

        @type   node: node
        @param  node: Node
        
        @rtype:  boolean
        @return: true, if the node is in the graph, otherwise false
        """
        return node in  self._graph_nodes

    def contains_edge(self, node_1, node_2):
        '''
        Checks, if a given edge (represented by node_1 and node_2 is 
        in the graph or not.
        We use nodes, becaues we may node hav the edge itself, if we have it,
        we can just take it's to nodes.

        @type   node_1: node
        @param  node_1: Node on one side of the edge

        @type   node_2: node
        @param  node_2: Node on the other side of the edge

        @rtype: boolean
        @return: true, if the edge is in the graph, otherwise false
        '''

        return node_2 in self._graph_nodes[node_1]

    def edge_by_nodes(self, node_1, node_2):
        '''
        Return a list of edges between two nodes

        @type   node_1: node
        @param  node_1: Node on one end of the edge
        @type   node_2: node
        @param  node_2: Node on the other end of the edge

        @rtype: list
        @return: List of edges between the given nodes
        '''

        return self._graph_nodes[node_1][node_2]

    def lookup_distance(self, node_1, node_2):
        '''
        Return all destances between two nodes.

        @rtype: list
        @return: List of distances beteeen two nodes.
        '''
        if node_1 in self._distance_lookup:
            if node_2 in self._distance_lookup[node_1]:
                return self._distance_lookup[node_1][node_2]
            else:
                raise NodeNotFoundError()
        else:
            raise NodeNotFoundError()

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
    def size(self):
        """ 
        Return the size of the graph (number of nodes).
        
        @rtype:  int
        @return: Number of nodes
        """
        return len(self._graph_nodes)

    @ property
    def edge_count(self):
        '''
        Return the number of edges in the graph.

        @rtype: int
        @return: number of edges
        return self._edge_count
        '''
        return self._edge_count

    @ property
    def distance_lookup(self):
        '''
        Return the distance lookup directory.

        @rtype: dictionary
        @return: Dictionary that contains all distances of the graph.
        '''
        return self._distance_lookup

class NodeNotFoundError(Exception):
    ''' Exception if a node can't be found. '''
    def __init__(self):
        Exception.__init__(self)

        print('Could not find the given node in this graph')

class NodeAdditionError(Exception):
    ''' Execption if a node can't be added '''
    def __init__(self, node_nr):
        Exception.__init__(self)

        print('Node Nr. {0} is already in the graph'.format(node_nr))

class EdgeAdditionError(Exception):
    ''' Exception if a node can't be added '''
    def __init__(self):
        Exception.__init__(self)
        print('Could not add Edge, one or both nodes are not in the graph')
