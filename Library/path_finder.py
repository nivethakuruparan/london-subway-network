import heapq


def dijkstra(graph, starting_station):
    distances = {station: float('inf') for station in graph}
    distances[starting_station] = 0
    came_from = {station: None for station in graph}
    queue = [(0, starting_station)]

    while queue:
        current_distance, current_station = heapq.heappop(queue)

        neighbours = graph[current_station].neighbours

        for neighbour in neighbours:
            next_station = neighbour[0]
            weight = int(neighbour[2])

            distance_temp = current_distance + weight
            if distance_temp < distances[next_station]:
                distances[next_station] = distance_temp
                came_from[next_station] = current_station
                heapq.heappush(queue, (distance_temp, next_station))

    return distances, came_from


def dijkstra_shortest_path(graph, starting_station, ending_station):
    print("\nComputing Graph Using Dijkstra's Algorithm")
    distances, came_from = dijkstra(graph, starting_station)
    if ending_station in distances and distances[ending_station] != float('inf'):
        print("The least amount of time to go from Station", starting_station, "to Station", ending_station, "is", str(distances[ending_station]))

        path = [ending_station]
        index = 0
        while path[-1] != starting_station:
            key = path[index]
            path.append(came_from[key])
            index += 1

        print('Path:', end=' ')
        for p in reversed(path):
            if p != path[0]:
                print('Station', p, '->', end=' ')
            else:
                print('Station', p)
    else:
        print("There is no path connecting from Station", starting_station, "to Station", ending_station)
