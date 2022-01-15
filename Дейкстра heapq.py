import sys
import heapq
import math
input = sys.stdin.readline
# n вершины m ребра
n, m = map(int, input().split())

graph = [[0 for j in range(n+1)] for i in range(n+1)]
for i in range(m):
    x, y, w = map(int, input().split())
    if x != y:
        if graph[x][y] == 0:
            graph[x][y] = w
            graph[y][x] = w
        else:
            graph[x][y] = min(graph[x][y], w)
            graph[y][x] = graph[x][y]

print(graph)

def dijkstra(G, n):
    shortest_distances = [math.inf]* (n+1)
    visited = {1}
    vertex = 1
    shortest_distances[vertex] = 0
    while vertex > 0:
        # находим мин расстояние от текущей до остальных
        for idx, _ in enumerate(G[vertex]):
            if idx not in visited and G[vertex][idx] != 0:
                pretendent = G[vertex][idx] + shortest_distances[vertex]
                shortest_distances[idx] = min(pretendent, shortest_distances[idx])
        # -1 когда посетили все вершины
        # в противном случае ищем минимум между элементами
        min_next_vertex = -1
        min_next_index = -1
        for i, value in enumerate(shortest_distances):
            if i not in visited and i > 0:
                if min_next_vertex == -1:
                    min_next_vertex = value
                    min_next_index = i
                elif min_next_vertex > value:
                    min_next_vertex = value
                    min_next_index = i
    
        vertex =  min_next_index
        visited.add(vertex)
    return shortest_distances
    

print(dijkstra(graph, n))