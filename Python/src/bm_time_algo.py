import pyperf
# from PathFactory import PathFactory as pf
# import metrics_extractor as me
# import bm_data as btd
# from graph import Graph
import Python.src.bm_data as btd
from Python.src.graph import Graph 
from Python.src.PathFactory import PathFactory as pf 
import Python.src.metrics_extractor as me

def generate_alg_list():
    return ["Dijkstra", "AStar"]

def get_data(gr):
    return btd.generate_time_data(gr)

def do_bench(alg_list, gr, bench_data):
    runner = pyperf.Runner()
    for alg in alg_list:
        for j in bench_data.keys():
            i = bench_data[j]
            path_query = [gr, i[0],i[1]]
            path_finder = pf.build(alg, path_query)
            bname  = alg + " for starting station of degree "+ str(j)
            runner.bench_func(bname, path_finder)

def main():
    stations_list = me.extract_data('_dataset/london.stations.csv')
    lines_list = me.extract_data('_dataset/london.lines.csv')
    connections_list = me.extract_data('_dataset/london.connections.csv')
    
    gr = Graph(stations_list, lines_list, connections_list).connections
    dataset = get_data(gr)
    alg_list = generate_alg_list()
    do_bench(alg_list, gr, dataset)

# def execute():
#     main()