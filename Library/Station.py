class Station():
    def __init__(self, node):
        self.id = node
        self.adjacent = {} #dictionary with key= neighbour station number, value = list of Line and time(int)
        self.latitude = 0
        self.longitude = 0 
        self.name = ''
        self.zone = 0
        self.total_lines = 0
        self.rail = 0
    
    def add_neighbour(self, neighbour, line, time):
        self.adjacent[neighbour] = [line, time]

    def set_latitude(self, lat):
        self.latitude = lat

    def set_longitude(self, long):
        self.longitude = long 

    def set_name(self, name):
        self.name = name

    def set_zone(self, zone):
        self.zone = zone

    def set_total_lines(self, tl):
        self.total_lines = tl

    def set_rail(self, rail):
        self.rail = rail

    def get_connections(self):
        #returns a list containing 0-> neighbour id, 1-> line object, 2-> time/weight 
        connections = []
        for key,value in self.adjacent.items():
            connections.append((key, value[0], value[1]))
        return connections

    def get_id(self):
        return self.id
    
    def get_time(self, neighbour):
        return self.adjacent[neighbour]

    def get_latitude(self):
        return self.latitude

    def get_longitude(self):
        return self.longitude

    def get_name(self):
        return self.name

    def get_zone(self):
        return self.zone

    def get_total_lines(self):
        return self.total_lines

    def get_rail(self):
        return self.rail