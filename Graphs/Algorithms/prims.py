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
    V = len(graph)  # Number of vertices
    key = [float("inf")] * V  # Key values used to pick minimum weight edge in cut
    parent = [None] * V  # Array to store constructed MST
    mstSet = [False] * V  # To represent set of vertices included in MST
    key[0] = 0  # Make key 0 so that this vertex is picked as first vertex
    parent[0] = -1  # First node is always root of MST

    for _ in range(V):
        u = minKey(
            key, mstSet
        )  # Pick the minimum key vertex from the set of vertices not yet included in MST
        mstSet[u] = True  # Add the picked vertex to the MST Set
        for v in range(V):
            if (
                graph[u][v] and not mstSet[v] and graph[u][v] < key[v]
            ):  # Update key value and parent index of the adjacent vertices of the picked vertex
                key[v] = graph[u][
                    v
                ]  # Update the key only if graph[u][v] is smaller than key[v]
                parent[v] = u  # Set the parent of vertex v to u

    return parent  # Return the constructed MST


def minKey(key, mstSet):
    min = float("inf")  # Initialize min value
    min_index = -1  # Initialize min_index
    for v in range(len(key)):
        if (
            key[v] < min and not mstSet[v]
        ):  # Pick the minimum key vertex from the set of vertices not yet included in MST
            min = key[v]  # Update the min value
            min_index = v  # Update the min_index
    return min_index


# Example:

graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0],
]

parent = prims(graph)  # Construct the MST
for i in range(1, len(parent)):  # Print the constructed MST
    print(parent[i], "-", i, ":", graph[i][parent[i]])  # Print the edge and its weight

# Output:

# 0 - 1 : 2
# 1 - 2 : 3
# 0 - 3 : 6
# 1 - 4 : 5
