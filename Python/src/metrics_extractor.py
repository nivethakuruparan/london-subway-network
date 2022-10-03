import csv


def extract_data(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        data = list(reader)

    return [x for x in data if x]

# Used for benchmarking
def extract_connection_pairs(filename):
    data = extract_data(filename)
    connection_pairs = []
    for line in data:
        connection_pairs.append([line[0], line[1]])

    return connection_pairs