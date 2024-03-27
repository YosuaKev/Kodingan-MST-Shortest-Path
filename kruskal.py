def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)

    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    else:
        parent[y_root] = x_root
        rank[x_root] += 1

def kruskal(graph):
    # Inisialisasi MST kosong
    mst = []
    # Inisialisasi himpunan untuk menyimpan kota yang sudah ada di MST
    parent = {k: k for k in graph.keys()}
    rank = {k: 0 for k in graph.keys()}

    # Urutkan semua sisi berdasarkan bobotnya
    edges = [(graph[u][v], u, v) for u in graph for v in graph[u]]
    edges.sort()

    # Lakukan loop untuk setiap sisi
    for edge in edges:
        cost, u, v = edge
        # Jika sisi tidak membentuk siklus, tambahkan ke MST
        if find(parent, u) != find(parent, v):
            mst.append((u, v, cost))
            union(parent, rank, u, v)

    return mst

def total_distance(mst):
    return sum(cost for _, _, cost in mst)

graph = {
    'Kota A': {'Kota B': 12, 'Kota D': 14, 'Kota F': 11},
    'Kota B': {'Kota A': 12, 'Kota C': 15, 'Kota D': 18, 'Kota E': 17, 'Kota F': 20},
    'Kota C': {'Kota B': 15, 'Kota E': 13},
    'Kota D': {'Kota A': 14, 'Kota B': 18, 'Kota E': 11, 'Kota F': 16},
    'Kota E': {'Kota B': 17, 'Kota C': 13, 'Kota D': 11, 'Kota F': 10},
    'Kota F': {'Kota A': 11, 'Kota B': 20, 'Kota D': 16, 'Kota E': 10},
}

mst = kruskal(graph)
print("Jalur terpendek untuk menghubungkan semua kota:")
for edge in mst:
    print(edge[0], "->", edge[1], ": jarak", edge[2])
print("Total jarak jalur terpendek:", total_distance(mst))
