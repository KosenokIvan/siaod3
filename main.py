from copy import deepcopy
from math import inf


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


def read_from_file(filename):
    with open(filename) as file:
        if file.readline().strip().lower().startswith("a"):
            return read_as_adjacency_matrix(file.readlines())
        else:
            return read_as_incidence_matrix(file.readlines())


def read_as_adjacency_matrix(lines):
    matrix = []
    for line in lines:
        if line:
            elements = line.split()
            row = []
            for el in elements:
                try:
                    row.append(int(el))
                except ValueError:
                    row.append(inf)
            matrix.append(row)
    return matrix


def read_as_incidence_matrix(lines):
    lines = [line for line in lines if line]
    edges = [{"from": -1, "to": -1, "length": -1} for _ in range(len(lines[0].split()))]
    for i, line in enumerate(lines):
        elements = line.split()
        for j, el in enumerate(elements):
            if int(el) > 0:
                edges[j]["from"] = i
                edges[j]["length"] = int(el)
            elif int(el) < 0:
                edges[j]["to"] = i
    matrix = [[inf for __ in range(len(lines))] for _ in range(len(lines))]
    for edge in edges:
        matrix[edge["from"]][edge["to"]] = edge["length"]
    return matrix


def main():
    print(*floyd_warshall(read_from_file("input1.txt")), sep="\n")


if __name__ == '__main__':
    main()
