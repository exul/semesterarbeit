from reader import Reader
from writer import Writer
from mst import Minimum_Spanning_Tree
from matcher import Matcher
from euler_tour import Euler_Tour

import os

reader = Reader()
writer = Writer()

# read graph data/in from file
#graph = reader.euler_2d('data/in/eil101.tsp')
#graph = reader.euler_2d('data/in/eil51.tsp')
#graph = reader.euler_2d('data/in/a280.tsp')
#graph = reader.euler_2d('data/in/ch130.tsp')
#graph = reader.euler_2d('data/in/fl1400.tsp')
#graph = reader.euler_2d('data/in/kroA100.tsp')
#graph = reader.euler_2d('data/in/ulysses22.tsp')
#graph = reader.euler_2d('data/in/bier127.tsp')
#graph = reader.euler_2d('data/in/bayg29.tsp')
#graph = reader.euler_2d('data/in/float.tsp')
#graph = reader.euler_2d('data/in/int.tsp')
graph = reader.euler_2d('data/in/graph.tsp', 6, 5)

print('Graph is created')

# TODO: write graph as matrix, not needed for the algortihm
writer.write_matrix(graph, 'data/out/graph_matrix.tsp')

# calculate the minimum spanning tree
mst = Minimum_Spanning_Tree()
graph = mst.calculate(graph)

print('MST calculated')

# do a minimum perfect matching on the odd nodes of the graph
# and add the new edges to the graph
matcher = Matcher()

# do a minimum perfect matching on the MST
graph_tsp = matcher.calculate(graph)

# do a minimum perfect matching on the MST + {s, t}

print('Perfect Matching calculated')

euler_tour = Euler_Tour()
euler_nodes_tsp = euler_tour.calculate(graph_tsp)

print('Euler Tour calculated')

nodes_tsp = euler_tour.shorten(euler_nodes_tsp)

print('Euler Tour shortened')

writer.write_nodes(nodes_tsp, 'data/out/tour_winwin.tsp')

cost_tsp = 0
for i in range(len(nodes_tsp)):
    if i > 0:
        cost_tsp += graph_tsp.lookup_distance(nodes_tsp[i-1], nodes_tsp[i])[0]

print('This tour costs {0}, we visited {1} nodes.'.format(cost_tsp, i))
