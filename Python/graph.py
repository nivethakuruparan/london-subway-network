from .station import *
from .line import *


class Graph:
    def __init__(self, stations_list, lines_list, connections_list):
        self.stations_list = stations_list
        self.lines_list = lines_list
        self.connections_list = connections_list

        self.num_stations = 0  # number of stations
        self.num_lines = 0  # number of lines
        self.num_connections = 0  # number of connections

        self.connections = {}  # dictionary in the form {station_id (str) : Station (object)}
        self.lines = {}  # dictionary in the form {line (str) : Line (object)}

        for connection in connections_list:
            self.add_connection(connection[0], connection[1], connection[2], connection[3])

    def add_connection(self, station1, station2, line, time):
        if station1 not in self.connections:
            self.add_station(station1)

        if station2 not in self.connections:
            self.add_station(station2)

        if line not in self.lines:
            self.add_line(line)

        self.connections[station1].add_neighbour(self.connections[station2], self.lines[line], time)
        self.connections[station2].add_neighbour(self.connections[station1], self.lines[line], time)
        self.num_connections += 1

    def add_station(self, station):
        for station_list in self.stations_list:
            if station == station_list[0]:
                self.connections[station] = Station(station_list)
                self.num_stations += 1
                return

    def add_line(self, line):
        for line_list in self.lines_list:
            if line == line_list[0]:
                self.lines[line] = Line(line_list)
                self.num_lines += 1
                return

    def avg_degree(self):
        return (2 * self.num_connections) / self.num_stations
