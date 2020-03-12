import networkx as nx 
import matplotlib.pyplot as plt

# this function reads from a file the graph information
# currently a dummy file
# param: file_path
# return edges in list of tuples 
def read_edges(file_path):

	return [(1,2), (1,6), (2,3)]

def read_nodes(file_path):

	return [1,2,3,6]

edges = read_edges("dummy_path")
G = nx.Graph()
G.add_edges_from(edges)
nx.draw_networkx(G, with_label = True)

plt.show()

