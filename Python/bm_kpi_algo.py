import pyperf
import matplotlib.pyplot as pplot
import numpy as np
# from graph import Graph 
# from PathFactory import PathFactory as pf 
# import metrics_extractor as me
from Python.graph import Graph 
from Python.PathFactory import PathFactory as pf 
import Python.metrics_extractor as me
import Python.bm_kpi_data as bkd

def generate_data():
    return bkd.generate_kpi_data()

def generate_alg_list():
    alg1 = 'Dijkstra'
    alg2 = 'AStar'
    return [alg1,alg2]

def do_bench(alg:str, gr, bench_data):
    data_ind = []
    noc_results = []
    noda_results = []
    for i in bench_data:
        pair_list = bench_data[i]
        noc = 0
        noda = 0 
        for j in pair_list:
            result = pf.build(alg, gr, j[0], j[1])
            noc += result[3]
            noda += result[4]
        data_ind.append(i)
        noc_results.append(noc)
        noda_results.append(noda)
    return data_ind, noc_results, noda_results  


# def plot_results(xlist, yDlist, yAlist, yname):
#     x_axis = np.arange(len(xlist))
#     pplot.bar(x_axis - 0.2, yDlist, 0.4, label = "Dijkstra")
#     pplot.bar(x_axis + 0.2, yAlist, 0.4, label = "AStar" )
#     pplot.xticks(x_axis, xlist)
#     pplot.xlabel('Algorithms')
#     pplot.ylabel(yname)
#     pplot.title('For Dijkstra and A Star Algorithm')
#     pplot.legend()
#     pplot.show()

def plot_results(x_list, noc_list, noda_list, alg_name):
    x_axis = np.arange(len(x_list))
    pplot.bar(x_axis - 0.2, noc_list, 0.4, label = "Number of Comparisons")
    pplot.bar(x_axis + 0.2, noda_list, 0.4, label = "Number of Data Accesses")
    pplot.xticks(x_axis, x_list)
    pplot.xlabel("Size of Input")
    pplot.ylabel("Number of Comparisons/Data Accessses")
    pplot.title("KPIs for "+ alg_name)
    pplot.legend()
    pplot.show()

def print_results(x_list, d_list, a_list, title):
    print("\n************"+title+"************")
    print("------------------------------------------------")
    print("Input Size \t Dijkstra's \t AStar")
    print("------------------------------------------------")
    for i in range(0, len(x_list)):
        print("\n")
        print(str(x_list[i])+ "\t \t " + str(d_list[i]) + "\t \t" + str(a_list[i]))

def main():
    alg_list = generate_alg_list()
    data_list = generate_data()
    stations_list = me.extract_data('_dataset/london.stations.csv')
    lines_list = me.extract_data('_dataset/london.lines.csv')
    connections_list = me.extract_data('_dataset/london.connections.csv')
    
    g = Graph(stations_list, lines_list, connections_list)

    ind, noc0, noda0 = do_bench(alg_list[0],g.connections,data_list)
    ind, noc1, noda1 = do_bench(alg_list[1],g.connections,data_list)

    print("Displaying KPIs for Path Finding Algorithms")
    print("Input Size refers to number of station connections requested")
    print_results(ind, noc0, noc1, "Number of Comparisons")
    print_results(ind, noda0, noda1, "Number of Data Accesses")

    plot_results(ind, noc0, noda0, alg_list[0])
    plot_results(ind, noc1, noda1, alg_list[1])


if __name__ == "__main__":
    main()
