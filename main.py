import os

from reader import Reader
from writer import Writer
from mst import Minimum_Spanning_Tree
from euler_tour import Euler_Tour
from graph import Graph
from edge import Edge

reader = Reader()
writer = Writer()
#graph_original = reader.graph_euler_2d('data/graph.tsp')
#graph_original = reader.graph_euler_2d('data/eil51.tsp')
graph_original = reader.graph_euler_2d('data/eil101.tsp')
#Copy graph, because we need one, that doesn't change during the whole
# TODO: is there a better solution (delete edges only logically)
graph_copy = graph_original.copy

mst = Minimum_Spanning_Tree(graph_copy)
graph_mst = mst.calculate()

#TODO just for debugging
total_cost = 0
for edge in graph_original.edges:
    total_cost += edge.weight
print('Total cost for this Graph is: {0}'.format(total_cost))

cost = 0
for edge in graph_mst.edges:
    cost += edge.weight
print('Cost for this MST is: {0}'.format(cost))

#TODO: just for debugging
writer.write_blossom_iv(graph_mst,'/tmp/graph_mst')

graph_odd_nodes = Graph(False)
odd_nodes = graph_mst.odd_nodes

for node_1 in odd_nodes:
    graph_odd_nodes.add_node(node_1)
    for node_2 in odd_nodes:
        if node_1 != node_2:
            if(not graph_odd_nodes.contains_node(node_2)):
                graph_odd_nodes.add_node(node_2)

            edge_list = graph_original.edge_by_nodes(node_1, node_2)
            for edge in edge_list:
                temp_distance = edge.weight
                temp_edge = Edge(node_1, node_2, temp_distance)
                graph_odd_nodes.add_edge(temp_edge)
        else:
            break

writer.write_blossom_iv(graph_odd_nodes,'mpm/graph.tsp')

os.system('mpm/blossom5 -e mpm/graph.tsp -w mpm/mpm.tsp')

graph_eulerian = reader.edges_blossom_iv('mpm/mpm.tsp', graph_odd_nodes.nodes, \
        graph_original, graph_mst)

print('=== Debug FIRST eulerian graph in main ===')
edges = set()
for edge in graph_eulerian.edges:
    edges.add(edge)

for edge in edges:
    print('From {0} to {1} with weight {2}'.format(edge.node_1.label,
        edge.node_2.label, edge.weight))

euler_result = list()
euler_tour = Euler_Tour(graph_eulerian)
euler_nodes = euler_tour.calculate()
graph_eulerian = euler_tour.euler_graph

#TODO: The following is only for debuging
tsp_tour = euler_tour.shorten(graph_original, graph_eulerian, euler_nodes)
for node in tsp_tour:
    print('Walk to node {0}'.format(node.label))

graph_eulerian = euler_tour.euler_graph
edges = set()
for edge in graph_eulerian.edges:
    edges.add(edge)

tsp_cost = 0
for edge in edges:
    tsp_cost += edge.weight
print('Cost {0}'.format(tsp_cost))

print('Debug - export to draw picture')
f = open('result.txt', 'w')
for node in euler_nodes:
    print('{0} {1}'.format(node.x, node.y), file=f)
