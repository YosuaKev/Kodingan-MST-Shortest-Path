import heapq
from collections import defaultdict

def prim_mst(graph):
    mst = defaultdict(dict)
    visited = set()
    start_node = list(graph.keys())[0]
    priority_queue = [(0, None, start_node)]

    while priority_queue:
        weight, parent, current_node = heapq.heappop(priority_queue)
        if current_node not in visited:
            visited.add(current_node)
            if parent is not None:
                mst[parent][current_node] = weight
                mst[current_node][parent] = weight

            for neighbor, neighbor_weight in graph[current_node].items():
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (neighbor_weight, current_node, neighbor))

    return mst

def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances[end]

def shortest_path(graph, start, end):
    shortest_distance = dijkstra(graph, start, end)
    print("Jarak terpendek antara Kota", start, "dan Kota", end, "adalah:", shortest_distance)

graph = {
    'Kota A': {'Kota B': 12, 'Kota D': 14, 'Kota F': 11},
    'Kota B': {'Kota A': 12, 'Kota C': 15, 'Kota D': 18, 'Kota E': 17, 'Kota F':20 },
    'Kota C': {'Kota B': 15, 'Kota E': 13},
    'Kota D': {'Kota A': 14, 'Kota B': 18, 'Kota E': 11, 'Kota F': 16},
    'Kota E': {'Kota B': 17, 'Kota C': 13, 'Kota D': 11, 'Kota F': 10},
    'Kota F': {'Kota A': 11, 'Kota B': 20, 'Kota D': 16, 'Kota E': 10},
}

# Langkah 1: Membuat Minimum Spanning Tree
mst_graph = prim_mst(graph)
print("Minimum Spanning Tree:")
print(mst_graph)

# Langkah 2: Menggunakan Dijkstra untuk mencari jalur terpendek
shortest_path(mst_graph, 'Kota A', 'Kota C')
