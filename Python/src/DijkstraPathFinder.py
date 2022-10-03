import heapq
from Python.src.PathFinder import PathFinder
# from PathFinder import PathFinder
class DijkstraPathFinder(PathFinder):
    def __init__(self, pq):
        return 

    def check_exists(self, graph, st):
        for i in graph:
            if (st == i):
                return True
        return False

    def dijkstra(self, graph, starting_station: str):
        noc = 0
        noda = 0 
        distances = {station: float('inf') for station in graph}
        distances[starting_station] = 0
        came_from = {station: None for station in graph}
        travel_details = {station: None for station in graph}
        queue = [(0, starting_station)]

        while queue:
            current_distance, current_station = heapq.heappop(queue)

            neighbours = graph[current_station].neighbours 
            noda += 1

            for neighbour in neighbours:
                next_station = neighbour[0]
                weight = int(neighbour[2])
                noda += 2

                distance_temp = current_distance + weight
                noc += 1
                noda += 1
                if distance_temp < distances[next_station]:
                    distances[next_station] = distance_temp
                    came_from[next_station] = current_station
                    travel_details[next_station] = (neighbour[1], neighbour[2])
                    noda += 2
                    heapq.heappush(queue, (distance_temp, next_station))

        return distances, came_from, travel_details, noc, noda

    def get_path(self, path_query):
        graph = path_query[0]
        starting_station = path_query[1]
        ending_station = path_query[2]
        
        if not(self.check_exists(graph, starting_station) and self.check_exists(graph, ending_station)):
            return None 
    # def get_path(self, graph, starting_station: str, ending_station: str):
        
        distances, came_from, travel_details, noc, noda = self.dijkstra(graph, starting_station)
        noda += 1
        if ending_station in distances and distances[ending_station] != float('inf'):
            path = [ending_station]
            details = []
            index = 0
            while path[-1] != starting_station:
                key = path[index]
                path.append(came_from[key])
                details.append(travel_details[key])
                noda += 3
                index += 1

            return str(distances[ending_station]), list(reversed(path)), list(reversed(details)), noc, noda
            # noc : a kpi : number of comparisons 
            # noda : a kpi : number of data accesses 
        else:
            return None
