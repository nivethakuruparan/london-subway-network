import Python.metrics_extractor as metric_extractor
import random


def generate_kpi_data():
    kpi_data = {
        10: [],
        20: [],
        50: [],
        100: [],
        200: [],
        300: [],
        400: []
    }

    connection_pairs = metric_extractor.extract_connection_pairs('_dataset/london.connections.csv')
    connection_range = len(connection_pairs) - 1

    for item in kpi_data:
        count = 0
        while count < item:
            index = random.randint(0, connection_range)
            kpi_data[item].append(connection_pairs[index])
            count += 1

    return kpi_data


def generate_time_data(graph):
    degree_list = []

    for i in graph.values():
        degree_list.append((len(i.neighbours)))
        
    min_degree = min(degree_list)
    max_degree = max(degree_list)

    time_data = {i: None for i in range(min_degree, max_degree + 1)}

    for station in graph.values():
        degree = len(station.neighbours)

        if not time_data[degree]:
            index = random.randint(0, degree - 1)
            time_data[degree] = [station.id, station.neighbours[index][0]]

    time_data = {key: val for key, val in time_data.items() if val is not None}

    return time_data
