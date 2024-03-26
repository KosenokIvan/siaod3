from copy import deepcopy


def floyd_warshall(graph_):
    min_distances = deepcopy(graph_)
    n = len(min_distances)
    for i in range(n):
        min_distances[i][i] = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                min_distances[i][j] = min(min_distances[i][j], min_distances[i][k] + min_distances[k][j])
    return min_distances
