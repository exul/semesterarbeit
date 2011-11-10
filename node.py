class Node:
    ''' Represents a node in a graph '''

    def __init__(self, x, y, label=''):
        self.x = float(x)
        self.y = float(y)
        self.label = label
        self.visits = 0
        self.odd_node_nr = -1

    def get_id(self):
        return id(self)

    def __cmp__(self, other):
        return id(self).__cmp__(id(other))

    def __hash__(self):
        return hash(id(self))

    def get_is_odd_node():
        if self._odd_node == -1:
            return False
        else:
            return True

    id = property(get_id)
