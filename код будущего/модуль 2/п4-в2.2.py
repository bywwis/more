def bfs(graph, start, end):
    queue = []
    visited = {}
    distance = {}

    queue.append(start)
    visited[start] = True
    distance[start] = 0

    while queue:
        current_vertex = queue.pop(0)

        if current_vertex == end:
            return distance[current_vertex]

        for neighbor in graph[current_vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited[neighbor] = True
                distance[neighbor] = distance[current_vertex] + 1

    return -1

if __name__ == '__main__':

    graph = {1: [2, 3],
            2: [1, 3, 4, 5],
            3: [1, 2, 4],
            4: [2, 3, 5, 7],
            5: [2, 4, 6, 7],
            6: [5, 7],
            7: [4, 5, 6],
            8: [9, 10],
            9: [8, 10],
            10: [8, 9]}

    start = int(input("Введите начальную вершину: "))
    end = int(input("Введите конечную вершину: "))

    result = bfs(graph, start, end)
    print("Длина кратчайшего пути: ", result)
