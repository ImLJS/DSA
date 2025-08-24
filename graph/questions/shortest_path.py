# Q. Shortest Path between two vertices

# Given a list of edges, and two vertices, find the shortest path between the two vertices.
# If there is no path between the two vertices, return -1.

# Example:
# edges = [
#     ["a", "c"],
#     ["a", "b"],
#     ["c", "b"],
#     ["c", "d"],
#     ["b", "d"],
#     ["e", "d"],
#     ["g", "f"],
# ]

# shortest_path(edges, "b", "g") => -1
# shortest_path(edges, "e", "c") => 2
# shortest_path(edges, "a", "e") => 3

from collections import defaultdict, deque


def convert_to_adjacency_list(edge):  # Convert edge list to adjacency list
    graph = defaultdict(list)  # Using default dict to avoid key errors
    for u, v in edge:  # u -> v
        graph[u].append(v)  # Add v to u's list
        graph[v].append(u)  # Add u to v's list
    return graph  # Return adjacency list


def shortest_path(edge, src, dst):
    graph = convert_to_adjacency_list(edge)  # Convert edge list to adjacency list
    queue = deque([(src, 0)])  # Initialize queue with source and distance
    visited = {src}  # Initialize visited set with source

    while queue:
        node, distance = queue.popleft()  # Pop the first element from the queue
        if node == dst:  # If the node is the destination, return the distance
            return distance

        for neighbour in graph[node]:  # For each neighbour of the node
            if neighbour not in visited:  # If the neighbour is not visited
                queue.append(
                    (neighbour, distance + 1)
                )  # Add the neighbour to the queue with distance + 1
                visited.add(neighbour)  # Add the neighbour to the visited set

    return -1  # If no path is found, return -1


edges = [
    ["a", "c"],
    ["a", "b"],
    ["c", "b"],
    ["c", "d"],
    ["b", "d"],
    ["e", "d"],
    ["g", "f"],
]

print(shortest_path(edges, "b", "g"))  # -1
print(shortest_path(edges, "e", "c"))  # 2
print(shortest_path(edges, "a", "e"))  # 3

# Time Complexity: O(V + E)
# Space Complexity: O(V + E)
