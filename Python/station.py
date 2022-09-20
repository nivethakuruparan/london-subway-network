class Station(object):
    def __init__(self, station_list):
        self.id = station_list[0]
        self.neighbours = []

    def add_neighbour(self, neighbour, line, time):
        neighbour_details = [neighbour.id, line, time]
        self.neighbours.append(neighbour_details)
