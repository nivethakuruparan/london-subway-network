import pprint
from extractor import *
from graph import *
from a_star import *

connections = extract_data('../_dataset/london.connections.csv')
lines = extract_data('../_dataset/london.stations.csv')

g = Graph(connections, lines)
 #change to undirected 
 #uncomment a star path and see if it works 

#IMPORTANT change termnilogy in graph class 
print('start')
print("Number of Stations:", g.vertices) #change vertices --> stations 
print("Number of Edges:", g.edges)
print("Average Degree of Nodes:", g.avg_degree())

print("\nPrinting Connections for each Station")
for key in g.graph.keys():
    print(key)
    print(g.graph[key].adjacent)

a_star_path(g, 11, 123)
print("end")