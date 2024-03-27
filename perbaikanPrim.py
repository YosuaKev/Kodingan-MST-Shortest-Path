import sys

def prim(graph, start, end):
    visited = set()
    visited.add(start)
    min_cost = 0
    path = []

    while len(visited) < len(graph):
        min_edge = (None, None, sys.maxsize)
        for node in visited:
            for neighbor, cost in graph[node].items():
                if neighbor not in visited and cost < min_edge[2]:
                    min_edge = (node, neighbor, cost)

        visited.add(min_edge[1])
        min_cost += min_edge[2]
        path.append((min_edge[0], min_edge[1]))

    return min_cost, path

graph = {
    'Kota A': {'Kota B': 9, 'Kota D': 10, 'Kota F': 3},
    'Kota B': {'Kota A': 9, 'Kota C': 5, 'Kota D': 6, 'Kota E': 5, 'Kota F': 11},
    'Kota C': {'Kota B': 5, 'Kota E': 8},
    'Kota D': {'Kota A': 10, 'Kota B': 6, 'Kota E': 6, 'Kota F': 6},
    'Kota E': {'Kota B': 5, 'Kota C': 8, 'Kota D': 6, 'Kota F': 9},
    'Kota F': {'Kota A': 3, 'Kota B': 11, 'Kota D': 6, 'Kota E': 9},
}

start_city = 'Kota A'
end_city = 'Kota C'

min_cost, path = prim(graph, start_city, end_city)
print("Biaya minimum:", min_cost)
print("Jalur terpendek:")
for edge in path:
    print(edge[0], "->", edge[1])
