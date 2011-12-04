from reader import Reader
from writer import Writer
from mst import Minimum_Spanning_Tree
from matcher import Matcher
from euler_tour import Euler_Tour

import os

reader = Reader()
writer = Writer()

# read graph data from file
#graph = reader.euler_2d('data/eil101.tsp')
#graph = reader.euler_2d('data/eil51.tsp')
#graph = reader.euler_2d('data/a280.tsp')
#graph = reader.euler_2d('data/ch130.tsp')
#graph = reader.euler_2d('data/fl1400.tsp')
#graph = reader.euler_2d('data/kroA100.tsp')
#graph = reader.euler_2d('data/ulysses22.tsp')
#graph = reader.euler_2d('data/bier127.tsp')
#graph = reader.euler_2d('data/bayg29.tsp')
#graph = reader.euler_2d('data/float.tsp')
#graph = reader.euler_2d('data/int.tsp')
graph = reader.euler_2d('data/graph.tsp')

print('Graph is created')

# TODO: write graph as matrix, not needed for the algortihm
writer.write_matrix(graph, '/tmp/matrix_graph.tsp')

# calculate the minimum spanning tree
mst = Minimum_Spanning_Tree()
graph = mst.calculate(graph)

print('MST calculated')

# do a minimum perfect matching on the odd nodes of the graph
# and add the new edges to the graph
matcher = Matcher()
graph = matcher.calculate(graph)

print('Perfect Matching calculated')

euler_tour = Euler_Tour()
euler_nodes = euler_tour.calculate(graph)

print('Euler Tour calculated')

tsp_nodes = euler_tour.shorten(euler_nodes)

print('Euler Tour shortened')

writer.write_nodes(tsp_nodes, '/tmp/tour.tsp')

tsp_cost = 0
for i in range(len(tsp_nodes)):
    if i > 0:
        tsp_cost += graph.lookup_distance(tsp_nodes[i-1], tsp_nodes[i])[0]

print('This tour costs {0}, we visited {1} nodes.'.format(tsp_cost, i))
