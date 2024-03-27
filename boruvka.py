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

def boruvka(graph):
    parent = {}
    rank = {}

    # Inisialisasi setiap kota sebagai parent dari dirinya sendiri
    for kota in graph.keys():
        parent[kota] = kota
        rank[kota] = 0

    mst = []
    while len(mst) < len(graph) - 1:
        cheapest = {}
        # Temukan sisi terpendek yang terhubung ke setiap komponen
        for kota in graph.keys():
            for neighbor, cost in graph[kota].items():
                kota_root = find(parent, kota)
                neighbor_root = find(parent, neighbor)
                if kota_root != neighbor_root:
                    if kota_root not in cheapest or cost < cheapest[kota_root][1]:
                        cheapest[kota_root] = (neighbor, cost)

        # Gabungkan setiap komponen dengan sisi terpendek
        for root, (neighbor, cost) in cheapest.items():
            if root != find(parent, neighbor):
                mst.append((root, neighbor, cost))
                union(parent, rank, root, neighbor)

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

mst = boruvka(graph)
print("Jalur terpendek untuk menghubungkan semua kota:")
for edge in mst:
    print(edge[0], "->", edge[1], ": jarak", edge[2])
print("Total jarak jalur terpendek:", total_distance(mst))
