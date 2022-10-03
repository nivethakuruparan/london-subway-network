from Python.src.pathfinder import *
import heapq


class DijkstraPathFinder(PathFinder):
    def __init__(self):
        self.num_comparisons = 0
        self.num_data_accesses = 0

    def get_path(self, graph: dict, starting_station: str, ending_station: str):
        distances = {station: float('inf') for station in graph}
        distances[starting_station] = 0

        came_from = {station: None for station in graph}
        travel_details = {station: None for station in graph}

        queue = [(0, starting_station)]

        while queue:
            current_distance, current_station = heapq.heappop(queue)

            neighbours = graph[current_station].neighbours 
            self.num_data_accesses += 1

            for neighbour in neighbours:
                next_station = neighbour[0]
                weight = int(neighbour[2])
                self.num_data_accesses += 2

                distance_temp = current_distance + weight
                self.num_data_accesses += 1
                self.num_comparisons += 1

                if distance_temp < distances[next_station]:
                    distances[next_station] = distance_temp
                    came_from[next_station] = current_station
                    travel_details[next_station] = (neighbour[1], neighbour[2])
                    self.num_data_accesses += 2
                    heapq.heappush(queue, (distance_temp, next_station))

        if ending_station in distances and distances[ending_station] != float('inf'):
            path = [ending_station]
            details = []
            index = 0
            while path[-1] != starting_station:
                key = path[index]
                path.append(came_from[key])
                details.append(travel_details[key])
                self.num_data_accesses += 3
                index += 1

            return str(distances[ending_station]), list(reversed(path)), list(reversed(details)), self.num_comparisons, self.num_data_accesses
        else:
            return None
