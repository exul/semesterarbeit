import os
import sys

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(os.path.realpath(__file__)), './lib')))

from winwin.edge import Edge
from winwin.reader import Reader
from winwin.writer import Writer
from winwin.mst import Minimum_Spanning_Tree
from winwin.matcher import Matcher
from winwin.euler import Euler
from winwin.generator import Generator

# set if we want to plot the problem instance
#do_plot = False
do_plot = True

# how many times we like to run the calculation
#run_counts = 1000
#run_counts = 100
run_counts = 1

# calculate exact solution?
calc_exact = True
#calc_exact = False

# do we generate the graph ourselfs?
generated_graph = False
#generated_graph = True

if do_plot:
    from plot import Plot # TODO: this import takes a lot of time

generator = Generator()
reader = Reader()
writer = Writer()

# store solutions for every calculation run
solutions_tsp = list()
solutions_hpp = list()

for i in range(0, run_counts):
    # read graph data/in from file
    #graph_tsp = reader.euclidean('data/in/eil101.tsp') # alg 705 / opt 629 = 112%
    #graph_hpp = reader.euclidean('data/in/eil101.tsp', 38, 64) # alg 698 / opt 613 = 113% (13.27%)
    #graph_tsp = reader.euclidean('data/in/eil51.tsp') # alg 493 / opt 426 115%
    #graph_hpp = reader.euclidean('data/in/eil51.tsp', 40, 36) # alg 463 / opt 403 = 114% (14.77%)
    #graph_tsp = reader.euclidean('data/in/berlin52.tsp') # alg 8422 / opt 7542
    #graph_hpp = reader.euclidean('data/in/berlin52.tsp', 29, 44) # alg 8161 / opt 6967
    #graph_tsp = reader.euclidean('data/in/dantzig42.tsp') # alg 8422 / opt 7542
    #graph_hpp = reader.euclidean('data/in/dantzig42.tsp', 14, 42) # alg 8161 / opt 6967
    #graph_tsp = reader.euclidean('data/in/hoogeveen.tsp') # 
    #graph_hpp = reader.euclidean('data/in/hoogeveen.tsp', 1, 8) # 

    graph_tsp = reader.euclidean('data/in/christophides.tsp') # 
    graph_hpp = reader.euclidean('data/in/christophides.tsp', 1, 39) # 

    #graph_tsp = reader.euclidean('data/in/bier127.tsp') # 
    #graph_hpp = reader.euclidean('data/in/bier127.tsp', 98, 107) # 

    #graph_tsp = reader.euclidean('data/in/my_tsp.tsp') # 
    #graph_hpp = reader.euclidean('data/in/my_tsp.tsp', 32, 4) # 


    if generated_graph:
        # generate graph
        #generator.random('data/in/my_tsp.tsp', 'my tsp', 'My own graph', 50, 2, \
                #1, 1000)

        #generator.belt('data/in/my_tsp.tsp', 'my tsp', 'My own graph (belt)', 50, 2, \
                #1, 100, 1, 1500)

        #generator.crowds2('data/in/my_tsp.tsp', 'my tsp', 'My own graph (crowds2)', \
                        #50, 2, 100, 100, 2000)

        # read generated graph
        graph = reader.euclidean('data/in/my_tsp.tsp') # 

        # TODO: write graphs to file, not needed for the algortihm
        writer.write_matrix(graph,'data/out/graph_matrix_tsp.tsp', False) #TSP
        writer.write_matrix(graph,'data/out/graph_matrix_hpp.tsp', True) #HPP
    else:
        writer.write_matrix(graph_tsp,'data/out/graph_matrix_tsp.tsp', False) #TSP
        writer.write_matrix(graph_hpp,'data/out/graph_matrix_hpp.tsp', True) #HPP

    print('Graph is created')

    # TODO: Calculate exact solution
    if calc_exact:
        os.system('{0} -o {1} {2} | grep "Optimal Solution: "'.format("concorde", \
            "data/out/solution_tsp.tsp", "data/out/graph_matrix_tsp.tsp"))

        os.system('{0} -o {1} {2} | grep "Optimal Solution: "'.format("concorde", \
            "data/out/solution_hpp.tsp", "data/out/graph_matrix_hpp.tsp"))

        # cleanup temp files
        os.system('rm *.mas *.pul *.sav *.sol *.res')

    if generated_graph:
        # get s and t from optimal solution
        f = open('data/out/solution_hpp.tsp')
        data = f.readlines()
        first_line = data[1]
        last_line = data[-1]
        s = first_line.split()[1]
        t = last_line.split()[-1]

        # read graph again, with correct s and t
        graph_tsp = reader.euclidean('data/in/my_tsp.tsp') # 
        graph_hpp = reader.euclidean('data/in/my_tsp.tsp', s, t) # 

    if do_plot:
        # TODO: only to create graphics, not needed for the algorithm
        plt = Plot('data/plot/solution.pdf', False)

    # calculate the minimum spanning tree
    mst = Minimum_Spanning_Tree()
    graph_tsp = mst.calculate(graph_tsp)
    graph_hpp = mst.calculate(graph_hpp)

    if do_plot:
        # TODO: only to create graphics, not needed for the algorithm
        plt.plot_graph(graph_tsp, '#000000', 'MST TSP')
        plt.plot_graph(graph_hpp, '#000000', 'MST HPP')

    print('MST calculated')

    # do a minimum perfect matching on the odd nodes of the graph
    # and add the new edges to the graph
    matcher = Matcher()

    # do a minimum perfect matching on the MST
    graph_tsp = matcher.calculate(graph_tsp)

    if do_plot:
        #TODO: only to create graphics, not needed for the algorithm
        plt.plot_graph(graph_tsp, '#ff0000', 'TSP with Perfect Matching')

    # add {s, t} to the MST
    node_s = graph_hpp.node_s
    node_t = graph_hpp.node_t
    weight = graph_hpp.lookup_distance(node_s, node_t)[0]

    if not graph_hpp.contains_edge(node_s, node_t):
        edge_st = Edge(node_s, node_t, weight)
        graph_hpp.add_edge(edge_st)

    if do_plot:
        # TODO: only to create graphics, not needed for the algorithm
        plt.plot_graph(graph_hpp, '#000000', 'MST with s and t')

    # do a minimum perfect matching on the MST + {s, t}
    graph_hpp = matcher.calculate(graph_hpp)

    print('Perfect Matching calculated')

    euler = Euler()

    # calculate euler tour
    euler_nodes_tsp = euler.calculate(graph_tsp)

    # TODO: calculate euler path => correct?
    euler_nodes_hpp = euler.calculate(graph_hpp, False)

    if do_plot:
        # TODO: only to create graphics, not needed for the algorithm
        plt.plot_nodes(euler_nodes_tsp, '#000000', 'Euler nodes TSP')
        #print(euler_nodes_hpp)
        plt.plot_nodes(euler_nodes_hpp, '#000000', 'Euler nodes HPP')

    print('Euler Tour calculated')

    nodes_tsp = euler.shorten_tour(euler_nodes_tsp)
    nodes_hpp = euler.shorten_path(euler_nodes_hpp)

    if do_plot:
        # TODO: only to create graphics, not needed for the algorithm
        plt.plot_nodes(nodes_tsp, '#000000', 'TSP Tour')
        plt.plot_nodes(nodes_hpp, '#000000', 'HPP Tour')

    print('Euler Tour shortened')

    writer.write_nodes(nodes_tsp, 'data/out/tour_winwin.tsp')
    writer.write_nodes(nodes_hpp, 'data/out/tour_winwin.hpp')

    # calculate TSP costs
    cost_tsp = 0
    for i in range(len(nodes_tsp)):
        if i > 0:
            #print(graph_tsp.lookup_distance(nodes_tsp[i-1], nodes_tsp[i])[0])
            cost_tsp += graph_tsp.lookup_distance(nodes_tsp[i-1], nodes_tsp[i])[0]

    # add tsp costs to the list of solutions
    solutions_tsp.append(cost_tsp)

    print('TSP: This tour costs {0}, we visited {1} nodes.'.format(cost_tsp, i))

    # calculate HPP costs
    cost_hpp = 0
    for i in range(len(nodes_hpp)):
        if i > 0:
            #print(graph_hpp.lookup_distance(nodes_hpp[i-1], nodes_hpp[i])[0])
            cost_hpp += graph_hpp.lookup_distance(nodes_hpp[i-1], nodes_hpp[i])[0]

    # add hamilton path costs to the list of solutions
    solutions_hpp.append(cost_hpp)

    print('HPP: This tour costs {0}, we visited {1} nodes.'.format(cost_hpp, i+1))

    if do_plot:
        # TODO: only to create graphics, optimal solution
        solution_nodes_tsp = reader.solution('data/out/solution_tsp.tsp', nodes_tsp, True)
        plt.plot_nodes(solution_nodes_tsp, '#000000', 'Optimal Solution TSP')

        solution_nodes_hpp = reader.solution('data/out/solution_hpp.tsp', nodes_tsp, False)
        plt.plot_nodes(solution_nodes_hpp, '#000000', 'Optimal Solution HPP')

        # TODO: only to create graphics, not needed for the algorithm
        plt.save_file()

print('Average Costs for TSP in {0} runs: {1}' \
        .format(len(solutions_tsp), sum(solutions_tsp)/len(solutions_tsp)))
print('Average Costs for HPP in {0} runs: {1}' \
        .format(len(solutions_hpp), sum(solutions_hpp)/len(solutions_tsp)))

print('Min value tsp is: {0}'.format(min(solutions_tsp)))
print('Max value tsp is: {0}'.format(max(solutions_tsp)))

print('Min value hpp is: {0}'.format(min(solutions_hpp)))
print('Max value hpp is: {0}'.format(max(solutions_hpp)))
