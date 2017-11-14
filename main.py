import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from network import Network
from generate_data import generate_data

def label_to_color(label):
	red = (label + 1) / 2
	green = 0
	blue = 1 - (label + 1) / 2
	alpha = 1
	return [red, green, blue, alpha]

def plot_data(data):
	xCoords = []
	yCoords = []
	labels = []
	for point in data:
		xCoords.append(point['coord'][0])
		yCoords.append(point['coord'][1])
		labels.append(point['label'])

	colors = []
	for label in labels:
		colors.append(label_to_color(label))

	plt.scatter(xCoords, yCoords, c=colors)

def plot_network(network):
	x = y = np.arange(-3.0, 3.0, 0.05)
	X, Y = np.meshgrid(x, y)
	Z = np.array([network.evaluate([x, y]) for (x,y) in zip(X.ravel(), Y.ravel())]).reshape(X.shape)

	levels = [0]

	plt.contour(X, Y, Z, levels, colors='black')

clusters = [[1, 1], [-1, -1], [1, -1], [-1, 1], [2, 0], [-2, 0], [-2, 2]]
labels = [-1, -1, 1, 1, -1, 1, -1]

data = generate_data(clusters, labels, 1, 20)

G = nx.DiGraph()

G.add_nodes_from(range(0, 2), type='input')
G.add_nodes_from(range(2, 6), type='hidden')
G.add_nodes_from(range(6, 7), type='output')

for i in range(0, 2):
	for j in range(2, 6):
		G.add_edge(i, j)

for i in range(2, 6):
	for j in range(6, 7):
		G.add_edge(i, j)

net = Network(G)

for j in range(0, 300):
	for j in range (0, len(data)):
		net.learn(data[j]['coord'], [data[j]['label']])

plot_data(data)
plot_network(net)

plt.xlabel('x1')
plt.ylabel('x2')

plt.show()