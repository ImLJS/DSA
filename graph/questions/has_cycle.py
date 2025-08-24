# has cycle
#
# Write a function, has_cycle, that takes in an object representing the adjacency list
# of a directed graph. The function should return a boolean indicating whether the
# graph contains a cycle.

# Example:

# has_cycle({
#   "a": ["b"],
#   "b": ["c"],
#   "c": ["a"],
# }) # -> True

# has_cycle({
#   "a": ["b", "c"],
#   "b": ["c"],
#   "c": ["d"],
#   "d": [],
# }) # -> False


def has_cycle(graph):
    visited = set()
    rec_stack = set()

    def dfs(node):
        if (
            node in rec_stack
        ):  # if the node is in the recursion stack, then there is a cycle
            return True
        if (
            node in visited
        ):  # if the node has already been visited, then there is no cycle
            return False

        visited.add(node)  # add the node to the visited set
        rec_stack.add(node)  # add the node to the recursion stack

        for neighbor in graph[node]:  # recursively call dfs on the neighbors
            if dfs(neighbor):
                return True

        rec_stack.remove(node)  # remove the node from the recursion stack
        return False

    for node in graph:
        if dfs(node):  # if there is a cycle, return True
            return True
    return False  # if there is no cycle, return False


graph = {
    "a": ["b"],
    "b": ["c"],
    "c": ["a"],
}

print(has_cycle(graph))  # -> True

graph = {
    "a": ["b", "c"],
    "b": ["c"],
    "c": ["d"],
    "d": [],
}

print(has_cycle(graph))  # -> False
