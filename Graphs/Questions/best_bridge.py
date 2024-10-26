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
        if (
            i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != "L"
        ):  # out of bounds or not land
            return
        grid[i][j] = "W"  # mark as visited
        islands[-1].append((i, j))  # add to current island
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:  # check all 4 directions
            dfs(grid, i + di, j + dj)

    islands = [[]]  # store the two islands
    for i in range(len(grid)):  # find the two islands
        for j in range(len(grid[0])):
            if grid[i][j] == "L":  # if land
                dfs(grid, i, j)  # dfs to find the island
                islands.append([])

    island1, island2 = islands[0], islands[1]  # get the two islands
    min_bridge = float("inf")  # store the minimum bridge length
    for i1, j1 in island1:  # check all pairs of land cells from the two islands
        for i2, j2 in island2:
            min_bridge = min(
                min_bridge, abs(i1 - i2) + abs(j1 - j2) - 1
            )  # update the minimum bridge length

    return min_bridge  # return the minimum bridge length


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
