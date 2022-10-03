from Python.src.pathfinder import *


class BFSPathFinder(PathFinder):
    def get_path(self, graph, starting_station: str, ending_station: str):
        queue = [(starting_station, [starting_station])]

        while queue:
            (vertex, path) = queue.pop(0)

            neighbours = set()
            for neighbour in graph[vertex].neighbours:
                neighbours.add(neighbour[0])

            for next_station in (neighbours - set(path)):
                if next_station == ending_station:
                    yield path + [next_station]
                elif len(path) > 10:
                    break
                else:
                    queue.append((next_station, path + [next_station]))
