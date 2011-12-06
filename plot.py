from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt

class Plot():
    ''' Plot a figure '''

    def plot_graph(self, graph, file_location='data/plot/solution.pdf'):
        f = PdfPages(file_location)
        plt.figure()

        for edge in graph.edges:
            list_x = [edge.node_1.x, edge.node_2.x]
            list_y = [edge.node_1.y, edge.node_2.y]
            plt.plot(list_x, list_y, marker='o', color='#000000')

        f.savefig()
        f.close()
