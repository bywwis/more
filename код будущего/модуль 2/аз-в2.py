adj_list = {1: [5, 6],
       2: [5, 7],
       3: [5, 6, 8, 9],
       4: [6, 8],
       5: [1, 2, 3, 7],
       6: [1, 3, 4, 8],
       7: [2, 5],
       8: [3, 4, 6],
       9: [3]}

visited = [False] * (len(adj_list) + 1)
ost_tree_node = []

def dfs(v):
    visited[v] = True
    ost_tree_node.append(v)
    for w in adj_list[v]:
        if not visited[w]:
            dfs(w)

v = int(input(f'Введите номер вершины графа G (от 1 до {len(adj_list)}): '))
if v < 1 or v >len(adj_list):
    print('Ошибка ввода вершины графа G')
else:
    dfs(v)
    edges_ost_tree = []
    w_t = ost_tree_node[0]

    for i in range(1, len(ost_tree_node)):
        u = ost_tree_node[i]
        if u in adj_list[w_t]:
            edges_ost_tree.append([w_t, u])
        else:
            for point in ost_tree_node:
                if u in adj_list[point]:
                    edges_ost_tree.append([point, u])
                    break
        w_t = u
    print('Вершины остовного дерева: ', ost_tree_node)
    print('Рёбра остовного дерева: ', edges_ost_tree)

