from edge import Edge
from reader import Reader
from writer import Writer
from mst import Minimum_Spanning_Tree
from matcher import Matcher
from euler import Euler
from plot import Plot # TODO: this import takes a lot of time

import os

reader = Reader()
writer = Writer()

# read graph data/in from file
#graph = reader.euler_2d('data/in/eil101.tsp')
#graph_tsp = reader.euler_2d('data/in/eil51.tsp')
#graph_hpp = reader.euler_2d('data/in/eil51.tsp', 39, 41)
#graph = reader.euler_2d('data/in/a280.tsp')
#graph = reader.euler_2d('data/in/ch130.tsp')
#graph = reader.euler_2d('data/in/fl1400.tsp')
#graph = reader.euler_2d('data/in/kroA100.tsp')
#graph = reader.euler_2d('data/in/ulysses22.tsp')
#graph = reader.euler_2d('data/in/bier127.tsp')
#graph = reader.euler_2d('data/in/bayg29.tsp')
#graph = reader.euler_2d('data/in/float.tsp')
#graph = reader.euler_2d('data/in/int.tsp')
#graph_tsp = reader.euler_2d('data/in/graph.tsp')
#graph_hpp = reader.euler_2d('data/in/graph.tsp', 5, 6)
graph_tsp = reader.euler_2d('data/in/graph_zz.tsp')
graph_hpp = reader.euler_2d('data/in/graph_zz.tsp', 1, 9)

print('Graph is created')

# TODO: write graph as matrix, not needed for the algortihm
writer.write_matrix(graph_tsp, 'data/out/graph_matrix.tsp')

# TODO: only to create graphics, not needed for the algorithm
plt = Plot()

# calculate the minimum spanning tree
mst = Minimum_Spanning_Tree()
graph_tsp = mst.calculate(graph_tsp)
graph_hpp = mst.calculate(graph_hpp)

# TODO: only to create graphics, not needed for the algorithm
plt.plot_graph(graph_tsp, 'MST TSP')
plt.plot_graph(graph_hpp, 'MST HPP')

print('MST calculated')

# do a minimum perfect matching on the odd nodes of the graph
# and add the new edges to the graph
matcher = Matcher()

# do a minimum perfect matching on the MST
graph_tsp = matcher.calculate(graph_tsp)

# add {s, t} to the MST
node_s = graph_hpp.node_s
node_t = graph_hpp.node_t
weight = graph_hpp.lookup_distance(node_s, node_t)[0]

if not graph_hpp.contains_edge(node_s, node_t):
    edge_st = Edge(node_s, node_t, weight)
    graph_hpp.add_edge(edge_st)

# TODO: only to create graphics, not needed for the algorithm
plt.plot_graph(graph_hpp, 'MST with s and t')

# do a minimum perfect matching on the MST + {s, t}
graph_hpp = matcher.calculate(graph_hpp)

print('Perfect Matching calculated')

euler = Euler()

# calculate euler tour
euler_nodes_tsp = euler.calculate(graph_tsp)

# TODO: calculate euler path => correct?
euler_nodes_hpp = euler.calculate(graph_hpp, False)

# TODO: only to create graphics, not needed for the algorithm
plt.plot_nodes(euler_nodes_tsp, 'Euler nodes TSP')
plt.plot_nodes(euler_nodes_hpp, 'Euler nodes HPP')

print('Euler Tour calculated')

nodes_tsp = euler.shorten_tour(euler_nodes_tsp)
nodes_hpp = euler.shorten_path(euler_nodes_hpp)

# TODO: only to create graphics, not needed for the algorithm
plt.plot_nodes(nodes_tsp, 'TSP Tour')
plt.plot_nodes(nodes_hpp, 'HPP Tour')

print('Euler Tour shortened')

writer.write_nodes(nodes_tsp, 'data/out/tour_winwin.tsp')
writer.write_nodes(nodes_hpp, 'data/out/tour_winwin.hpp')

# calculate TSP costs
cost_tsp = 0
for i in range(len(nodes_tsp)):
    if i > 0:
        cost_tsp += graph_tsp.lookup_distance(nodes_tsp[i-1], nodes_tsp[i])[0]

print('TSP: This tour costs {0}, je visited {1} nodes.'.format(cost_tsp, i))

# calculate HPP costs
cost_hpp = 0
for i in range(len(nodes_hpp)):
    if i > 0:
        cost_hpp += graph_hpp.lookup_distance(nodes_hpp[i-1], nodes_hpp[i])[0]

print('HPP: This tour costs {0}, je visited {1} nodes.'.format(cost_hpp, i+1))

# TODO: only to create graphics, not needed for the algorithm
plt.save_file()
