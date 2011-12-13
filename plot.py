from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt

class Plot():
    ''' Plot a figure '''

    def __init__(self, file_location='data/plot/solution.pdf'):
        self.pdf_file = PdfPages(file_location)

    def plot_graph(self, graph, title=''):
        fig = plt.figure()
        fig.suptitle(title, fontsize=12)


        for edge in graph.edges:
            list_x = [edge.node_1.x, edge.node_2.x]
            list_y = [edge.node_1.y, edge.node_2.y]
            plt.plot(list_x, list_y, marker='o', color='#000000')
            plt.text(edge.node_1.x+0.5,edge.node_1.y+1,va='center',\
                    s=edge.node_1.nr,color='#000000',fontsize=12)
            plt.text(edge.node_2.x+0.5,edge.node_2.y+1,va='center',\
                    s=edge.node_2.nr,color='#000000',fontsize=12)

        # scale axis to have some space
        x_scale_lower = plt.gca().get_xaxis().get_data_interval()[0]
        x_scale_upper = plt.gca().get_xaxis().get_data_interval()[1]
        x_factor = 0.1 * abs(x_scale_upper)
        x_scale_upper += x_factor
        x_scale_lower -= x_factor

        y_scale_lower = plt.gca().get_yaxis().get_data_interval()[0]
        y_scale_upper = plt.gca().get_yaxis().get_data_interval()[1]
        y_factor = 0.1 * abs(y_scale_upper)
        y_scale_upper += y_factor
        y_scale_lower -= y_factor

        plt.axis([x_scale_lower,x_scale_upper,y_scale_lower,y_scale_upper])

        self.pdf_file.savefig()

    def plot_nodes(self, nodes, title=''):
        fig = plt.figure()
        fig.suptitle(title, fontsize=12)

        for idx, node in enumerate(nodes):
            if idx > 0:
                list_x = [nodes[idx-1].x, nodes[idx].x]
                list_y = [nodes[idx-1].y, nodes[idx].y]
                plt.plot(list_x, list_y, marker='o', color='#000000')
                plt.text(node.x+0.5,node.y+0.5,va='center',\
                            s=node.nr,color='#000000',fontsize=12)

        # scale axis to have some space
        x_scale_lower = plt.gca().get_xaxis().get_data_interval()[0]
        x_scale_upper = plt.gca().get_xaxis().get_data_interval()[1]
        x_factor = 0.1 * abs(x_scale_upper)
        x_scale_upper += x_factor
        x_scale_lower -= x_factor

        y_scale_lower = plt.gca().get_yaxis().get_data_interval()[0]
        y_scale_upper = plt.gca().get_yaxis().get_data_interval()[1]
        y_factor = 0.1 * abs(y_scale_upper)
        y_scale_upper += y_factor
        y_scale_lower -= y_factor

        plt.axis([x_scale_lower,x_scale_upper,y_scale_lower,y_scale_upper])

        self.pdf_file.savefig()

    def save_file(self):
        self.pdf_file.close()
