from Python.PathFactory import PathFactory as pf
from Python.graph import Graph
# from PathFactory import PathFactory as pf
# from graph import Graph


class Itinerary:
    def __init__(self, graph, starting_station:str, ending_station:str):
        self.graph = graph
        self.starting_station = starting_station
        self.ending_station = ending_station
        self.create_itinerary()

    def create_itinerary(self):
        print('\nStarting station: ', self.starting_station)
        print('Destination: ', self.ending_station)
        print('\nCreating itinerary...')

        least_time = self.least_time()

        if not least_time:
            print('Route does not exist! Please enter different starting station or destination.')
            return 

        least_stations = self.least_stations(least_time)

    def least_time(self):
        algo_name = "Dijkstra"
        path_query = [self.graph, self.starting_station, self.ending_station]
        path_res = pf.build(algo_name, path_query)()
        if not path_res:
            return None 
        pf.display_path(algo_name, path_res)
        return path_res[1]

    def least_stations(self, least_time):
        algo_name = "AStar"
        path_query = [self.graph, self.starting_station, self.ending_station]
        path_res = pf.build(algo_name, path_query)()

        if path_res[1] == least_time or len(path_res[1]) == len(least_time):
            return None 
        pf.display_path(algo_name, path_res)
        return path_res[1]

    def alternative_routes(self, least_time, least_stations):
        algo_name = "BFS"
        path_query = [self.graph, self.starting_station, self.ending_station]
        path_res = pf.build(algo_name, path_query)()

        if least_time in path_res:
            path_res.remove(least_time)

        if least_stations in path_res:
            path_res.remove(least_stations)
        
        if not path_res:
            return None

        pf.display_path(path_res)
