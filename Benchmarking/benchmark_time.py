import pyperf
import Benchmarking.benchmark_data as benchmark_data
from Python.GraphBuilder.graph import Graph
from Python.PathFinder.pathfinder_factory import PathFinderFactory as pathfinder_factory
import Python.metrics_extractor as metrics_extractor


def get_data(graph):
    return benchmark_data.generate_time_data(graph)

def generate_algorithm_list():
    return ['Dijkstra', 'A Star']

def do_bench(algorithm_list, graph, bench_data):
    runner = pyperf.Runner()

    for algorithm in algorithm_list:
        for key in bench_data.keys():
            value = bench_data[key]

            result = pathfinder_factory.get_algorithm(algorithm, graph, value[0], value[1])

            bench_name = algorithm + " for starting station of degree " + str(key)
            runner.bench_func(bench_name, result)

def main():
    stations_list = metrics_extractor.extract_data('_dataset/london.stations.csv')
    lines_list = metrics_extractor.extract_data('_dataset/london.lines.csv')
    connections_list = metrics_extractor.extract_data('_dataset/london.connections.csv')
    
    g = Graph(stations_list, lines_list, connections_list)
    data_set = get_data(g.connections)
    algorithm_list = generate_algorithm_list()
    
    do_bench(algorithm_list, g.connections, data_set)
