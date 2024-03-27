import heapq

def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    pq = [(0, start)]
    
    path = {start: []}
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        if current_node == end:
            return distances[end], path[end]
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
                path[neighbor] = path[current_node] + [(current_node, neighbor)]
    
    return float('inf'), []

distance_graph = {
    'Kota A': {'Kota B': 12, 'Kota D': 14, 'Kota F': 11},
    'Kota B': {'Kota A': 12, 'Kota C': 15, 'Kota D': 18, 'Kota E': 17, 'Kota F': 20},
    'Kota C': {'Kota B': 15, 'Kota E': 13},
    'Kota D': {'Kota A': 14, 'Kota B': 18, 'Kota E': 11, 'Kota F': 16},
    'Kota E': {'Kota B': 17, 'Kota C': 13, 'Kota D': 11, 'Kota F': 10},
    'Kota F': {'Kota A': 11, 'Kota B': 20, 'Kota D': 16, 'Kota E': 10},
}

repair_cost = {
    'Kota A': {'Kota B': 9, 'Kota D': 10, 'Kota F': 3},
    'Kota B': {'Kota A': 9, 'Kota C': 5, 'Kota D': 6, 'Kota E': 5, 'Kota F': 11},
    'Kota C': {'Kota B': 5, 'Kota E': 8},
    'Kota D': {'Kota A': 10, 'Kota B': 6, 'Kota E': 6, 'Kota F': 6},
    'Kota E': {'Kota B': 5, 'Kota C': 8, 'Kota D': 6, 'Kota F': 9},
    'Kota F': {'Kota A': 3, 'Kota B': 11, 'Kota D': 6, 'Kota E': 9},
}

shortest_distance, shortest_path = dijkstra(distance_graph, 'Kota A', 'Kota C')
total_cost = sum(repair_cost[a][b] for a, b in shortest_path)

print("Jalur terpendek antara Kota A dan Kota C:", shortest_path)
print("Jarak terpendek:", shortest_distance)
print("Biaya total perbaikan:", total_cost)
print("Jalur yang dikunjungi untuk jalur terpendek antara Kota A dan Kota C:")
for edge in shortest_path:
    print(edge[0], "->", edge[1])

