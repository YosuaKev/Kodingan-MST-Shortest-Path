import heapq

def prim(graph):
    mst = []
    visited = set()
    heap = [(0, None, 'Kota A')]  

    while len(visited) < len(graph):
        cost, parent, node = heapq.heappop(heap)
        if node not in visited:
            visited.add(node)
            if parent:
                mst.append((parent, node, cost))
            for neighbor, neighbor_cost in graph[node].items():
                if neighbor not in visited:
                    heapq.heappush(heap, (neighbor_cost, node, neighbor))

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

mst = prim(graph)
print("Jalur terpendek untuk menghubungkan semua kota:")
for edge in mst:
    print(edge[0], "->", edge[1], ": jarak", edge[2])
print("Total jarak jalur terpendek:", total_distance(mst))
