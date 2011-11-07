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
        self.graph_nodes = dict() # dictionary to store the nodes
        self._is_undirected = is_undirected

    def add_node(self, node):
        """ 
        Add node to the graph.
        
        @type  node: node
        @param node: Node
        """
        if(not node in self.graph_nodes):
            self.graph_nodes[node] = {} # dictionary to store the nodes neighbours
        else:
            #TODO: Define AdditionError
            raise AdditionError("This node is already in the graph")

    def add_edge(self, edge):
        """ 
        Add edge to the graph.
        
        @type   edge: edge
        @param  node1: Edge to add, both nodes of the edge have to be in the graph
        """
        node1 = edge.node_1
        node2 = edge.node_2 
        weight = edge.weight

        if(node1 in self.graph_nodes and node2 in self.graph_nodes):
            if(self.is_undirected):
                self.graph_nodes[node1][node2] = edge
                self.graph_nodes[node2][node1] = edge
            else:
                self.graph_nodes[node1][node2] = edge
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
            del(self.graph_nodes[edge.node_1][edge.node_2])
            del(self.graph_nodes[edge.node_2][edge.node_1])
        else:
            del(self.graph_nodes[edge.node_1][edge.node_2])

        del(edge)

    def neighbour_nodes(self, node):
        """
        Return all nodes that are connected to the given node.

        @type: node:node
        @param: Node

        @rtype: dict
        @return: A dict of all nodes that are connected to the node.
        """
        return self.graph_nodes[node]

    def neighbour_edges(self, node):
        """
        Return all edges that are connected to the given node.

        @type: node:node
        @param: Node

        @rtype: list
        @return: A list of all edges that are connected to the node.
        """
        return list(self.graph_nodes[node].copy().values())

    def contains_node(self, node):
        """ 
        Checks, if a given node is in the graph or not.
        
        @rtype:  boolean
        @return: true, if the node is in the graph, otherwise false
        """
        return node in  self.graph_nodes

    def edge_by_nodes(self, node_1, node_2):
        '''
        Return the between two nodes

        @type: node_1:node
        @param: Node on one end of the edge
        @type: node_2:node
        @param: Node on the other end of the edge

        @rtype: edge
        @return: Edge between the given nodes
        '''

        return self.graph_nodes[node_1][node_2]

    @property
    def nodes(self):
        """ 
        Return all nodes in the graph.
        
        @rtype:  list
        @return: List of all nodes in the graph.
        """
        return list(self.graph_nodes.copy().keys())

    @property
    def edges(self):
        """ 
        Return all edges in the graph.
        
        @rtype:  list
        @return: List of all edges in the graph.
        """
        self.graph_edges = list() # list to store edges

        for node in self.graph_nodes.keys():
            self.graph_edges = self.graph_edges + list(self.graph_nodes[node].copy().values())

        return self.graph_edges

    @property
    def size(self):
        """ 
        Return the size of the graph (number of nodes).
        
        @rtype:  int
        @return: Number of nodes
        """
        return len(self.graph_nodes)

    @property
    def is_undirected(self):
        """ 
        Returns if a graph is undirected (True) or not (False).
        
        @rtype: boolean
        @return: True or False
        """
        return self._is_undirected
