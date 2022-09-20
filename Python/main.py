from metrics_extractor import *
from graph import *
from path_finder import *


def main():
    stations_list = extract_data('../_dataset/london.stations.csv')
    lines_list = extract_data('../_dataset/london.lines.csv')
    connections_list = extract_data('../_dataset/london.connections.csv')

    g = Graph(stations_list, connections_list)
    print("\nNumber of Stations:", g.num_stations)
    print("Number of Connections:", g.num_connections)
    print("Average Degree of Nodes:", g.avg_degree())

    print("\nPrinting Connections for each Station")
    for key in g.connections.keys():
        print(key + ":", g.connections[key].neighbours)

    dijkstra_shortest_path(g.connections, '300', '303')


main()
