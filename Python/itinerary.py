from Python.PathFinder.pathfinder_factory import *


class Itinerary(object):
    def __init__(self, graph: dict, starting_station: str, ending_station: str):
        self.graph = graph
        self.starting_station = starting_station
        self.ending_station = ending_station

        self.create_itinerary()

    def create_itinerary(self):
        print("\n****************** ITINERARY ******************")
        print("Starting Station:", self.starting_station)
        print("Destination:", self.ending_station)
        print("Creating Itinerary...")

        pathfinder = PathFinderFactory()

        least_time = self.least_time(pathfinder)

        if not least_time:
            print("\nRoute does not exist! Please enter different starting station or destination.")
            return

        least_stations = self.least_stations(pathfinder, least_time)
        self.alternative_routes(pathfinder, least_time, least_stations)


    def least_time(self, pathfinder):
        dijkstra_output = pathfinder.get_algorithm('Dijkstra', self.graph, self.starting_station, self.ending_station)()

        if not dijkstra_output:
            return None

        print("\nDisplaying route with the least amount of time:")

        path = dijkstra_output[1]
        details = dijkstra_output[2]

        for i in range(1, len(path)):
            print('Station', path[i - 1], end=' -> ')
            print('Station', path[i], end=' ')
            print('(Line:', str(details[i-1][0]), 'Time:', str(details[i-1][1]) + ')')

        print("Total Time:", dijkstra_output[0])
        print("Total Number of Stations:", len(path))

        return list(path)

    def least_stations(self, pathfinder, least_time):
        a_star_output = pathfinder.get_algorithm('A Star', self.graph, self.starting_station, self.ending_station)()

        if a_star_output[0] == least_time or len(a_star_output[0]) == len(least_time):
            return None

        print("\nDisplaying route with the least amount of stations:")

        path = a_star_output[0]
        details = a_star_output[1]

        total_time = 0

        for i in range(1, len(path)):
            print('Station', path[i - 1], end=' -> ')
            print('Station', path[i], end=' ')
            print('(Line:', str(details[i - 1][0]), 'Time:', str(details[i - 1][1]) + ')')
            total_time += int(details[i - 1][1])

        print("Total Time:", total_time)
        print("Total Number of Stations:", len(path))

        return list(path)

    def alternative_routes(self, pathfinder, least_time, least_stations):
        bfs_output = list(pathfinder.get_algorithm('BFS', self.graph, self.starting_station, self.ending_station)())

        if least_time in bfs_output:
            bfs_output.remove(least_time)

        if least_stations in bfs_output:
            bfs_output.remove(least_stations)

        if not bfs_output:
            return None

        print("\nDisplaying alternative routes:")

        for i in range(len(bfs_output)):
            if i > 3:
                break
            print(i + 1, end=': ')
            for j in range(len(bfs_output[i])):
                if bfs_output[i][j] == bfs_output[i][-1]:
                    print('Station', bfs_output[i][j])
                else:
                    print('Station', bfs_output[i][j], end=' -> ')
