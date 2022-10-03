import os
import sys

script_dir = os.path.dirname(__file__)
mymodule_dir = os.path.join(script_dir, '..', 'src')
sys.path.append(mymodule_dir)

import metrics_extractor
import graph
import pytest

def retrieve_data_case_1():
    stations_list = metrics_extractor.extract_data(
        '../../_samples/case1-london.stations.csv')
    lines_list = metrics_extractor.extract_data(
        '../../_samples/case1-london.lines.csv')
    connections_list = metrics_extractor.extract_data(
        '../../_samples/case1-london.connections.csv')

    return stations_list, lines_list, connections_list

def test_graph_num_nodes():
    stations_list, lines_list, connections_list = retrieve_data_case_1()
    g = graph.Graph(stations_list, lines_list, connections_list)

    num_nodes = g.num_stations
    assert num_nodes == 9


def test_graph_num_connections():
    stations_list, lines_list, connections_list = retrieve_data_case_1()
    g = graph.Graph(stations_list, lines_list, connections_list)

    num_connections = g.num_connections
    assert num_connections == 20


def test_graph_num_lines():
    stations_list, lines_list, connections_list = retrieve_data_case_1()
    g = graph.Graph(stations_list, lines_list, connections_list)

    num_lines = g.num_lines
    assert num_lines == 1


def test_graph_avg_degree():
    stations_list, lines_list, connections_list = retrieve_data_case_1()
    g = graph.Graph(stations_list, lines_list, connections_list)

    avg_degree = round(g.average_degree(), 2)
    assert avg_degree == 2.22


def test_graph_connection_keys():
    stations_list, lines_list, connections_list = retrieve_data_case_1()
    g = graph.Graph(stations_list, lines_list, connections_list)

    connections_keys = list(g.connections.keys())
    assert connections_keys == ['1', '2', '4', '5', '3', '7', '9', '6', '8']


def test_graph_connection_values():
    stations_list, lines_list, connections_list = retrieve_data_case_1()
    g = graph.Graph(stations_list, lines_list, connections_list)

    connections_values = []
    for key in g.connections.keys():
        connections_values.append(g.connections[key].neighbours)
    assert connections_values == [[['2', '13', '14'], ['4', '13', '34'], ['5', '13', '24']], [['1', '13', '14'], ['3', '13', '14']], [['1', '13', '34'], ['3', '13', '34'], ['9', '13', '14']], [['1', '13', '24'], [
        '6', '13', '34']], [['2', '13', '14'], ['4', '13', '34'], ['7', '13', '24']], [['3', '13', '24'], ['8', '13', '24']], [['4', '13', '14'], ['8', '13', '14']], [['5', '13', '34']], [['7', '13', '24'], ['9', '13', '14']]]
