# Q. Undirected Has Path

# Given an Undirected Graph and two vertices in it, check whether there is a
# path from the first given vertex to second.

# Example

# Input:

# graph = {"a": ["b", "c"], "b": ["a", "d"], "c": ["a", "e"], "d": ["b", "f"], "e": ["c"], "f": ["d"]}
# source = "a"
# destination = "f"

# Output:

# True

from collections import defaultdict


def convertToAdj(edges):  # O(E)
    graph = defaultdict(list)  # Create a defaultdict
    for u, v in edges:  # Iterate over the edges
        graph[u].append(v)  # Append the vertex v to the vertex u
        graph[v].append(u)  # Append the vertex u to the vertex v
    return graph


def dfs(
    graph, src, dst, visit
):  # O(V+E) - V is the number of vertices and E is the number of edges
    if src == dst:  # If the source is the destination
        return True

    if src in visit:  # If the source is already visited
        return False

    visit.add(src)  # Add the source to the visited set
    for neighbour in graph[src]:  # Iterate over the neighbours of the source
        if dfs(graph, neighbour, dst, visit):  # Recursively call the function
            return True

    return False  # Return False if no path is found


def hasPath(edges, src, dst):  # O(V+E)
    graph = convertToAdj(edges)  # Convert the edges to adjacency list
    return dfs(graph, src, dst, set())  # Call the dfs function


edges = [
    ("b", "a"),
    ("c", "a"),
    ("b", "c"),
    ("q", "r"),
    ("q", "s"),
    ("q", "u"),
    ("q", "t"),
]

print(hasPath(edges, "a", "b"))  # True
print(hasPath(edges, "a", "q"))  # False
