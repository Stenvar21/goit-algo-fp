import heapq

def dijkstra(graph, start):
    # Відстані від початкової вершини до всіх інших
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    
    # Створення мін-купу (бінарної купи) для зберігання вершин з їхніми відстанями
    pq = [(0, start)]  # (відстань, вершина)
    
    # Пройдемо через всі вершини графа
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        
        # Якщо поточна відстань більша, ніж вже знайдена, пропускаємо цю вершину
        if current_distance > distances[current_vertex]:
            continue
        
        # Перевірка суміжних вершин
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            
            # Якщо знайдена нова коротша відстань
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

# Приклад графа
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)],
}

# Викликаємо алгоритм Дейкстри для знаходження найкоротших шляхів від 'A'
start_vertex = 'A'
shortest_paths = dijkstra(graph, start_vertex)

print(f"Найкоротші шляхи від вершини {start_vertex}:")
for vertex, distance in shortest_paths.items():
    print(f"До вершини {vertex} відстань: {distance}")
