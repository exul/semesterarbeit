import random

filename = 'data/in/my_tsp.tsp'
tsp_name = 'myTSP'
tsp_comment = 'My comment'
tsp_type = 'TSP'
tsp_dimension = 50
tsp_euc_dimension = 5
tsp_edge_weight_type = 'EUC_2D'
tsp_min_coord = 1
tsp_max_coord = 1000

f = open(filename,'w')

print('NAME: {0}'.format(tsp_name), file=f)
print('COMMENT: {0}'.format(tsp_comment), file=f)
print('TYP: {0}'.format(tsp_type), file=f)
print('DIMENSION: {0}'.format(tsp_dimension), file=f)
print('EDGE_WEIGHT_TYPE: {0}'.format(tsp_edge_weight_type), file=f)
print('NODE_COORD_SECTION', file=f)

for i in range(0,tsp_dimension):
    print('{0}'.format(i+1), end=" ", file=f)

    for j in range(0, tsp_euc_dimension):
        print('{0}'.format(random.randrange(tsp_min_coord,tsp_max_coord)), end=" ", file=f)
    print('',file=f)
