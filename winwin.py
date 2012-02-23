from edge import Edge
from reader import Reader
from writer import Writer
from mst import Minimum_Spanning_Tree
from matcher import Matcher
from euler import Euler

import os
import argparse

# create parser
parser = argparse.ArgumentParser(add_help=False)
parser.add_argument('-f', '--file',dest='file',help='File to read TSP from',
        action='store',required=True)
parser.add_argument('-s','--start', dest='s',help='Start node to calculate \
        hamilton path', action='store',required=True)
parser.add_argument('-t','--end', dest='t',help='End node of to calculate \
hamilton path', action='store',required=True)

args = parser.parse_args()

# begin calculation
reader = Reader()
writer = Writer()

# read graph data/in from file
graph_tsp = reader.euler_2d(args.file) # graph_zz: alg 11290 / opt 7798
graph_hpp = reader.euler_2d(args.file, args.s, args.t) # graph_zz: alg 7490 / opt 7490, s = 1, t = 39

print('Graph is created')

# calculate the minimum spanning tree
mst = Minimum_Spanning_Tree()
graph_tsp = mst.calculate(graph_tsp)
graph_hpp = mst.calculate(graph_hpp)

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

# do a minimum perfect matching on the MST + {s, t}
graph_hpp = matcher.calculate(graph_hpp)

print('Perfect Matching calculated')
euler = Euler()

# calculate euler tour/path
euler_nodes_tsp = euler.calculate(graph_tsp)
euler_nodes_hpp = euler.calculate(graph_hpp, False)

print('Euler Tour calculated')
nodes_tsp = euler.shorten_tour(euler_nodes_tsp)
nodes_hpp = euler.shorten_path(euler_nodes_hpp)

print('Euler Tour shortened')
writer.write_nodes(nodes_tsp, 'data/out/tour_winwin.tsp')
writer.write_nodes(nodes_hpp, 'data/out/tour_winwin.hpp')

# calculate TSP costs
cost_tsp = 0
for i in range(len(nodes_tsp)):
    if i > 0:
        #print(graph_tsp.lookup_distance(nodes_tsp[i-1], nodes_tsp[i])[0])
        cost_tsp += graph_tsp.lookup_distance(nodes_tsp[i-1], nodes_tsp[i])[0]

print('TSP: This tour costs {0}, we visited {1} nodes.'.format(cost_tsp, i))

# calculate HPP costs
cost_hpp = 0
for i in range(len(nodes_hpp)):
    if i > 0:
        #print(graph_hpp.lookup_distance(nodes_hpp[i-1], nodes_hpp[i])[0])
        cost_hpp += graph_hpp.lookup_distance(nodes_hpp[i-1], nodes_hpp[i])[0]

print('HPP: This tour costs {0}, we visited {1} nodes.'.format(cost_hpp, i+1))
