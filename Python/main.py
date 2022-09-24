from metrics_extractor import *
from graph import *
from itinerary import *


def main():
    stations_list = extract_data('../_dataset/london.stations.csv')
    lines_list = extract_data('../_dataset/london.lines.csv')
    connections_list = extract_data('../_dataset/london.connections.csv')

    g = Graph(stations_list, lines_list, connections_list)
    print("\nNumber of Stations:", g.num_stations)
    print("Number of Connections:", g.num_connections)
    print("Number of Lines:", g.num_lines)
    print("Average Degree of Nodes:", g.avg_degree())

    print("\nPrinting Connections for each Station")
    for key in g.connections.keys():
        print(key + ":", g.connections[key].neighbours)

    Itinerary(g.connections, '11', '273') 
    Itinerary(g.connections, '11', '193')
    Itinerary(g.connections, '11', '400')


main()
