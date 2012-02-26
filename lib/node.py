class Node:
    ''' Represents a node in a graph '''

    def __init__(self, nr, coordinates, label=''):
        self.nr = int(nr)
        self.coordinates = coordinates
        self.label = label

    def get_id(self):
        return id(self)

    def get_x(self):
        return self.coordinates[0]

    def get_y(self):
        return self.coordinates[1]

    def get_z(self):
        return self.coordinates[2]

    def __cmp__(self, other):
        return id(self).__cmp__(id(other))

    def __hash__(self):
        return hash(id(self))

    id = property(get_id)
    x = property(get_x)
    y = property(get_y)
    z = property(get_z)
