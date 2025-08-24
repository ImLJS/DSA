# Q. Largest Component
from sys import maxsize


# Given an undirected graph, find the size of the largest connected component.

# Example

# Input:
# graph = {"a": ["b", "c"], "b": ["a"], "c": ["a"], "d": ["e"], "e": ["d"]}
# Output:
# 3


def largest_component(
    graph,
):  # O(V + E) time, O(V) space where V is the number of vertices and E is the number of edges
    max_size = 0  # Initialize the maximum size of the connected component
    visit = set()  # Initialize the set to store the visited nodes

    for node in graph:
        size = dfs(graph, node, visit)  # Call the dfs function
        max_size = max(
            size, max_size
        )  # Update the maximum size of the connected component

    return max_size  # Return the maximum size of the connected component


def dfs(graph, node, visit):

    if node in visit:  # If the node is already visited
        return 0

    visit.add(node)  # Add the node to the visited set

    size = 1  # Initialize the size of the connected component
    for neighbour in graph[node]:
        size += dfs(
            graph, neighbour, visit
        )  # Recursively call the function and update the size

    return size  # Return the size of the connected component


graph = {0: [4, 7], 1: [], 2: [], 3: [6], 4: [0], 6: [3], 7: [0], 8: []}
print(largest_component(graph))  # 3

graph2 = {0: [8, 1, 5], 1: [0], 5: [0, 8], 8: [0, 5], 2: [3, 4], 3: [2, 4], 4: [3, 2]}
print(largest_component(graph2))  # 4
