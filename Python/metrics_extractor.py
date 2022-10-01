import csv
from http.client import NOT_EXTENDED


def extract_data(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        data = list(reader)

    return data

#used for benchmarking 
def extract_connection_pairs(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        data = list(reader)
    
    conn_pairs = []
    for line in data:
        conn_pairs.append([line[0], line[1]])

    return conn_pairs