import heapq

def dijkstra(graph, start):
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

    return distances

def update_shortest_paths(graph):
    # Hitung jalur terpendek dari kota A ke kota C
    shortest_path_AC = dijkstra(graph, 'Kota A')['Kota C']
    
    for city in graph.keys():
        if city != 'Kota A' and city != 'Kota C':
            # Hitung jalur terpendek dari kota A ke kota saat ini
            shortest_path_from_A = dijkstra(graph, 'Kota A')[city]
            
            # Hitung jalur terpendek dari kota saat ini ke kota C
            shortest_path_to_C = dijkstra(graph, city)['Kota C']
            
            # Periksa apakah jalur terpendek yang dihitung menghubungkan kota tersebut ke kota A dan kota C
            if shortest_path_from_A + shortest_path_to_C != shortest_path_AC:
                # Jika tidak, tambahkan atau perbarui jalur terpendek yang dihitung
                graph['Kota A'][city] = shortest_path_from_A
                graph[city]['Kota C'] = shortest_path_to_C

    # Pastikan bahwa graf masih terhubung setelah memperbarui jalur-jalur terpendek
    # Di sini, Anda dapat menambahkan logika tambahan untuk memastikan keterhubungan graf, jika diperlukan

# Contoh graf
graph = {
    'Kota A': {'Kota B': 12, 'Kota D': 14, 'Kota F': 11},
    'Kota B': {'Kota A': 12, 'Kota C': 15, 'Kota D': 18, 'Kota E': 17, 'Kota F':20 },
    'Kota C': {'Kota B': 15, 'Kota E': 13},
    'Kota D': {'Kota A': 14, 'Kota B': 18, 'Kota E': 11, 'Kota F': 16},
    'Kota E': {'Kota B': 17, 'Kota C': 13, 'Kota D': 11, 'Kota F': 10},
    'Kota F': {'Kota A': 11, 'Kota B': 20, 'Kota D': 16, 'Kota E': 10},
}

# Perbarui jalur-jalur terpendek dalam graf
update_shortest_paths(graph)

# Cetak graf setelah pembaruan
print(graph)
