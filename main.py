from copy import deepcopy
from math import inf, isinf
from pprint import pprint
import time
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


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


def making_nx_graph(graph_):
    graph_nx = nx.DiGraph()
    for i, row in enumerate(graph_):
        for j, el in enumerate(row):
            if isinf(el):
                el = 0
            if el != 0:
                graph_nx.add_edge(i, j, weight=el)
    return graph_nx


def measure_time(func_, graph_):
    start_time = time.time()
    print("=" * 30)
    pprint(graph_)
    pprint(func_(graph_))
    graph_nx = making_nx_graph(graph_)
    pos = nx.spring_layout(graph_nx)
    nx.draw(graph_nx, pos, with_labels=True)
    labels = nx.get_edge_attributes(graph_nx, 'weight')
    nx.draw_networkx_edge_labels(graph_nx, pos, edge_labels=labels)
    plt.show()
    print("--- {0} ms ---".format(round((time.time() - start_time) * 1000)))


def main():
    files = ["input1.txt", "input2.txt", "input3.txt", "input4.txt", "input5.txt", "input6.txt"]
    for filename in files:
        measure_time(floyd_warshall, read_from_file(filename))


if __name__ == '__main__':
    main()
