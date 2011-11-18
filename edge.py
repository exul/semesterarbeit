class Edge:
    ''' Represents an edge in a graph '''
    def __init__(self, node_1, node_2, weight):
        """
        Create Edge

        @type  node1: node
        @param node1: Node on one end of the edge

        @type  node2: node
        @param node2: Node on the other end of the edge

        @type   weight: number
        @param  weight: Edge weight
        """ 
        self.node_1 = node_1
        self.node_2 = node_2
        self.weight = float(weight)

    def get_id(self):
        return id(self)

    def __eq__(self, other):
        return self.id == other.id

    def __lt__(self, other):
        # if the weights are the same, just compare the ids
        if self.weight == other.weight:
            return self.id < other.id
        else:
            return self.weight < other.weight

    def __hash__(self):
        return hash(id(self))

    id = property(get_id)
