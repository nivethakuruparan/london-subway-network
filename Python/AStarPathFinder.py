from Python.PathFinder import PathFinder 
import heapq
import math 

class AStarPathFinder(PathFinder):
    def __init__(self, graph, start, end):
        return 

    def heuristic(self,graph, current_station, end_station):
        a = [float(graph[current_station].latitude), float(graph[current_station].longitude)]
        b = [float(graph[end_station].latitude), float(graph[end_station].longitude)]

        return math.dist(a, b)


    def get_path(self,graph, starting_station: str, ending_station: str):
        open_list = []
        heapq.heapify(open_list)
        heapq.heappush(open_list, starting_station)
        closed_list = []
        
        current_distance = {starting_station: 0}
        parents = {starting_station: starting_station}

        while len(open_list) > 0:
            current = None

            for neighbour in open_list:
                if current is None or current_distance[neighbour] + self.heuristic(graph, neighbour, ending_station) < current_distance[current] + self.heuristic(graph, current, ending_station):
                    current = neighbour

            if current is None:
                return None

            if current == ending_station:
                path = []
                travel_details = []
                total_time = 0

                while parents[current] != current:
                    for neighbour in graph[current].neighbours:
                        if neighbour[0] == parents[current]:
                            total_time += int(neighbour[2])
                            travel_details.append((neighbour[1], neighbour[2]))
                            break

                    path.append(current)
                    current = parents[current]

                path.append(starting_station)
                for neighbour in graph[starting_station].neighbours:
                    if neighbour[0] == path[-2]:
                        total_time += int(neighbour[2])
                        travel_details.append((neighbour[1], neighbour[2]))
                        break

                return str(total_time), list(reversed(path)), list(reversed(travel_details))

            for neighbour in graph[current].neighbours:
                station = neighbour[0]
                if station not in open_list and station not in closed_list:
                    heapq.heappush(open_list, station)
                    # open_list.add(station)
                    parents[station] = current
                    current_distance[station] = current_distance[current] + 1

                else:
                    if current_distance[station] > current_distance[current] + 1:
                        current_distance[station] = current_distance[current] + 1
                        parents[station] = current

                        if station in closed_list:
                            closed_list.remove(station)
                            # open_list.add(station)
                            heapq.heappush(open_list, station)

            open_list.remove(current)
            # closed_list.add(current)
            heapq.heappush(closed_list, current)

        return None
