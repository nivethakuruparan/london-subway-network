import itertools
import math


class UrbanismPlanning(object):
    def __init__(self, graph: dict, zones: list):
        self.graph = graph
        self.zones = zones

        self.display_zone_network()

    def dfs_util(self, temp, v, visited, graph, zone):
        visited[v] = True
        temp.append(v)

        for neighbours in graph[v].neighbours:
            neighbour = neighbours[0]
            if neighbour in graph.keys() and not visited[neighbour]:
                temp = self.dfs_util(temp, neighbour, visited, graph, zone)
        return temp

    def find_zone_network(self):
        #  Remove zones with floats
        for i in range(len(self.zones)):
            self.zones[i] = str(math.floor(float(self.zones[i])))
        self.zones = list(dict.fromkeys(self.zones))

        main_zone_dict = {zone: None for zone in self.zones}

        #  For each zone, find all stations in that zone, create a dictionary, then find connected components
        for zone in self.zones:
            zone_dict = {}

            for key in self.graph.keys():
                if self.graph[key].zone == zone or str(math.floor(float(self.graph[key].zone))) == zone or str(math.ceil(float(self.graph[key].zone))) == zone:
                    zone_dict[key] = self.graph[key]

            connected_components = self.find_connected_components(
                zone, zone_dict)

            main_zone_dict[zone] = connected_components

        return main_zone_dict

    def find_connected_components(self, zone, graph):
        visited = {station: False for station in graph}
        connected_components = []

        for v in graph.keys():
            if not visited[v]:
                temp = []
                connected_components.append(
                    self.dfs_util(temp, v, visited, graph, zone))

        return connected_components

    def display_zone_network(self):
        zone_dict = self.find_zone_network()
        connections = self.find_zone_connections(zone_dict)

        print("\n****************** URBANISM PLANNING ******************")
        print("Identifying Transportation Network...")

        print("\nDisplaying Islands in each Zone")
        for key in zone_dict.keys():
            print("Zone", key + ":")
            for island in zone_dict[key]:
                print("\tIsland:", island)

        print("\nDisplaying Connections between Zones")
        for key in connections.keys():
            if not connections[key]:
                continue
            print("Zone", key[0], "<-> Zone", key[1])
            for connection in connections[key]:
                print("\tStation", connection[0], "- Station", connection[1])

        return zone_dict, connections

    def find_zone_connections(self, zone_dict):
        zone_combs = list(itertools.permutations(zone_dict.keys(), 2))
        connections = {combination: [] for combination in zone_combs}

        # Get the neighbours' zone from each station and check if the zones match.
        # If not, there is a connection between zones!
        for zone in zone_dict.keys():
            for island in zone_dict[zone]:
                for station in island:
                    for neighbours in self.graph[station].neighbours:
                        neighbour = neighbours[0]

                        if '.' not in self.graph[neighbour].zone and self.graph[neighbour].zone != zone:
                            zone_comb = (zone, self.graph[neighbour].zone)
                            connections[zone_comb].append([station, neighbour])
                        if '.' in self.graph[neighbour].zone:
                            if str(math.floor(float(self.graph[neighbour].zone))) != zone:
                                zone_comb = (zone, str(math.floor(
                                    float(self.graph[neighbour].zone))))
                                connections[zone_comb].append(
                                    [station, neighbour])
                            if str(math.ceil(float(self.graph[neighbour].zone))) != zone:
                                zone_comb = (
                                    zone, str(math.ceil(float(self.graph[neighbour].zone))))
                                connections[zone_comb].append(
                                    [station, neighbour])

        new_zone_combs = list(itertools.combinations(
            zone_dict.keys(), 2))  # Removing duplicates
        for key in list(connections):
            if key not in new_zone_combs:
                del connections[key]

        return connections
