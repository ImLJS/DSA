# Prims Algorithm

# Prim's Algorithm is a greedy algorithm that finds a minimum spanning tree for a weighted undirected graph.
# This means it finds a subset of the edges that forms a tree that includes every vertex,
# where the total weight of all the edges in the tree is minimized.

# Time Complexity: O(V^2)
# Space Complexity: O(V)

# Algorithm:

# 1. Create a set mstSet that keeps track of vertices already included in MST.
# 2. Assign a key value to all vertices in the input graph. Initialize all key values as INFINITE.
#    Assign key value as 0 for the first vertex so that it is picked first.
# 3. While mstSet doesn't include all vertices:
#     a. Pick a vertex u which is not there in mstSet and has minimum key value.
#     b. Include u to mstSet.
#     c. Update key value of all adjacent vertices of u. To update the key values, iterate through all adjacent vertices.
#        For every adjacent vertex v, if weight of edge u-v is less than the previous key value of v, update the key value as weight of u-v.

# Implementation:

from collections import defaultdict


def prims(graph):
    V = len(graph)
    key = [float("inf")] * V
    parent = [None] * V
    mstSet = [False] * V
    key[0] = 0
    parent[0] = -1

    for _ in range(V):
        u = minKey(key, mstSet)
        mstSet[u] = True
        for v in range(V):
            if graph[u][v] and not mstSet[v] and graph[u][v] < key[v]:
                key[v] = graph[u][v]
                parent[v] = u

    return parent


def minKey(key, mstSet):
    min = float("inf")
    min_index = -1
    for v in range(len(key)):
        if key[v] < min and not mstSet[v]:
            min = key[v]
            min_index = v
    return min_index


# Example:

graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0],
]

parent = prims(graph)
for i in range(1, len(parent)):
    print(parent[i], "-", i, ":", graph[i][parent[i]])

# Output:

# 0 - 1 : 2
# 1 - 2 : 3
# 0 - 3 : 6
# 1 - 4 : 5
