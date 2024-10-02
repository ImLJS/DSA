# Q. Has Path
#
# Given a Directed Acyclic Graph and two vertices in it, check whether there is a path
# from the first given vertex to second.
#
# Example
#
# Input:
#
# graph = {"a": ["b", "c"], "b": ["d"], "c": ["e"], "d": ["f"], "e": [], "f": []}
#
# source = "a"
# destination = "f"
#
# Output:
#
# True

from collections import deque


def hasPath_dfs(graph, source, destination):
    if source == destination:  # If the source is the destination
        return True

    for neighbor in graph[source]:  # Iterate over the neighbors of the source
        if hasPath_dfs(graph, neighbor, destination):  # Recursively call the function
            return True

    return False


def hasPath_bfs(graph, source, destination):
    queue = deque([source])  # Initialize the queue with the source node

    while queue:
        node = queue.popleft()  # Pop the first element from the queue
        if node == destination:  # If the node is the destination
            return True

        for neighbor in graph[node]:  # Iterate over the neighbors of the node
            queue.append(neighbor)  # Add the neighbor to the queue

    return False


graph = {"a": ["b", "c"], "b": ["d"], "c": ["e"], "d": ["f"], "e": [], "f": []}
source = "a"
destination = "f"

print(hasPath_dfs(graph, source, destination))  # True
print(hasPath_bfs(graph, source, destination))  # True

graph = {"a": ["b", "c"], "b": ["d"], "c": ["e"], "d": ["f"], "e": [], "f": []}

source = "a"
destination = "g"

print(hasPath_dfs(graph, source, destination))  # False
print(hasPath_bfs(graph, source, destination))  # False
