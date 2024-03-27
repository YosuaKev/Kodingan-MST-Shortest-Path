import heapq

def dijkstra(graph, start):
    # Inisialisasi jarak ke semua titik dengan nilai tak terhingga
    distances = {node: float('inf') for node in graph}
    # Inisialisasi jarak dari start ke start dengan nilai 0
    distances[start] = 0
    # Priority queue untuk menyimpan node yang akan dievaluasi
    queue = [(0, start)]
    
    while queue:
        # Ambil node dengan jarak terpendek dari antrian
        current_distance, current_node = heapq.heappop(queue)
        
        # Lewati node yang telah dikunjungi
        if current_distance > distances[current_node]:
            continue
        
        # Perbarui jarak ke tetangga-tetangga
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            # Jika jarak baru lebih pendek, perbarui nilai jarak
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    
    return distances

# Data jarak antar kota
graph_distances = {
    'Kota A': {'Kota B': 12, 'Kota D': 14, 'Kota F': 11},
    'Kota B': {'Kota A': 12, 'Kota C': 15, 'Kota D': 18, 'Kota E': 17, 'Kota F': 20},
    'Kota C': {'Kota B': 15, 'Kota E': 13},
    'Kota D': {'Kota A': 14, 'Kota B': 18, 'Kota E': 11, 'Kota F': 16},
    'Kota E': {'Kota B': 17, 'Kota C': 13, 'Kota D': 11, 'Kota F': 10},
    'Kota F': {'Kota A': 11, 'Kota B': 20, 'Kota D': 16, 'Kota E': 10},
}

# Data biaya perbaikan
graph_repairs = {
    'Kota A': {'Kota B': 9, 'Kota D': 10, 'Kota F': 3},
    'Kota B': {'Kota A': 9, 'Kota C': 5, 'Kota D': 6, 'Kota E': 5, 'Kota F': 11},
    'Kota C': {'Kota B': 5, 'Kota E': 8},
    'Kota D': {'Kota A': 10, 'Kota B': 6, 'Kota E': 6, 'Kota F': 6},
    'Kota E': {'Kota B': 5, 'Kota C': 8, 'Kota D': 6, 'Kota F': 9},
    'Kota F': {'Kota A': 3, 'Kota B': 11, 'Kota D': 6, 'Kota E': 9},
}

# Kota asal dan tujuan
start_city = 'Kota A'
end_city = 'Kota C'

# Hitung jarak terpendek dari kota asal ke semua kota lainnya
distances = dijkstra(graph_distances, start_city)

# Biaya perbaikan terpendek dari kota asal ke tujuan
repair_cost = graph_repairs[start_city][end_city]

# Total biaya minimum
total_cost = distances[end_city] + repair_cost

print("Jarak terpendek dari", start_city, "ke", end_city, "adalah", distances[end_city])
print("Biaya perbaikan terpendek dari", start_city, "ke", end_city, "adalah", repair_cost)
print("Total biaya minimum:", total_cost)
