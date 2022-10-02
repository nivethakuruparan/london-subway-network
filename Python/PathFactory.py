# from Python.BFSPathFinder import *
from operator import methodcaller
from Python.DijkstraPathFinder import *
from Python.AStarPathFinder import *
# from DijkstraPathFinder import *
# from AStarPathFinder import *
class PathFactory():
    @staticmethod
    def display_path(alg_name, path_res):
        if(path_res==None):
            return 
        if(alg_name == "Dijkstra"):
            print("Displaying route with least amount of time")
        elif(alg_name == "AStar"):
            print("Displaying route with least number of stations")
        time = path_res[0]
        path = path_res[1]
        details = path_res[2]
        for i in range(1,len(path)):
            print('Station', path[i - 1], end=' -> ')
            print('Station', path[i], end=' ')
            print('(Line:', str(details[i-1][0]), 'Time:', str(details[i-1][1]) + ')')
        print("Total time:", time)
        print("Total number of stations:",len(path))

    @staticmethod
    def build(alg_name,pq):
        if alg_name == 'Dijkstra':
            res = DijkstraPathFinder(pq)
            return lambda: res.get_path(pq)
        elif alg_name == 'AStar':
            res = AStarPathFinder(pq)
            return lambda: res.get_path(pq)
    # @staticmethod
    # def build(alg_name, g, start, end):
    #     if alg_name == 'Dijkstra':
    #         res = DijkstraPathFinder(g,start,end)
    #         return lambda: res.get_path(g,start,end)
    #     elif alg_name == 'AStar':
    #         res = AStarPathFinder(pq)
    #         return lambda: res.get_path(g,start,end)

    # @staticmethod
    # def build(alg_name, g, start, end):
    #     if alg_name == 'Dijkstra':
    #         res = DijkstraPathFinder(g,start,end)
    #         result = res.get_path(g,start,end)
    #         return result 
    #     elif alg_name == 'AStar':
    #         res = AStarPathFinder(g,start,end)
    #         result = res.get_path(g,start,end)
    #         return result
    #     # elif alg_name == 'BFS':
    #     #     res = BFSPathFinder(g,start,end)
    #     #     result = res.get_path(g,start,end)
    #     #     if(len(result) == 0):
    #     #         print('no bfs path')
    #     #     else:
    #     #         print('\Displaying other routes')
    #     #         for i in range(len(result)):
    #     #             if result[i][j] == result[i][-1]:
    #     #                 print('Station', result[i][j])
    #     #             else:
    #     #                 print('Station', result[i][j], end=' -> ')
