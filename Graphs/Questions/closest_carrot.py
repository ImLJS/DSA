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

from collections import deque


def closest_carrot(matrix, row, col):  # Breadth First Search
    ROW = len(matrix)
    COL = len(matrix[0])
    visit = set()
    queue = deque(
        [(row, col, 0)]
    )  # Store the row, column, and distance from the starting position
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]  # Store the directions to move

    while queue:
        r, c, distance = (
            queue.popleft()
        )  # Get the row, column, and distance from the queue

        if (  # If the row or column is out of bounds or if the cell is a wall or if the cell has already been visited
            not 0 <= r < ROW
            or not 0 <= c < COL
            or matrix[r][c] == "X"
            or (r, c) in visit
        ):
            continue
        if matrix[r][c] == "C":  # If the cell is a carrot,
            return distance
        visit.add((r, c))  # Add the cell to the visited set

        for x, y in directions:  # Iterate over the directions
            dx, dy = r + x, c + y
            queue.append(
                (dx, dy, distance + 1)
            )  # Add the row, column, and distance to the queue

    return -1  # Return -1 if there is no possible path to a carrot


grid = [
    ["O", "O", "X", "O", "O"],
    ["O", "X", "X", "X", "O"],
    ["O", "X", "C", "C", "O"],
]

grid2 = [
    ["O", "O", "O", "O", "O"],
    ["O", "X", "O", "O", "O"],
    ["O", "X", "X", "O", "O"],
    ["O", "X", "C", "O", "O"],
    ["O", "X", "X", "O", "O"],
    ["C", "O", "O", "O", "O"],
]

grid3 = [
    ["O", "O", "O", "O", "O"],
    ["O", "X", "O", "O", "O"],
    ["O", "X", "X", "O", "O"],
    ["O", "X", "C", "O", "O"],
    ["O", "X", "X", "O", "O"],
    ["C", "O", "O", "O", "O"],
]


print(closest_carrot(grid, 0, 0))  # -> -1
print(closest_carrot(grid2, 0, 0))  # -> 5
print(closest_carrot(grid3, 1, 2))  # -> 4
