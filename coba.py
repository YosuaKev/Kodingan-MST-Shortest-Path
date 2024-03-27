def prim_with_path(graph, start_node, end_node):
    # Inisialisasi himpunan solusi
    solution = []
    
    # Inisialisasi himpunan simpul yang sudah dipilih
    selected_nodes = set()
    
    # Inisialisasi dictionary untuk melacak jalur
    path = {start_node: None}
    
    # Pilih simpul awal
    selected_nodes.add(start_node)
    
    # Loop hingga simpul tujuan terpilih
    while end_node not in selected_nodes:
        min_edge = None
        min_cost = float('inf')
        
        # Loop melalui setiap simpul yang sudah dipilih
        for node in selected_nodes:
            # Loop melalui setiap sisi yang terhubung dengan simpul yang sudah dipilih
            for neighbor, cost in graph[node].items():
                # Jika tetangga belum terpilih dan biayanya lebih kecil dari minimum sejauh ini
                if neighbor not in selected_nodes and cost < min_cost:
                    min_cost = cost
                    min_edge = (node, neighbor)
                    path[neighbor] = node
        
        # Tambahkan sisi dengan biaya minimum ke dalam himpunan solusi
        solution.append((min_edge[0], min_edge[1], min_cost))
        selected_nodes.add(min_edge[1])
    
    # Membuat jalur dari simpul awal ke simpul tujuan
    path_list = []
    current_node = end_node
    while current_node != start_node:
        path_list.insert(0, current_node)
        current_node = path[current_node]
    path_list.insert(0, start_node)
    
    return solution, path_list

# Data yang diberikan
graph = {
    'Kota A': {'Kota B': 9, 'Kota D': 10, 'Kota F': 3},
    'Kota B': {'Kota A': 9, 'Kota C': 5, 'Kota D': 6, 'Kota E': 5, 'Kota F': 11},
    'Kota C': {'Kota B': 5, 'Kota E': 8},
    'Kota D': {'Kota A': 10, 'Kota B': 6, 'Kota E': 6, 'Kota F': 6},
    'Kota E': {'Kota B': 5, 'Kota C': 8, 'Kota D': 6, 'Kota F': 9},
    'Kota F': {'Kota A': 3, 'Kota B': 11, 'Kota D': 6, 'Kota E': 9},
}

# Panggil fungsi Prim dengan jalur
solution, path = prim_with_path(graph, 'Kota A', 'Kota C')

# Hitung biaya total minimum
total_cost = sum(edge[2] for edge in solution)

print("Jalur yang Dilewati dari Kota A ke Kota C:")
print(" -> ".join(path))
print("\nHimpunan Sisi Terpilih:")
for edge in solution:
    print(edge[0], "-", edge[1], ": Biaya", edge[2])

print("\nBiaya Minimum:", total_cost)
