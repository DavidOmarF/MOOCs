# Write two functions, the first, validity_check which takes a potential
# cover and the adjacency matrix of a graph as its inputs and returns True
# if the potential cover is a cover of the graph and False otherwise.
# The second, vertex_cover_naive, takes the adjacency matrix of a graph
# as its input, checks all potential covers, and returns the size of a
# minimum vertex cover. You should assume there are no loops in the graph.

from itertools import *

def get_edges(graph):
    n = len(graph)
    edges = []
    for i in range(n):
        for j in range (0, i):
            if graph[i][j] == 1:
                edges.append([i, j])
    return edges

def validity_check(cover, graph, edges):
    vertices = [i for i, x in enumerate(cover) if x == 1]
    for edge in edges:
        if edge[0] not in vertices and edge[1] not in vertices:
            return False
    return True

def vertex_cover_naive(input_graph):
    n = len(input_graph)
    minimum_vertex_cover = n
    edges = get_edges(input_graph)
    for assignment in product([0,1], repeat=n):
        cover = list(assignment)
        if validity_check(cover, input_graph, edges):
            try:
                cover_size = cover.count(1)
            except NameError:
                cover_size = 0
            if cover_size < minimum_vertex_cover:
                minimum_vertex_cover = cover_size
    return minimum_vertex_cover

def test():
    graph = [[0, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 1, 1],
            [1, 0, 1, 0, 1],
            [1, 1, 1, 1, 0]]

    print(vertex_cover_naive(graph))
    assert vertex_cover_naive(graph)==3

# If you've not seen testing like this before, all you need to do is
# to call test(). If the tests pass, you'll get no output. If they don't
# you'll get an assertion error. Don't forget to remove the call to the
# test before submitting your code.

test()