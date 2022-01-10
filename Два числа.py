from sys import path

n, m = [int(x) for x in input().split()]

graph = {}
limit = 2*m if m%2 else m
print('limit', limit)
for i in range(2*m, 0, -1):
    graph[i] = []
    if limit >= 2*i:
        graph[i].append(i*2)
    if i - 1 != 0:
        graph[i].append(i-1)


# print(graph)


def bfs(graph, start):
    path = []
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        if vertex in graph:
            if vertex not in path:
                path.append(vertex)
                queue.extend(graph[vertex])
    return path


res = bfs(graph, n)
res = res[0:res.index(m)+1]

print('res', res)
print('len', len(res))
odd_i = []
even_i = []
for i in range(0, len(res)):
    if i % 2:
        even_i.append(res[i])
    else:
        odd_i.append(res[i])
if res.index(m) % 2 == 0:
    # print(odd_i)
    print('odd_i',len(odd_i) - 1)
else:
    # print(even_i)
    print('even_i', len(even_i))