# Q. Minimum Island Area

# Given a 2D array matrix of W's and L's (W representing water and L representing land),
# return the area of the smallest island in matrix.

# An island is surrounded by water and is formed by connecting adjacent lands


def dfs(matrix, row, col, visited):  # Depth First Search
    if (  # if row or col is out of bounds or if the cell is water
        not 0 <= row < len(matrix)
        or not 0 <= col < len(matrix[0])
        or matrix[row][col] == "W"
    ):
        return 0
    if (row, col) in visited:  # if the cell has already been visited
        return 0
    visited.add((row, col))  # add the cell to the visited set
    size = 1  # initialize the size of the island to 1
    size += dfs(
        matrix, row + 1, col, visited
    )  # recursively call dfs on all 4 directions
    size += dfs(matrix, row - 1, col, visited)
    size += dfs(matrix, row, col + 1, visited)
    size += dfs(matrix, row, col - 1, visited)
    return size  # return the size of the island


def minimum_island(matrix):
    min_count = float("inf")  # initialize the minimum count to infinity
    visited = set()  # set to keep track of visited cells

    rows = len(matrix)
    cols = len(matrix[0])

    for row in range(rows):  # iterate through the matrix
        for col in range(cols):
            size = dfs(matrix, row, col, visited)  # call dfs on the cell
            if (
                0 < size < min_count
            ):  # if the size of the island is greater than 0 and less than the minimum count
                min_count = size

    return min_count  # return the minimum count


grid = [
    ["L", "L", "L"],
    ["L", "L", "L"],
    ["L", "L", "L"],
]

grid2 = [["W", "W"], ["L", "L"], ["W", "W"], ["W", "L"]]

print(minimum_island(grid))  # -> 9
print(minimum_island(grid2))  # -> 1
