from Station import *
from Line import *
from a_star import *

class Graph(object):
    def __init__(self, connections, lines):
        print("starting graph")
        self.graph = {}
        self.edges = 0
        self.vertices = 0 
        self.add_connections(connections, lines)
      
    #graph is a dictionary key: station id, value: corresponding station object
    #key: station id 
    #value: station object with its adjacency list 
    def add_connections(self, connections, lines):
        for i in connections:
            vertex1 = int(i[0])
            vertex2 = int(i[1])
            st1_check = self.check_vertex(vertex1)
            st2_check = self.check_vertex(vertex2)

            new_ln = Line(int(i[2]))
            for j in lines:
                if j[0] == i[2]:
                    new_ln.set_name(j[1])
                    new_ln.set_colour(j[2])
                    new_ln.set_stripe(j[3])
                    break
                          
            conn_id = new_ln
            self.edges += 1
            t_weight = int(i[3])

            if(not st1_check):
                new_st = Station(vertex1)
                self.graph[vertex1] = new_st
                self.vertices += 1
            if(not st2_check):
                new_st = Station(vertex2)
                self.graph[vertex2] = new_st
                self.vertices += 1
                
            self.graph[vertex1].add_neighbour(vertex2, conn_id, t_weight)
            self.graph[vertex2].add_neighbour(vertex1, conn_id, t_weight)
        return 

    def get_connections(self, vertex):
        return self.graph[vertex].get_connections() 

    def check_vertex(self, vertex):
        if vertex in self.graph:  # check if vertex exists in keys
            return True 
        return False 

    def num_edges(self):
        return self.edges

    def num_vertices(self):
        return self.vertices

    def avg_degree(self):
        return self.edges / self.vertices

    