class Node:
    ''' Represents a node in a graph '''

    def __init__(self, x, y, label=''):
        self.x = float(x)
        self.y = float(y)
        self.label = label
        self.visits = 0

    def get_id(self):
        return id(self)

    def __cmp__(self, other):
        return id(self).__cmp__(id(other))

    def __hash__(self):
        return hash(id(self))

    id = property(get_id)
