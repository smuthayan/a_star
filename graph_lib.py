import math
import random
#credits for graph class: https://www.bogotobogo.com/python/python_graph_data_structures.php
class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        self.gScore = math.inf
        self.fScore = math.inf

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def __repr(self):
        return str(self.id)

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def get_all_adjacents(self):
        return self.get_connections()

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()





def find_smallest_fScore(openSet):
    minimum = math.inf
    smallest_node = None
    for x in openSet:
        if x.fScore < minimum:
            minimum = x.fScore
            smallest_node = x
    return smallest_node

def reconstruct_path(cameFrom, current):
    total_path = [current]
    while current in cameFrom.keys():
        current = cameFrom[current]
        total_path.insert(0, current)
    return total_path

# distance from node_n to goal node. So I get
def manhattan_distance(node_n, goal_node, data_list):
    x_coord = 0
    for y in data_list:
        if (y['origin'] == node_n.get_id() and y['destination'] == goal_node.get_id()) or (y['origin'] == goal_node.get_id() and y['destination'] == node_n.get_id()):
            x_coord = y['weight']
    y_coord = random.randint(5000, 10000)
    return abs(x_coord - y_coord)