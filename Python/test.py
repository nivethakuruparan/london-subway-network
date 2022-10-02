from PathFactory import PathFactory as pf
from graph import Graph 
import metrics_extractor as me 
import bm_time_data as btd
def test_this():
    stations_list = me.extract_data('../_dataset/london.stations.csv')
    lines_list = me.extract_data('../_dataset/london.lines.csv')
    connections_list = me.extract_data('../_dataset/london.connections.csv')
    
    g = Graph(stations_list, lines_list, connections_list)
    print(btd.generate_time_data(g.connections))

test_this()
