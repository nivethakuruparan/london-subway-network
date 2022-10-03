from Python.src.PathFinder import PathFinder 
# from PathFinder import PathFinder
import heapq
import math 

class AStarPathFinder(PathFinder):
    def __init__(self, pq):
        return 

    def heuristic(self,graph, current_station, end_station):
        a = [float(graph[current_station].latitude), float(graph[current_station].longitude)]
        b = [float(graph[end_station].latitude), float(graph[end_station].longitude)]

        return math.dist(a, b)

    def check_exists(self, graph, st):
        for i in graph:
            if (st == i):
                return True
        return False 

    def get_path(self, path_query):
        graph = path_query[0]
        starting_station = path_query[1]
        ending_station = path_query[2]

        if not(self.check_exists(graph, starting_station) and self.check_exists(graph, ending_station)):
            return None 

    # def get_path(self,graph, starting_station: str, ending_station: str):
        noc = 0
        noda = 0
        open_list = []
        heapq.heapify(open_list)
        heapq.heappush(open_list, starting_station)
        closed_list = []
        
        current_distance = {starting_station: 0}
        parents = {starting_station: starting_station}

        noc += 1
        while len(open_list) > 0:
            current = None

            for neighbour in open_list:
                noc += 1
                noda += 2
                if current is None or current_distance[neighbour] + self.heuristic(graph, neighbour, ending_station) < current_distance[current] + self.heuristic(graph, current, ending_station):
                    current = neighbour

            if current is None:
                return None

            if current == ending_station:
                path = []
                travel_details = []
                total_time = 0
                while parents[current] != current:
                    noda += 1
                    for neighbour in graph[current].neighbours:
                        noda+=3
                        noc += 1
                        if neighbour[0] == parents[current]:
                            noda += 3
                            travel_details.append((neighbour[1], neighbour[2]))
                            break

                    path.append(current)
                    current = parents[current] 
                    noda += 1

                path.append(starting_station)
                for neighbour in graph[starting_station].neighbours:
                    noda += 3
                    noc += 1
                    if neighbour[0] == path[-2]:
                        travel_details.append((neighbour[1], neighbour[2]))
                        noda += 3
                        break

                for i in range(1, len(path)):
                    total_time += int(travel_details[i-1][1])


                return str(total_time), list(reversed(path)), list(reversed(travel_details)), noc, noda

            for neighbour in graph[current].neighbours:
                station = neighbour[0]
                noda+=2
                if station not in open_list and station not in closed_list:
                    heapq.heappush(open_list, station)
                    # open_list.add(station)
                    parents[station] = current
                    current_distance[station] = current_distance[current] + 1
                    noda += 1

                else:
                    noda += 2
                    if current_distance[station] > current_distance[current] + 1:
                        current_distance[station] = current_distance[current] + 1
                        parents[station] = current
                        noda += 1

                        if station in closed_list:
                            closed_list.remove(station)
                            # open_list.add(station)
                            heapq.heappush(open_list, station)

            open_list.remove(current)
            # closed_list.add(current)
            heapq.heappush(closed_list, current)

        return None
