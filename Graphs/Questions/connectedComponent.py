# Q. Connected Component

# Given an undirected graph, find the number of connected components.

# Example

# Input:
# graph = {"a": ["b", "c"], "b": ["a"], "c": ["a"], "d": ["e"], "e": ["d"]}
# Output:
# 2


def connected_component(
    graph,
):  # O(V + E) time, O(V) space where V is the number of vertices and E is the number of edges
    visit = set()  # Initialize the set to store the visited nodes
    count = 0  # Initialize the count of connected components

    for node in graph:  # Iterate over the nodes in the graph
        if dfs(graph, node, visit):
            count += 1  # Increment the count of connected components

    return count  # Return the count of connected components


def dfs(graph, src, visit):  # Depth First Search
    if src in visit:  # If the source is already visited
        return False

    visit.add(src)  # Add the source to the visited set
    for neighbour in graph[src]:  # Iterate over the neighbours of the source
        dfs(graph, neighbour, visit)  # Recursively call the function

    return True  # Return True if all the nodes are visited


graph = {0: [4, 7], 1: [], 2: [], 3: [6], 4: [0], 6: [3], 7: [0], 8: []}
graph2 = {0: [8, 1, 5], 1: [0], 5: [0, 8], 8: [0, 5], 2: [3, 4], 3: [2, 4], 4: [3, 2]}

print(connected_component(graph))  # 5
print(connected_component(graph2))  # 2
