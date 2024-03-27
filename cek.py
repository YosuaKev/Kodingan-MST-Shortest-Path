import heapq

# Algoritma Dijkstra untuk mencari jalur terpendek dalam graf
def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous_nodes = {}

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    path = []
    current = end
    while current in previous_nodes:
        path.insert(0, current)
        current = previous_nodes[current]
    path.insert(0, start)

    return distances[end], path

# Data graf yang diberikan
graph = {
    'Kota A': {'Kota B': 12, 'Kota D': 14, 'Kota F': 11},
    'Kota B': {'Kota A': 12, 'Kota C': 15, 'Kota D': 18, 'Kota E': 17, 'Kota F':20 },
    'Kota C': {'Kota B': 15, 'Kota E': 13},
    'Kota D': {'Kota A': 14, 'Kota B': 18, 'Kota E': 11, 'Kota F': 16},
    'Kota E': {'Kota B': 17, 'Kota C': 13, 'Kota D': 11, 'Kota F': 10},
    'Kota F': {'Kota A': 11, 'Kota B': 20, 'Kota D': 16, 'Kota E': 10},
}

# Fungsi untuk mencari jalur terpendek antara kota A dan kota C
def shortest_path(graph, start, end):
    shortest_distance, path = dijkstra(graph, start, end)
    
    # Memeriksa apakah kota C adalah tetangga langsung dari kota A
    if end not in graph[start]:
        print("Tidak ada jalur yang terhubung dengan jarak terpendek antara Kota", start, "dan Kota", end)
        return
    
    print("Jarak terpendek antara Kota", start, "dan Kota", end, "adalah:", shortest_distance)
    print("Jalur terpendek antara Kota", start, "dan Kota", end, "adalah:", ' -> '.join(path))

# Menemukan jalur terpendek antara kota A dan kota C menggunakan algoritma Dijkstra pada graf asli
shortest_path(graph, 'Kota A', 'Kota C')
