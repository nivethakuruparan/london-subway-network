import pytest 

# from src.graph import Graph
# from src.PathFactory import PathFactory as pf
# from src import metrics_extractor as me

from Python.src.graph import Graph
from Python.src.PathFactory import PathFactory as pf
import Python.src.metrics_extractor as me

@pytest.fixture
def no_path() -> list[str]:
    return ['11','400']
#no path exists between the pair

# @pytest.fixture
# def one_path() -> list[str]:
#     return ['','']
# # exactly one path exists between the pair

@pytest.fixture 
def two_diff_paths() -> list[str]:
    return ['11','193']
#two paths exists between the pair, one takes less time and other has less number of stations 

@pytest.fixture 
def two_same_paths() -> list[str]:
    return ['11','273']
#two paths exist between the pair, both take same amount of time and same number of stations 

@pytest.fixture
def no_stations() -> list[str]:
    return ['999','1000']
#returning stations that do not exist 

def get_graph():
    stations_list = me.extract_data('_dataset/london.stations.csv')
    lines_list = me.extract_data('_dataset/london.lines.csv')
    connections_list = me.extract_data('_dataset/london.connections.csv')
    
    g = Graph(stations_list, lines_list, connections_list)
    return g.connections

def is_correct_pair(gr, st1, st2):
    for i in gr[st1].neighbours:
        if (st2 == i[0]):
            return True
    print("returning false ")
    return False

def is_correct_route(gr, path_details):
    time = int(path_details[0])
    path = path_details[1]
    details = path_details[2]

    test_time = 0
    for i in range(1, len(path)):
        st1 = path[i-1]
        st2 = path[i]
        if(not is_correct_pair(gr,st1,st2)):
            return (False)
        pair_line = details[i-1][0]
        pair_time = details[i-1][1]
        test_time += int(pair_time)
    print("---------------------------------------------------------------------------------------------------------------------")
    print(test_time == time)
    return (test_time == time)

@pytest.fixture 
def all_paths(no_path, two_diff_paths, two_same_paths, no_stations):
    return [no_path, two_diff_paths, two_same_paths, no_stations]

@pytest.mark.parametrize("algorithm_name", ['Dijkstra', 'AStar'])
def test_path_finder_algorithms(algorithm_name, all_paths):
    gr = get_graph()
    for path in all_paths:
        path_query = [gr, path[0], path[1]]
        result = pf.build(algorithm_name,path_query)()
        if result is not None:
            error = "not correct for " + path[0] + " and " + path[1] + "result is: "+ ' '.join(result[1]) + "time is "+result[0]
            assert is_correct_route(gr, result), error