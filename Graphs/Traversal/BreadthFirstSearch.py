# Breadth First Search Algorithm

# Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges
# Space Complexity: O(V) where V is the number of vertices

# Directed Graph

from collections import deque


def bfs(graph, source):
    stack = deque([source])

    while stack:
        node = stack.popleft()
        print(node)
        for neighbour in graph[node]:
            stack.append(neighbour)


graph = {"a": ["b", "c"], "b": ["d"], "c": ["e"], "d": ["f"], "e": [], "f": []}

source = "a"

bfs(graph, source)  # a b c d e f
