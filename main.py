import googlemaps
import responses
import datetime
from graph_lib import *
import math

# Vancouver, North Vancouver, West Vancouver, Burnaby, Richmond, Surrey, New
# Westminster, Delta, Langley, Abbotsford, Chilliwack, Hope, Mission.

DEBUGMODE=False

#offline data
minimum_distance_between_cities = [
{'origin': 'Vancouver, BC, Canada', 'destination': 'North Vancouver, BC, Canada', 'weight': 10136},
{'origin': 'Vancouver, BC, Canada', 'destination': 'West Vancouver, BC, Canada', 'weight': 8579},
{'origin': 'Vancouver, BC, Canada', 'destination': 'Burnaby, BC, Canada', 'weight': 12840},
{'origin': 'Vancouver, BC, Canada', 'destination': 'Richmond, BC, Canada', 'weight': 15815},
{'origin': 'Vancouver, BC, Canada', 'destination': 'Surrey, BC, Canada', 'weight': 29199},
{'origin': 'Vancouver, BC, Canada', 'destination': 'New Westminster, BC, Canada', 'weight': 21302},
{'origin': 'Vancouver, BC, Canada', 'destination': 'Delta, BC, Canada', 'weight': 25324},
{'origin': 'Vancouver, BC, Canada', 'destination': 'Langley, BC, Canada', 'weight': 49679},
{'origin': 'Vancouver, BC, Canada', 'destination': 'Abbotsford, BC, Canada', 'weight': 71439},
{'origin': 'Vancouver, BC, Canada', 'destination': 'Chilliwack, BC, Canada', 'weight': 102022},
{'origin': 'Vancouver, BC, Canada', 'destination': 'Hope, BC, Canada', 'weight': 151828},
{'origin': 'Vancouver, BC, Canada', 'destination': 'Mission, BC, Canada', 'weight': 67228},
{'origin': 'North Vancouver, BC, Canada', 'destination': 'West Vancouver, BC, Canada', 'weight': 6591},
{'origin': 'North Vancouver, BC, Canada', 'destination': 'Burnaby, BC, Canada', 'weight': 15049},
{'origin': 'North Vancouver, BC, Canada', 'destination': 'Richmond, BC, Canada', 'weight': 28698},
{'origin': 'North Vancouver, BC, Canada', 'destination': 'Surrey, BC, Canada', 'weight': 31408},
{'origin': 'North Vancouver, BC, Canada', 'destination': 'New Westminster, BC, Canada', 'weight': 23510},
{'origin': 'North Vancouver, BC, Canada', 'destination': 'Delta, BC, Canada', 'weight': 35447},
{'origin': 'North Vancouver, BC, Canada', 'destination': 'Langley, BC, Canada', 'weight': 51888},
{'origin': 'North Vancouver, BC, Canada', 'destination': 'Abbotsford, BC, Canada', 'weight': 73647},
{'origin': 'North Vancouver, BC, Canada', 'destination': 'Chilliwack, BC, Canada', 'weight': 104231},
{'origin': 'North Vancouver, BC, Canada', 'destination': 'Hope, BC, Canada', 'weight': 154036},
{'origin': 'North Vancouver, BC, Canada', 'destination': 'Mission, BC, Canada', 'weight': 69436},
{'origin': 'West Vancouver, BC, Canada', 'destination': 'Burnaby, BC, Canada', 'weight': 23217},
{'origin': 'West Vancouver, BC, Canada', 'destination': 'Richmond, BC, Canada', 'weight': 23739},
{'origin': 'West Vancouver, BC, Canada', 'destination': 'Surrey, BC, Canada', 'weight': 39061},
{'origin': 'West Vancouver, BC, Canada', 'destination': 'New Westminster, BC, Canada', 'weight': 33789},
{'origin': 'West Vancouver, BC, Canada', 'destination': 'Delta, BC, Canada', 'weight': 33248},
{'origin': 'West Vancouver, BC, Canada', 'destination': 'Langley, BC, Canada', 'weight': 59541},
{'origin': 'West Vancouver, BC, Canada', 'destination': 'Abbotsford, BC, Canada', 'weight': 81300},
{'origin': 'West Vancouver, BC, Canada', 'destination': 'Chilliwack, BC, Canada', 'weight': 111884},
{'origin': 'West Vancouver, BC, Canada', 'destination': 'Hope, BC, Canada', 'weight': 161689},
{'origin': 'West Vancouver, BC, Canada', 'destination': 'Mission, BC, Canada', 'weight': 77089},
{'origin': 'Burnaby, BC, Canada', 'destination': 'Richmond, BC, Canada', 'weight': 20871},
{'origin': 'Burnaby, BC, Canada', 'destination': 'Surrey, BC, Canada', 'weight': 13886},
{'origin': 'Burnaby, BC, Canada', 'destination': 'New Westminster, BC, Canada', 'weight': 7367},
{'origin': 'Burnaby, BC, Canada', 'destination': 'Delta, BC, Canada', 'weight': 27864},
{'origin': 'Burnaby, BC, Canada', 'destination': 'Langley, BC, Canada', 'weight': 35227},
{'origin': 'Burnaby, BC, Canada', 'destination': 'Abbotsford, BC, Canada', 'weight': 59102},
{'origin': 'Burnaby, BC, Canada', 'destination': 'Chilliwack, BC, Canada', 'weight': 89685},
{'origin': 'Burnaby, BC, Canada', 'destination': 'Hope, BC, Canada', 'weight': 139491},
{'origin': 'Burnaby, BC, Canada', 'destination': 'Mission, BC, Canada', 'weight': 54891},
{'origin': 'Richmond, BC, Canada', 'destination': 'Surrey, BC, Canada', 'weight': 27835},
{'origin': 'Richmond, BC, Canada', 'destination': 'New Westminster, BC, Canada', 'weight': 21431},
{'origin': 'Richmond, BC, Canada', 'destination': 'Delta, BC, Canada', 'weight': 13403},
{'origin': 'Richmond, BC, Canada', 'destination': 'Langley, BC, Canada', 'weight': 44531},
{'origin': 'Richmond, BC, Canada', 'destination': 'Abbotsford, BC, Canada', 'weight': 75355},
{'origin': 'Richmond, BC, Canada', 'destination': 'Chilliwack, BC, Canada', 'weight': 106214},
{'origin': 'Richmond, BC, Canada', 'destination': 'Hope, BC, Canada', 'weight': 156019},
{'origin': 'Richmond, BC, Canada', 'destination': 'Mission, BC, Canada', 'weight': 71994},
{'origin': 'Surrey, BC, Canada', 'destination': 'New Westminster, BC, Canada', 'weight': 7051},
{'origin': 'Surrey, BC, Canada', 'destination': 'Delta, BC, Canada', 'weight': 25695},
{'origin': 'Surrey, BC, Canada', 'destination': 'Langley, BC, Canada', 'weight': 18324},
{'origin': 'Surrey, BC, Canada', 'destination': 'Abbotsford, BC, Canada', 'weight': 46086},
{'origin': 'Surrey, BC, Canada', 'destination': 'Chilliwack, BC, Canada', 'weight': 76670},
{'origin': 'Surrey, BC, Canada', 'destination': 'Hope, BC, Canada', 'weight': 126475},
{'origin': 'Surrey, BC, Canada', 'destination': 'Mission, BC, Canada', 'weight': 47209},
{'origin': 'New Westminster, BC, Canada', 'destination': 'Delta, BC, Canada', 'weight': 26663},
{'origin': 'New Westminster, BC, Canada', 'destination': 'Langley, BC, Canada', 'weight': 27761},
{'origin': 'New Westminster, BC, Canada', 'destination': 'Abbotsford, BC, Canada', 'weight': 53805},
{'origin': 'New Westminster, BC, Canada', 'destination': 'Chilliwack, BC, Canada', 'weight': 85325},
{'origin': 'New Westminster, BC, Canada', 'destination': 'Hope, BC, Canada', 'weight': 135130},
{'origin': 'New Westminster, BC, Canada', 'destination': 'Mission, BC, Canada', 'weight': 50531},
{'origin': 'Delta, BC, Canada', 'destination': 'Langley, BC, Canada', 'weight': 30508},
{'origin': 'Delta, BC, Canada', 'destination': 'Abbotsford, BC, Canada', 'weight': 61253},
{'origin': 'Delta, BC, Canada', 'destination': 'Chilliwack, BC, Canada', 'weight': 92112},
{'origin': 'Delta, BC, Canada', 'destination': 'Hope, BC, Canada', 'weight': 141917},
{'origin': 'Delta, BC, Canada', 'destination': 'Mission, BC, Canada', 'weight': 68476},
{'origin': 'Langley, BC, Canada', 'destination': 'Abbotsford, BC, Canada', 'weight': 31876},
{'origin': 'Langley, BC, Canada', 'destination': 'Chilliwack, BC, Canada', 'weight': 62460},
{'origin': 'Langley, BC, Canada', 'destination': 'Hope, BC, Canada', 'weight': 112265},
{'origin': 'Langley, BC, Canada', 'destination': 'Mission, BC, Canada', 'weight': 35283},
{'origin': 'Abbotsford, BC, Canada', 'destination': 'Chilliwack, BC, Canada', 'weight': 34257},
{'origin': 'Abbotsford, BC, Canada', 'destination': 'Hope, BC, Canada', 'weight': 84062},
{'origin': 'Abbotsford, BC, Canada', 'destination': 'Mission, BC, Canada', 'weight': 12334},
{'origin': 'Chilliwack, BC, Canada', 'destination': 'Hope, BC, Canada', 'weight': 52482},
{'origin': 'Chilliwack, BC, Canada', 'destination': 'Mission, BC, Canada', 'weight': 42936},
{'origin': 'Hope, BC, Canada', 'destination': 'Mission, BC, Canada', 'weight': 83037},
]

city_map = [
{'origin': 'Vancouver, BC, Canada', 'destination': 'North Vancouver, BC, Canada', 'weight': 10136},
{'origin': 'Vancouver, BC, Canada', 'destination': 'West Vancouver, BC, Canada', 'weight': 8579},
{'origin': 'Vancouver, BC, Canada', 'destination': 'Burnaby, BC, Canada', 'weight': 12840},
{'origin': 'Vancouver, BC, Canada', 'destination': 'Richmond, BC, Canada', 'weight': 15815},
{'origin': 'North Vancouver, BC, Canada', 'destination': 'West Vancouver, BC, Canada', 'weight': 6591},
{'origin': 'North Vancouver, BC, Canada', 'destination': 'Burnaby, BC, Canada', 'weight': 15049},
{'origin': 'Burnaby, BC, Canada', 'destination': 'Richmond, BC, Canada', 'weight': 20871},
{'origin': 'Burnaby, BC, Canada', 'destination': 'Surrey, BC, Canada', 'weight': 13886},
{'origin': 'Burnaby, BC, Canada', 'destination': 'New Westminster, BC, Canada', 'weight': 7367},
{'origin': 'Burnaby, BC, Canada', 'destination': 'Mission, BC, Canada', 'weight': 54891},
{'origin': 'Richmond, BC, Canada', 'destination': 'Surrey, BC, Canada', 'weight': 27835},
{'origin': 'Richmond, BC, Canada', 'destination': 'New Westminster, BC, Canada', 'weight': 21431},
{'origin': 'Richmond, BC, Canada', 'destination': 'Delta, BC, Canada', 'weight': 13403},
{'origin': 'Surrey, BC, Canada', 'destination': 'New Westminster, BC, Canada', 'weight': 7051},
{'origin': 'Surrey, BC, Canada', 'destination': 'Delta, BC, Canada', 'weight': 25695},
{'origin': 'Surrey, BC, Canada', 'destination': 'Abbotsford, BC, Canada', 'weight': 46086},
{'origin': 'Surrey, BC, Canada', 'destination': 'Langley, BC, Canada', 'weight': 18324},
{'origin': 'Delta, BC, Canada', 'destination': 'Langley, BC, Canada', 'weight': 30508},
{'origin': 'Langley, BC, Canada', 'destination': 'Abbotsford, BC, Canada', 'weight': 31876},
{'origin': 'Abbotsford, BC, Canada', 'destination': 'Chilliwack, BC, Canada', 'weight': 34257},
{'origin': 'Abbotsford, BC, Canada', 'destination': 'Mission, BC, Canada', 'weight': 12334},
{'origin': 'Chilliwack, BC, Canada', 'destination': 'Hope, BC, Canada', 'weight': 52482},
]



locations = [
            "Vancouver, BC, Canada",
            "North Vancouver, BC, Canada",
            "West Vancouver, BC, Canada",
            "Burnaby, BC, Canada",
            "Richmond, BC, Canada",
            "Surrey, BC, Canada",
            "New Westminster, BC, Canada",
            "Delta, BC, Canada",
            "Langley, BC, Canada",
            "Abbotsford, BC, Canada",
            "Chilliwack, BC, Canada",
            "Hope, BC, Canada",
            "Mission, BC, Canada"
        ]
class GenerateData:
    def __init__(self):
        self.key = "null"
        self.client = googlemaps.Client(self.key)


    def generate_online_data(self):
        responses.add(responses.GET,
                      "https://maps.googleapis.com/maps/api/directions/json",
                      body='{"status":"OK", "rows":[]}',
                      status=200,
                      content_type="application/json",
                      )


        this_dict = []
        now = datetime.datetime.now()
        origin_iter = 0
        while origin_iter < len(locations):
            i = origin_iter + 1
            while i < len(locations):
                matrix = self.client.directions(locations[origin_iter], locations[i], mode="driving", language="en-US", units="metric", alternatives=True)

                j=0
                minimum_dist = matrix[0]['legs'][0]['distance']['value']
                while j < len(matrix):
                    if minimum_dist > int(matrix[j]['legs'][0]['distance']['value']):
                        minimum_dist = int(matrix[j]['legs'][0]['distance']['value'])
                    j += 1
                if DEBUGMODE:
                    print("[+] start: " + str(matrix[0]['legs'][0]['start_address']) + " end: " + str(matrix[0]['legs'][0]['end_address']) +  " smallest_distance: " + str(self.to_kilometers(minimum_dist)) + " km")
                this_dict.append({"origin": str(matrix[0]['legs'][0]['start_address']), "destination": str(matrix[0]['legs'][0]['end_address']), "weight": minimum_dist})
                i += 1
            origin_iter += 1
        return this_dict


def to_kilometers(meters):
    return meters / 1000


def PathFinder(start, goal, method="A_Star"):
    g = Graph()
    for x in locations:
        g.add_vertex(str(x))

    for y in city_map:
        g.add_edge(y['origin'], y['destination'], y['weight'])

    openSet = [g.vert_dict[start]]
    goal_node = g.vert_dict[goal]
    cameFrom = {}
    global final_distance
    final_distance = 0
    g.vert_dict[start].gScore = 0

    g.vert_dict[start].fScore = manhattan_distance(g.vert_dict[start], goal_node, minimum_distance_between_cities)

    while len(openSet) > 0:
        current_node = find_smallest_fScore(openSet)
        if current_node == goal_node:
            total_path = reconstruct_path(cameFrom, current_node)
            for y in total_path:
                print(y.get_id())
            i = 0
            while i < len(total_path) - 1:
                final_distance = final_distance + total_path[i].get_weight(total_path[i+1])
                i = i + 1

        openSet.remove(current_node)

        for x in current_node.get_all_adjacents():
            tentative_gScore = current_node.gScore + current_node.get_weight(x)
            if tentative_gScore < x.gScore:
                cameFrom[x] = current_node
                x.gScore = tentative_gScore
                x.fScore = tentative_gScore + manhattan_distance(x, goal_node, minimum_distance_between_cities)
                if x not in openSet:
                    openSet.append(x)


if __name__ == '__main__':
    start = input("Please enter a starting city IE. \"city, province, country\": ")
    goal = input("Please enter a goal city IE. \"city, province, country\": ")
    PathFinder(start, goal, "A_Star")
    print("Distance: " + str(to_kilometers(final_distance)) + " km")


















