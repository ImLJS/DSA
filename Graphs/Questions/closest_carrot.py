# Closest Carrot

# Write a function, closest_carrot, that takes in a grid, a starting row, and a starting column.
# In the grid, 'X's are walls, 'O's are open spaces, and 'C's are carrots.
# The function should return a number representing the length of the shortest path from the
# starting position to a carrot. You may move up, down, left, or right,
# but cannot pass through walls (X). If there is no possible path to a carrot, then return -1.
# You may assume that the grid will contain at least one carrot.

# Example:

# grid = [
#   ['O', 'O', 'O', 'O', 'O'],
#   ['O', 'X', 'O', 'O', 'O'],
#   ['O', 'X', 'X', 'O', 'O'],
#   ['O', 'X', 'C', 'O', 'O'],
#   ['O', 'X', 'X', 'O', 'O'],
#   ['C', 'O', 'O', 'O', 'O'],
# ]
#
# closest_carrot(grid, 1, 2) # -> 4

# grid = [
#   ['O', 'O', 'O', 'O', 'O'],
#   ['O', 'X', 'O', 'O', 'O'],
#   ['O', 'X', 'X', 'O', 'O'],
#   ['O', 'X', 'C', 'O', 'O'],
#   ['O', 'X', 'X', 'O', 'O'],
#   ['C', 'O', 'O', 'O', 'O'],
# ]
#
# closest_carrot(grid, 0, 0) # -> 5
