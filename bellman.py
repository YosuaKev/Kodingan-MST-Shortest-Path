def bellman_ford(graph, start, end):
    # Inisialisasi jarak ke setiap node dengan infinity, kecuali start node dengan jarak 0
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Lakukan relaksasi sebanyak V-1 kali (V adalah jumlah node dalam graf)
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    # Periksa adanya siklus negatif
    for node in graph:
        for neighbor, weight in graph[node].items():
            if distances[node] + weight < distances[neighbor]:
                raise ValueError("Graf memiliki siklus negatif")

    return distances[end]

# Fungsi untuk menemukan jalur terpendek
def shortest_path(graph, start, end):
    shortest_distance = bellman_ford(graph, start, end)
    print("Jarak terpendek antara Kota", start, "dan Kota", end, "adalah:", shortest_distance)

# Contoh graf yang merepresentasikan jarak antar kota
# Kode ini adalah kode yang kita buat sendiri
graph = {
    'Kota A': {'Kota B': 12, 'Kota D': 14, 'Kota F': 11},
    'Kota B': {'Kota A': 12, 'Kota C': 15, 'Kota D': 18, 'Kota E': 17, 'Kota F':20 },
    'Kota C': {'Kota B': 15, 'Kota E': 13},
    'Kota D': {'Kota A': 14, 'Kota B': 18, 'Kota E': 11, 'Kota F': 16},
    'Kota E': {'Kota B': 17, 'Kota C': 13, 'Kota D': 11, 'Kota F': 10},
    'Kota F': {'Kota A': 11, 'Kota B': 20, 'Kota D': 16, 'Kota E': 10},
}

# Menemukan jalur terpendek antara Kota 1 dan Kota 2
shortest_path(graph, 'Kota A', 'Kota C')
