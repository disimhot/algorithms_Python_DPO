def main():
    G = read_graph()
    start = input('С какой вершины начать')
    shortest_distances = dijkstra(G, start)
    finish = input('К какой вершине построить?')

    shortest_path = reveal_shortest_path(start, finish, shortest_distances)



if __name__= "__main__":
    main()