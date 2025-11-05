import json
import re
from tkinter import Tk, filedialog
import openrouteservice
from math import radians, sin, cos, sqrt, atan2
import networkx as nx
from queue import PriorityQueue


def select_file():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Select your GeoJSON file",
        filetypes=[("GeoJSON files", "*.geojson"), ("All files", "*.*")]
    )
    if not file_path:
        print("No file selected. Exiting.")
        exit()
    return file_path


file_path = select_file()

try:
    with open(file_path, 'r') as file:
        data = json.load(file)
except FileNotFoundError:
    print("File not found. Please check the path and try again.")
    exit()


nodes_dict = {}
for feature in data['features']:
    node_id = feature['properties']['@id']
    coordinates = tuple(feature['geometry']['coordinates'])
    node_id_cleaned = re.sub(r'^node/', '', node_id)
    nodes_dict[node_id_cleaned] = coordinates


api_key = "your-own-api-key-here"
client = openrouteservice.Client(key=api_key)


def calculate_distance(coord1, coord2):
    try:
        result = client.directions(
            coordinates=[coord1, coord2],
            profile='driving-car',
            format='json'
        )
        distance = result['routes'][0]['summary']['distance']
        return distance
    except Exception as e:
        print(f"Error: {e}")
        return None


distances = {}
node_ids = list(nodes_dict.keys())
for i in range(len(node_ids)):
    for j in range(i + 1, len(node_ids)):
        id1, id2 = node_ids[i], node_ids[j]
        coord1, coord2 = nodes_dict[id1], nodes_dict[id2]
        distance = calculate_distance(coord1, coord2)
        if distance is not None:
            distances[(id1, id2)] = distance


def haversine(coord1, coord2):
    Earth_R = 6371000
    lon1, lat1 = radians(coord1[0]), radians(coord1[1])
    lon2, lat2 = radians(coord2[0]), radians(coord2[1])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return Earth_R * c


def calculate_heuristic(target_node, nodes_dict):
    target_coord = nodes_dict[target_node]
    heuristic_values = {}
    for node_id, coord in nodes_dict.items():
        heuristic_values[node_id] = haversine(coord, target_coord)
    return heuristic_values


def build_graph(distances):
    G = nx.Graph()
    for (node1, node2), distance in distances.items():
        G.add_edge(node1, node2, weight=distance)
    return G


def A_star(graph, start, target, heuristic):
    came_from = {start: None}
    g_score = {node: float('inf') for node in graph.nodes()}
    f_score = {node: float('inf') for node in graph.nodes()}

    g_score[start] = 0
    f_score[start] = heuristic[start]

    pq = PriorityQueue()
    pq.put((f_score[start], start))

    while not pq.empty():
        current_node_f, current_node = pq.get()

        if current_node == target:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = came_from[current_node]
            return path[::-1]

        for neighbor in graph.neighbors(current_node):
            new_g = g_score[current_node] + graph[current_node][neighbor]['weight']
            if new_g < g_score[neighbor]:
                came_from[neighbor] = current_node
                g_score[neighbor] = new_g
                f_score[neighbor] = new_g + heuristic[neighbor]
                pq.put((f_score[neighbor], neighbor))

    return None


print("Extracted Nodes:")
print("{")
for key, value in nodes_dict.items():
    print(f"    '{key}': {value},")
print("}")

print("COST_PATH between nodes:")
print("{")
for key, value in distances.items():
    print(f"    {key}: {value},")
print("}")

start_node = input("Enter the ID of the start node: ")
target_node = input("Enter the ID of the target node: ")

heuristic = calculate_heuristic(target_node, nodes_dict)

print("Heuristic values (Haversine distance to target node):")
print("{")
for node, value in heuristic.items():
    print(f"    '{node}': {value:.2f},")
print("}")

graph = build_graph(distances)
path = A_star(graph, start_node, target_node, heuristic)

if path:
    print("Shortest path:", path)
else:
    print("No path found between the selected nodes.")



