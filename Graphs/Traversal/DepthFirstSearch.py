# Depth First Search Algorithm

# Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges
# Space Complexity: O(V) where V is the number of vertices

# Directed Graph

from collections import deque


def dfs(graph, start):
    stack = deque([start])

    while stack:
        node = stack.pop()
        print(node)
        for neighbour in graph[node]:
            stack.append(neighbour)


graph = {"a": ["b", "c"], "b": ["d"], "c": ["e"], "d": ["f"], "e": [], "f": []}

source = "a"
dfs(graph, source)  # a c e b d f
