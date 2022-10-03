from Python.src.pathfinder import *
import heapq
import math


class AStarPathFinder(PathFinder):
    def __init__(self):
        self.num_comparisons = 0
        self.num_data_accesses = 0
    
    def heuristic(self, graph, current_station, end_station):
        a = [float(graph[current_station].latitude), float(graph[current_station].longitude)]
        b = [float(graph[end_station].latitude), float(graph[end_station].longitude)]

        return math.dist(a, b)

    def get_path(self, graph: dict, starting_station: str, ending_station: str):
        open_list = []
        heapq.heapify(open_list)
        heapq.heappush(open_list, starting_station)
        closed_list = []

        current_distance = {starting_station: 0}
        parents = {starting_station: starting_station}

        self.num_comparisons += 1
        while len(open_list) > 0:
            current = None

            for neighbour in open_list:
                self.num_data_accesses += 2
                self.num_comparisons += 1
                if current is None or current_distance[neighbour] + self.heuristic(graph, neighbour, ending_station) < \
                        current_distance[current] + self.heuristic(graph, current, ending_station):
                    current = neighbour

            if current is None:
                return None

            if current == ending_station:
                path = []
                travel_details = []

                while parents[current] != current:
                    self.num_data_accesses += 1
                    for neighbour in graph[current].neighbours:
                        self.num_data_accesses += 3
                        self.num_comparisons += 1
                        if neighbour[0] == parents[current]:
                            self.num_data_accesses += 3
                            travel_details.append((neighbour[1], neighbour[2]))
                            break

                    path.append(current)
                    current = parents[current]
                    self.num_data_accesses += 1

                path.append(starting_station)
                for neighbour in graph[starting_station].neighbours:
                    self.num_data_accesses += 3
                    self.num_comparisons += 1
                    if neighbour[0] == path[-2]:
                        travel_details.append((neighbour[1], neighbour[2]))
                        self.num_data_accesses += 3
                        break

                return list(reversed(path)), list(reversed(travel_details)), self.num_comparisons, self.num_data_accesses

            for neighbour in graph[current].neighbours:
                station = neighbour[0]
                self.num_data_accesses += 2
                if station not in open_list and station not in closed_list:
                    heapq.heappush(open_list, station)
                    parents[station] = current
                    current_distance[station] = current_distance[current] + 1  # making all stations a weight of one
                    self.num_data_accesses += 1

                else:
                    self.num_data_accesses += 2
                    if current_distance[station] > current_distance[current] + 1:
                        current_distance[station] = current_distance[current] + 1
                        parents[station] = current
                        self.num_data_accesses += 1

                        if station in closed_list:
                            closed_list.remove(station)
                            heapq.heappush(open_list, station)

            open_list.remove(current)
            heapq.heappush(closed_list, current)

        return None
