# Graph Notes

## Graphs

- Graphs are a collection of nodes and edges.
- Nodes are also called vertices.
- Edges are the lines connecting the nodes.
- Graphs can be directed or undirected.
- In directed graphs, the edges have a direction.
- In undirected graphs, the edges do not have a direction.
- Graphs can be cyclic or acyclic.
- In cyclic graphs, there is a cycle.
- In acyclic graphs, there is no cycle.
- Graphs can be weighted or unweighted.
- In weighted graphs, the edges have a weight.
- In unweighted graphs, the edges do not have a weight.
- Graphs can be connected or disconnected.
- In connected graphs, all nodes are reachable from every other node.
- In disconnected graphs, there are nodes that are not reachable from every other node.

## Graph Representation

- Graphs can be represented using an adjacency matrix or an adjacency list.
- In an adjacency matrix, a 2D array is used to represent the graph.
- In an adjacency list, a list of lists is used to represent the graph.

### Adjacency Matrix

- In an adjacency matrix, a 2D array is used to represent the graph.
- The rows and columns of the matrix represent the nodes.
- The value at `matrix[i][j]` is 1 if there is an edge between nodes `i` and `j`, and 0 otherwise.
- The space complexity of an adjacency matrix is O(V^2), where V is the number of vertices.
- The time complexity of checking if there is an edge between two nodes is O(1).

Example:

```
   0  1  2  3
0  0  1  1  0
1  1  0  1  1
2  1  1  0  1
3  0  1  1  0
```

Here, there is an edge between nodes 0 and 1, 0 and 2, 1 and 2, 1 and 3, 2 and 3.

### Adjacency List

- In an adjacency list, a list of lists is used to represent the graph.
- Each list represents the neighbors of a node.
- The space complexity of an adjacency list is O(V + E), where V is the number of vertices and E is the number of edges.
- The time complexity of checking if there is an edge between two nodes is O(V), where V is the number of vertices.

Example:

```
0: [1, 2]
1: [0, 2, 3]
2: [0, 1, 3]
3: [1, 2]
```

Here, node 0 has neighbors 1 and 2, node 1 has neighbors 0, 2, and 3, and so on.

## Graph Traversal

- Graph traversal is the process of visiting all the nodes in a graph.
- There are two main graph traversal algorithms: depth-first search (DFS) and breadth-first search (BFS).
- DFS explores as far as possible along each branch before backtracking.
- BFS explores the neighbor nodes before moving to the next level of neighbors.
- Both DFS and BFS can be used to find paths, connected components, and cycles in a graph.
- DFS can be implemented using recursion or a stack.
- BFS can be implemented using a queue.
- The time complexity of DFS and BFS is O(V + E), where V is the number of vertices and E is the number of edges.
- The space complexity of DFS and BFS is O(V), where V is the number of vertices.
- DFS is often used to find paths and connected components in a graph.
- BFS is often used to find the shortest path in a graph.

## Graph Algorithms

- There are many graph algorithms that can be used to solve various problems.
- Some common graph algorithms include Dijkstra's algorithm, Bellman-Ford algorithm, Floyd-Warshall algorithm, Kruskal's algorithm, Prim's algorithm, and Tarjan's algorithm.
- Dijkstra's algorithm is used to find the shortest path in a graph with non-negative edge weights.
- Bellman-Ford algorithm is used to find the shortest path in a graph with negative edge weights.
- Floyd-Warshall algorithm is used to find the shortest path between all pairs of nodes in a graph.
- Kruskal's algorithm is used to find the minimum spanning tree of a graph.
- Prim's algorithm is used to find the minimum spanning tree of a graph.
- Tarjan's algorithm is used to find the strongly connected components of a graph.
- These algorithms can be used to solve various graph problems such as finding the shortest path, finding the minimum spanning tree, and finding the strongly connected components.
