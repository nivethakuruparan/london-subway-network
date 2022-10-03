import pyperf
import matplotlib.pyplot as matplot
import numpy as numpy

import Benchmarking.benchmark_data as benchmark_data
from Python.GraphBuilder.graph import Graph
from Python.PathFinder.pathfinder_factory import PathFinderFactory as pathfinder_factory
import Python.metrics_extractor as metrics_extractor


def get_data():
    return benchmark_data.generate_kpi_data()

def generate_algorithm_list():
    return ['Dijkstra', 'A Star']

def do_bench(algorithm_name: str, graph: dict, bench_data):
    data_index = []
    num_comparisons_results = []
    num_data_acceses_results = []

    for bench in bench_data:
        pair_list = bench_data[bench]

        for pair in pair_list:
            result = pathfinder_factory.get_algorithm(algorithm_name, graph, pair[0], pair[1])()
            num_comparison = result[-2]
            num_data_accesses = result[-1]
        
        data_index.append(bench)
        num_comparisons_results.append(num_comparison)
        num_data_acceses_results.append(num_data_accesses)

    return data_index, num_comparisons_results, num_data_acceses_results

def plot_results(x_list, noc_list, noda_list, alg_name):
    x_axis = numpy.arange(len(x_list))
    matplot.bar(x_axis - 0.2, noc_list, 0.4, label="Number of Comparisons")
    matplot.bar(x_axis + 0.2, noda_list, 0.4, label="Number of Data Accesses")
    matplot.xticks(x_axis, x_list)
    matplot.xlabel("Size of Input")
    matplot.ylabel("Number of Comparisons/Data Accessses")
    matplot.title("KPIs for " + alg_name)
    matplot.legend()
    matplot.show()


def print_results(x_list, d_list, a_list, title):
    print("\n************" + title + "************")
    print("------------------------------------------------")
    print("Input Size \t Dijkstra's \t AStar")
    print("------------------------------------------------")
    for i in range(0, len(x_list)):
        print("\n")
        print(str(x_list[i]) + "\t \t " + str(d_list[i]) + "\t \t" + str(a_list[i]))


def main():
    alg_list = generate_algorithm_list()
    data_list = get_data()
    stations_list = metrics_extractor.extract_data('_dataset/london.stations.csv')
    lines_list = metrics_extractor.extract_data('_dataset/london.lines.csv')
    connections_list = metrics_extractor.extract_data('_dataset/london.connections.csv')

    gr = Graph(stations_list, lines_list, connections_list).connections

    ind, noc0, noda0 = do_bench(alg_list[0], gr, data_list)
    ind, noc1, noda1 = do_bench(alg_list[1], gr, data_list)

    print("Displaying KPIs for Path Finding Algorithms")
    print("Input Size refers to number of station connections requested")
    print_results(ind, noc0, noc1, "Number of Comparisons")
    print_results(ind, noda0, noda1, "Number of Data Accesses")

    plot_results(ind, noc0, noda0, alg_list[0])
    plot_results(ind, noc1, noda1, alg_list[1])