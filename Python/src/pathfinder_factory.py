from Python.src.dijkstra_pathfinder import *
from Python.src.a_star_pathfinder import *
from Python.src.bfs_pathfinder import *


class PathFinderFactory(object):
    @staticmethod
    def get_algorithm(name, graph: dict, starting_station: str, ending_station: str):
        if name == 'Dijkstra':
            dijkstra = DijkstraPathFinder()
            return lambda: dijkstra.get_path(graph, starting_station, ending_station)
        elif name == 'A Star':
            a_star = AStarPathFinder()
            return lambda: a_star.get_path(graph, starting_station, ending_station)
        elif name == 'BFS':
            bfs = BFSPathFinder()
            return lambda: bfs.get_path(graph, starting_station, ending_station)
