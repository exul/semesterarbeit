import random

from node import Node
from edge import Edge
from graph import Graph
from euler_to_hamilton import Euler_to_Hamilton

def merge_cycles(euler, euler_sub):
    '''
    Merge two eulerian cycles.

    @type:  euler:list
    @param: List that contains the eulerian path.
    @type:  euler_sub:list
    @param: List that should be merged into eulerian path.

    @rtype: list
    @return: A list containing all nodes.
    '''
    # copy content of euler list to euler_tmp
    euler_tmp = list()
    euler_tmp += euler
    # empty euler list
    euler = list()
    # only append list once
    found = False

    if len(euler_tmp) > 0:
        for node in euler_tmp:
            if node == current_node and found == False:
                for node_sub in euler_sub:
                    euler.append(node_sub)
                found = True
            else:
                euler.append(node)
    else:
        euler += euler_sub

    return euler

my_node1 = Node(1,1)
my_node2 = Node(1,2)
my_node3 = Node(1,3)
my_node4 = Node(1,4)
my_node5 = Node(1,5)
my_node6 = Node(1,6)
my_node7 = Node(1,7)
my_node8 = Node(1,8)
my_node9 = Node(1,9)

my_node99 = Node(1,99)

my_graph = Graph()

my_graph.add_node(my_node1)
my_graph.add_node(my_node2)
my_graph.add_node(my_node3)
my_graph.add_node(my_node4)
my_graph.add_node(my_node5)
my_graph.add_node(my_node6)
my_graph.add_node(my_node7)
my_graph.add_node(my_node8)
my_graph.add_node(my_node9)

my_edge1 = Edge(my_node1, my_node2, 7)
my_edge2 = Edge(my_node1, my_node3, 5)
my_edge3 = Edge(my_node1, my_node7, 5)
my_edge4 = Edge(my_node1, my_node8, 5)
my_edge5 = Edge(my_node2, my_node3, 8)
my_edge6 = Edge(my_node3, my_node4, 5)
my_edge7 = Edge(my_node3, my_node7, 5)
my_edge8 = Edge(my_node4, my_node5, 15) 
my_edge9 = Edge(my_node4, my_node7, 15) 
my_edge10 = Edge(my_node4, my_node9, 15) 
my_edge11 = Edge(my_node5, my_node9, 8)
my_edge12 = Edge(my_node6, my_node7, 9)
my_edge13 = Edge(my_node6, my_node9, 11) 
my_edge14 = Edge(my_node7, my_node8, 11) 
my_edge15 = Edge(my_node7, my_node9, 11) 

my_graph.add_edge(my_edge1)
my_graph.add_edge(my_edge2)
my_graph.add_edge(my_edge3)
my_graph.add_edge(my_edge4)
my_graph.add_edge(my_edge5)
my_graph.add_edge(my_edge6)
my_graph.add_edge(my_edge7)
my_graph.add_edge(my_edge8)
my_graph.add_edge(my_edge9)
my_graph.add_edge(my_edge10)
my_graph.add_edge(my_edge11)
my_graph.add_edge(my_edge12)
my_graph.add_edge(my_edge13)
my_graph.add_edge(my_edge14)
my_graph.add_edge(my_edge15)

euler = list()
euler_graph = Graph()

# save start node, so we can check if we did a cycle
start_node = my_node1
# for the first walk our start_node is the current_node
current_node = start_node
# we want wo walk at least once
condition = True

# get size of the current graph
graph_size = my_graph.size

# TODO: list only for debugging
euler_ori = list()

while euler_graph.size < graph_size:
    # list to store nodes for each cycle
    euler_sub = list() 
    # list to store a copy of the original euler list, needed to merge euler
    # with euler_sub
    euler_tmp = list()
    # loop until we hit the start_node, but at least once
    while condition:
        # add the current node to the euler tour
        euler_sub.append(current_node)
        # take an arbitrary neighbour
        neighbours = my_graph.neighbour_nodes(current_node)
        next_node = random.choice(list(neighbours.copy().keys()))
        # get the edge between the current node an our new node
        # if there is more than one edge, just take the first one
        edge_list = my_graph.edge_by_nodes(current_node, next_node)
        current_edge = edge_list[0]
        # delete the edge from the graph, we don't want to the the same edge twice
        my_graph.remove_edge(current_edge)

        # add nodes and edges to the graph that represents the euler cycle
        if not euler_graph.contains_node(current_node):
            euler_graph.add_node(current_node)

        if not euler_graph.contains_node(next_node):
            euler_graph.add_node(next_node)

        current_node.visits += 1
        euler_graph.add_edge(current_edge)

        # start agein with the next_node as current_node
        current_node = next_node
        # check if we hit the start_node
        condition = (current_node != start_node)

    # edge the last node
    euler_sub.append(current_node)
    # merge current cycle with the already computed one
    euler = merge_cycles(euler, euler_sub) 

    for node in euler:
        #TODO: Find better solution to get the next_node, best would be a list
        #with nodes that are candiates (nodes that are in the last cycle and
        #have at least 1 neighbour)
        if my_graph.contains_node(node):
            neighbours = my_graph.neighbour_nodes(node)
            if len(neighbours) > 0:
                start_node = node
                current_node = start_node
                condition = True
                break

# shorten eulerian cycle to hamilton cycle
euler_to_hamilton = Euler_to_Hamilton()
euler_to_hamilton.shorten(euler_graph)

print('========== Debug ========')
print('Real euler')
for node in euler:
    print('Node {0} visited {1}'.format(node.y, node.visits))
