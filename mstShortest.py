import heapq

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

def prim(graph):
    mst = set()
    visited = set()
    start_node = list(graph.keys())[0]
    visited.add(start_node)

    edges = [(weight, start_node, neighbor) for neighbor, weight in graph[start_node].items()]
    heapq.heapify(edges)

    while edges:
        weight, node1, node2 = heapq.heappop(edges)
        if node2 not in visited:
            visited.add(node2)
            mst.add((node1, node2))
            for neighbor, weight in graph[node2].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (weight, node2, neighbor))

    return mst

graph = {
    'Kota A': {'Kota B': 12, 'Kota D': 14, 'Kota F': 11},
    'Kota B': {'Kota A': 12, 'Kota C': 15, 'Kota D': 18, 'Kota E': 17, 'Kota F':20 },
    'Kota C': {'Kota B': 15, 'Kota E': 13},
    'Kota D': {'Kota A': 14, 'Kota B': 18, 'Kota E': 11, 'Kota F': 16},
    'Kota E': {'Kota B': 17, 'Kota C': 13, 'Kota D': 11, 'Kota F': 10},
    'Kota F': {'Kota A': 11, 'Kota B': 20, 'Kota D': 16, 'Kota E': 10},
}

# Dijkstra
shortest_distance = dijkstra(graph, 'Kota A', 'Kota C')
print("Jarak terpendek antara Kota A dan Kota C (menggunakan Dijkstra):", shortest_distance)

# Prim
mst = prim(graph)
print("Minimum Spanning Tree (MST) yang dihasilkan (menggunakan Prim):", mst)
