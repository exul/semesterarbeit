import random

class Generator:
    ''' Generates a TSP instance '''

    def random(self, filename, name, comment, cities, dimension, min_coord, max_coord):

        tsp_type = 'TSP'
        tsp_edge_weight_type = 'EUC_' + str(dimension) + 'D'

        f = open(filename, 'w')

        # write header
        print('NAME: {0}'.format(name), file=f)
        print('COMMENT: {0}'.format(comment), file=f)
        print('TYP: {0}'.format(tsp_type), file=f)
        print('DIMENSION: {0}'.format(cities), file=f)
        print('EDGE_WEIGHT_TYPE: {0}'.format(tsp_edge_weight_type), file=f)
        print('NODE_COORD_SECTION', file=f)

        for i in range(0,cities):
            print('{0}'.format(i+1), end=" ", file=f)

            for j in range(0, dimension):
               print('{0}'.format(random.randrange(min_coord,max_coord)), end=" ", file=f)

            print('',file=f)

        f.close()

    def belt(self, filename, name, comment, cities, dimension, \
            min_coord_height, max_coord_height, min_coord_width, max_coord_with):

        tsp_type = 'TSP'
        tsp_edge_weight_type = 'EUC_' + str(dimension) + 'D'

        f = open(filename, 'w')

        # write header
        print('NAME: {0}'.format(name), file=f)
        print('COMMENT: {0}'.format(comment), file=f)
        print('TYP: {0}'.format(tsp_type), file=f)
        print('DIMENSION: {0}'.format(cities), file=f)
        print('EDGE_WEIGHT_TYPE: {0}'.format(tsp_edge_weight_type), file=f)
        print('NODE_COORD_SECTION', file=f)

        for i in range(0,cities):
            print('{0}'.format(i+1), end=" ", file=f)

            for j in range(0, dimension):
                if j == 1:
                    print('{0}'.format(random.randrange(min_coord_height,max_coord_height)), end=" ", file=f)
                else:
                    print('{0}'.format(random.randrange(min_coord_width,max_coord_with)), end=" ", file=f)


            print('',file=f)

        f.close()

    def crowds2(self, filename, name, comment, cities, dimension, \
        width_c1, width_c2, offset):

        tsp_type = 'TSP'
        tsp_edge_weight_type = 'EUC_' + str(dimension) + 'D'

        f = open(filename, 'w')

        # write header
        print('NAME: {0}'.format(name), file=f)
        print('COMMENT: {0}'.format(comment), file=f)
        print('TYP: {0}'.format(tsp_type), file=f)
        print('DIMENSION: {0}'.format(cities), file=f)
        print('EDGE_WEIGHT_TYPE: {0}'.format(tsp_edge_weight_type), file=f)
        print('NODE_COORD_SECTION', file=f)

        for i in range(0,cities):
            print('{0}'.format(i+1), end=" ", file=f)

            if i % 2 == 0:
                # x coordinate first crowd
                print('{0}'.format(random.randrange(1,width_c1)), end=" ", file=f)
                # y coordinate first crowd
                print('{0}'.format(random.randrange(1,width_c1)), end=" ", file=f)
            else:
                # x coordinate second crowd
                print('{0}'.format(random.randrange(offset,offset+width_c2)), end=" ", file=f)
                # y coordinate second crowd
                print('{0}'.format(random.randrange(1,width_c2)), end=" ", file=f)

            print('',file=f)

        f.close()
