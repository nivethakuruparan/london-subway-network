import heapq
from graph import *
from  Station import *

def h(vertex1, vertex2):
    return 1


def a_star_path(gr, start: int, end: int):
    open_list = set([start])
    # heapq.heappush(open_list, start)

    closed_list =set([])

    g = {}
    g[start] = 0 

    parents = {}
    parents[start] = start 

    while len(open_list)>0:
        print('entering loop')
        current = None 

        for i in open_list:
            if current == None or g[i] + h(i, end) < g[current] + h(current, end):
                current = i #choose node with lowest value of f

        if current == None:
            print("path does not exist")
            return None 

        if current == end:
            min_path = []

            while (parents[current] != current):
                min_path.append(current)
                current = parents[current]

            min_path.append(start)

            min_path.reverse()

            print("path exists")
            print(min_path)
            return min_path 

        # print("getting neighbours for")
        # print(current)
        # print(gr.get_connections(current))
        # print(gr.graph[current].adjacent.items())
        for i in gr.get_connections(current):
            print(i)
            neighbour = i[0]
            time = i[2]
            if neighbour not in open_list and neighbour not in closed_list:
                # heapq.heappush(open_list, neighbour)
                open_list.add(neighbour)
                parents[neighbour] = current 
                g[neighbour] = g[current] + time 

            else:
                if g[neighbour] > g[current] + time:
                    g[neighbour] = g[current] + time 
                    parents[neighbour] = current 

                    if neighbour in closed_list:
                        closed_list.remove(neighbour)
                        open_list.add(neighbour)
                        # heapq.heappush(open_list, neighbour)

        open_list.remove(current)
        # heapq.heappush(open_list, current)
        closed_list.add(current)

    print('path does not exist')goy 
    return None 
            