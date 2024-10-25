# best bridge
#
# Write a function, best_bridge, that takes in a grid as an argument.
# The grid contains water (W) and land (L). There are exactly two islands in the grid.
# An island is a vertically or horizontally connected region of land.
# Return the minimum length bridge needed to connect the two islands.
# A bridge does not need to form a straight line.

# Example:

# grid = [
#   ["W", "W", "W", "L", "L"],
#   ["L", "L", "W", "W", "L"],
#   ["L", "L", "L", "W", "L"],
#   ["W", "L", "W", "W", "W"],
#   ["W", "W", "W", "W", "W"],
#   ["W", "W", "W", "W", "W"],
# ]
# best_bridge(grid) # -> 1

# grid = [
#   ["W", "W", "W", "W", "W"],
#   ["W", "W", "W", "W", "W"],
#   ["L", "L", "W", "W", "L"],
#   ["W", "L", "W", "W", "L"],
#   ["W", "W", "W", "L", "L"],
#   ["W", "W", "W", "W", "W"],
# ]
# best_bridge(grid) # -> 2


def best_bridge(grid):

    def dfs(grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != "L":
            return
        grid[i][j] = "W"
        islands[-1].append((i, j))
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            dfs(grid, i + di, j + dj)

    islands = [[]]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "L":
                dfs(grid, i, j)
                islands.append([])

    island1, island2 = islands[0], islands[1]
    min_bridge = float("inf")
    for i1, j1 in island1:
        for i2, j2 in island2:
            min_bridge = min(min_bridge, abs(i1 - i2) + abs(j1 - j2) - 1)

    return min_bridge


grid = [
    ["W", "W", "W", "L", "L"],
    ["L", "L", "W", "W", "L"],
    ["L", "L", "L", "W", "L"],
    ["W", "L", "W", "W", "W"],
    ["W", "W", "W", "W", "W"],
    ["W", "W", "W", "W", "W"],
]

print(best_bridge(grid))  # -> 1

grid = [
    ["W", "W", "W", "W", "W"],
    ["W", "W", "W", "W", "W"],
    ["L", "L", "W", "W", "L"],
    ["W", "L", "W", "W", "L"],
    ["W", "W", "W", "L", "L"],
    ["W", "W", "W", "W", "W"],
]

print(best_bridge(grid))  # -> 2
