# Longest Path

# Write a function, longest_path, that takes in an adjacency list for a directed acyclic graph.
# The function should return the length of the longest path within the graph.
# A path may start and end at any two nodes. The length of a path is considered the number of
# edges in the path, not the number of nodes.

# Example:

# graph = {
#   'a': ['c', 'b'],
#   'b': ['c'],
#   'c': []
# }
#
# longest_path(graph) # -> 2

# graph = {
#   'a': ['c', 'b'],
#   'b': ['c'],
#   'c': [],
#   'q': ['r'],
#   'r': ['s', 'u', 't'],
#   's': ['t'],
#   't': ['u'],
#   'u': []
# }
#
# longest_path(graph) # -> 4


def longest_path(graph):  # O(V+E)
    def dfs(node):
        if node in cache:  # If node is in cache, return the value
            return cache[node]
        if not graph[node]:  # If no neighbors,
            return 0
        max_path = 0  # Initialize max path
        for neighbor in graph[node]:
            max_path = max(max_path, dfs(neighbor) + 1)  # max path from neighbor + 1
        cache[node] = max_path  # Store the max path in cache
        return max_path

    cache = {}  # Store the max path for each node
    maxpath = 0  # Initialize max path
    for node in graph:
        maxpath = max(maxpath, dfs(node))  # max path from each node
    return maxpath


graph = {"a": ["c", "b"], "b": ["c"], "c": []}

graph2 = {
    "a": ["c", "b"],
    "b": ["c"],
    "c": [],
    "q": ["r"],
    "r": ["s", "u", "t"],
    "s": ["t"],
    "t": ["u"],
    "u": [],
}

print(longest_path(graph))  # -> 2
print(longest_path(graph2))  # -> 4
