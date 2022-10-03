from Python.src.pathfinder_factory import *
import itertools


class SubwayPatrolPlanning(object):
    def __init__(self, graph, station_list):
        self.graph = graph
        self.station_list = station_list

        self.display_shortest_path()

    def find_shortest_path(self):
        #  Get all combinations of PAIRS of the station list
        combinations = list(itertools.permutations(self.station_list, 2))
        paths = {combination: None for combination in combinations}
        least_num_stations = float('inf')
        least_path_stations = []

        #  Get the shortest path for each combination and add to dictionary
        for combination in combinations:
            starting_station = combination[0]
            ending_station = combination[1]

            pathfinder = PathFinderFactory()
            paths[combination] = pathfinder.get_algorithm(
                'A Star', self.graph, starting_station, ending_station)()[0]

        #  Get all the permutations of the stations, excluding the first station
        permutations = list(itertools.permutations(self.station_list[1:]))

        #  Add the first station to start and end of each permutation
        for i in range(len(permutations)):
            permutations[i] = list(permutations[i])
            permutations[i].insert(0, self.station_list[0])
            permutations[i].append(self.station_list[0])

        #  Create a temporary path by combining the shortest path for each permutation
        for permutation in permutations:
            temp_path = []

            for i in range(1, len(permutation)):
                comb = (permutation[i - 1], permutation[i])
                if i != len(permutation) - 1:
                    temp_path.append(paths[comb][:-1])
                else:
                    temp_path.append(paths[comb])

            temp_path = list(itertools.chain.from_iterable(temp_path))

            #  Check if the temporary path is shorter
            if len(temp_path) < least_num_stations:
                least_num_stations = len(temp_path)
                least_path_stations = temp_path

        return least_path_stations, least_num_stations

    def display_shortest_path(self):
        least_path_stations, least_num_stations = self.find_shortest_path()

        print("\n****************** SUBWAY PATROL PLANNING ******************")
        print("Station List:", self.station_list)
        print("Creating Subway Patrol Planner...")

        print("\nRoute:", end=' ')
        for i in range(len(least_path_stations)):
            if i == len(least_path_stations) - 1:
                print('Station', least_path_stations[i])
            else:
                print('Station', least_path_stations[i], end=' -> ')

        print("Number of Stations:", least_num_stations)

        return least_path_stations, least_num_stations
