G = [[1, 3], [1, 6], [2, 3], [2, 4], [2, 5], [3, 4], [3, 6], [4, 5]]
print('Спимок рёбер для графа G:', *G)

adjacency_list = {1: [3, 6],
                  2: [3, 4, 5],
                  3: [1, 2, 4, 6],
                  4: [2, 3, 5],
                  5: [2, 4],
                  6: [1, 3]}
print('Список смежности для графа G:', adjacency_list)

matrix_adj = []
