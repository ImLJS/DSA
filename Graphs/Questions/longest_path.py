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