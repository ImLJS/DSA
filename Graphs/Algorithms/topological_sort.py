# Topological Sort

# Topological Sort is a linear ordering of vertices such that for every directed edge u -> v,
# vertex u comes before v in the ordering.

# Topological Sort is only possible in Directed Acyclic Graphs (DAGs).

# Topological Sort can be done using Depth First Search (DFS) or Breadth First Search (BFS).

# Topological Sort can be used to solve problems like scheduling tasks, course prerequisites, and more.

# The time complexity of Topological Sort is O(V + E), where V is the number of vertices and E is the number of edges.

# The space complexity of Topological Sort is O(V), where V is the number of vertices.

# Here is an example of Topological Sort using Depth First Search (DFS):


def topological_sort(graph):  # Depth First Search
    def dfs(node):
        visited.add(node)  # Add the node to the visited set
        for neighbor in graph[node]:  # For each neighbor of the node,
            if neighbor not in visited:  # If the neighbor has not been visited,
                dfs(neighbor)  # Recursively call the function on the neighbor
        result.append(node)  # Add the node to the result list

    visited = set()  # Create a visited set
    result = []  # Create a result list
    for node in graph:  # For each node in the graph,
        if node not in visited:  # If the node has not been visited,
            dfs(node)  # Call the dfs function on the node
    return result[::-1]  # Return the result list in reverse order


graph = {
    "A": ["C", "D"],
    "B": ["D"],
    "C": ["E"],
    "D": ["E"],
    "E": [],
}

print(topological_sort(graph))  # ['A', 'B', 'D', 'C', 'E'] or ['B', 'A', 'D', 'C', 'E']
