from reader import Reader
from writer import Writer
from mst import Minimum_Spanning_Tree
from matcher import Matcher
from euler_tour import Euler_Tour

import os

reader = Reader()
writer = Writer()

# read graph data from file
graph = reader.euler_2d('data/eil101.tsp')

# calculate the minimum spanning tree
mst = Minimum_Spanning_Tree()
graph = mst.calculate(graph)

# do a minimum perfect matching on the odd nodes of the graph
# and add the new edges to the graph
matcher = Matcher()
graph = matcher.calculate(graph)

euler_tour = Euler_Tour()
euler_nodes = euler_tour.calculate(graph)

tsp_nodes = euler_tour.shorten(euler_nodes)
writer.write_nodes(tsp_nodes, '/tmp/tour.tsp')

tsp_cost = 0
for i in range(len(tsp_nodes)):
    if i > 0:
        tsp_cost += graph.lookup_distance(tsp_nodes[i-1], tsp_nodes[i])[0]

print('This tour costs {0}, we visited {1} nodes.'.format(tsp_cost, i))
