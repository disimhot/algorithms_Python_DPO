from collections import deque


def main():
    G = read_graph()
    start = input('С какой вершины начать')
    shortest_distances = dijkstra(G, start)
    finish = input('К какой вершине построить?')

    shortest_path = reveal_shortest_path(start, finish, shortest_distances)

def read_graph():
    # М - количество ребер, далее А-Б-вес
    M = int(input())
    G = {}
    for i in range(M):
        a, b, weight = input().split()
        weight = float(weight)
        add_edge(G, a, b, weight)
        add_edge(G, b, a, weight)

    return G

def add_edge(G, a, b, weight):
    if a not in G:
        G[a] = {b: weight}
    else:
        G[a][b] = weight

def dijkstra(G, start):
    Q = deque()
    # shortest_distances
    s = {}
    s[start] = 0
    Q.push(start)
    while Q:
        v = Q.pop()
        # смежные вершины к v и обновим кратчайщее расстояние у них
        for u in G[v]:
            # s[v]+G[v][u] потенциальное кратч расстояние
            if u not in s or (s[v] + G[v][u]) < s[u]:
                s[u] = s[v] + G[v][u]
                Q.push(u)
    return s

def reveal_shortest_path(start, finish, s):
    pass
 
if __name__= "__main__":
    main()