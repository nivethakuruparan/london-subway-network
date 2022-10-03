class Station(object):
    def __init__(self, station_list):
        self.id = station_list[0]
        self.latitude = station_list[1]
        self.longitude = station_list[2]
        self.name = station_list[3]
        self.display_name = station_list[4]
        self.zone = station_list[5]
        self.total_lines = station_list[6]
        self.rail = station_list[7]

        self.neighbours = []
        self.lines = {}

    def add_neighbour(self, neighbour, line, time):
        if line not in self.lines:
            self.add_line(line)

        neighbour_details = [neighbour.id, line.line, time]
        self.neighbours.append(neighbour_details)

    def add_line(self, line):
        self.lines[line.line] = line

