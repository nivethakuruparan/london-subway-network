import pyperf
import matplotlib.pyplot as pplot
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


def plot_results(xlist, ylist, yname, tname):
    sheet = pplot.figure()
    bar_gr = sheet.add_axes([0,0,1,1])
    bar_gr.bar(xlist, ylist)
    bar_gr.set_ylabel(yname)
    bar_gr.set_xlabel('Number of Connections Tested')
    bar_gr.set_title(tname)
    pplot.show()

def main():
    alg_list = generate_alg_list()
    data_list = generate_data()
    stations_list = me.extract_data('_dataset/london.stations.csv')
    lines_list = me.extract_data('_dataset/london.lines.csv')
    connections_list = me.extract_data('_dataset/london.connections.csv')
    
    g = Graph(stations_list, lines_list, connections_list)

    # for i in data_list:
    #     pair_list = data_list[i]
    #     for j in pair_list:
    #         print(j[0])
    #         print(j[1])

    ind, noc0, noda0 = do_bench(alg_list[0],g.connections,data_list)
    ind, noc1, noda1 = do_bench(alg_list[1],g.connections,data_list)
    
    print("Dijktra")
    print("NOC")
    print(noc0)
    print("NODA")
    print(noda0)
    
    print("*********")
    print("NOC")
    print(noc1)
    print("NODA")
    print(noda1)

    plot_results(ind, noc0, "Number of Comparisons", alg_list[0])
    plot_results(ind, noda0, "Number of Data Accesses", alg_list[1])
    plot_results(ind, noc1, "Number of Comparisons", alg_list[1])
    plot_results(ind, noda1, "Number of Data Accesses", alg_list[1])


if __name__ == "__main__":
    main()
